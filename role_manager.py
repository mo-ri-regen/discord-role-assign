import discord
import pandas as pd
import os
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))

intents = discord.Intents.default()
intents.members = True  # メンバー情報を取得するために必要

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    guild = discord.utils.get(client.guilds, id=GUILD_ID)

    # CSVファイルを読み込む（Discord名とメンバー名の列が必要）
    df = pd.read_csv('members.csv')

    for index, row in df.iterrows():
        discord_name = str(row['Discord名']).strip()
        role_name = str(row['ロール名']).strip()

        # ユーザー名からメンバーを検索
        member = discord.utils.get(guild.members, name=discord_name.split('#')[0])
        if not member:
            print(f"⚠️ Member not found: {discord_name}")
            continue

        # ロールを検索
        role = discord.utils.get(guild.roles, name=role_name)
        if not role:
            print(f"⚠️ Role not found: {role_name}")
            continue

        try:
            await member.add_roles(role)
            print(f"✅ Added role '{role_name}' to {discord_name}")
        except Exception as e:
            print(f"❌ Failed to add role for {discord_name}: {e}")

    await client.close()

client.run(TOKEN)