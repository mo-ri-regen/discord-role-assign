# Discord Role Assigner Bot

CSV ファイルに記載されたユーザーに対して、Discord サーバー内のロールを自動で付与する Python 製 Bot です。

---

## 📦 機能

- `members.csv` に記載された「Discord 名」と「メンバー名（ロール名）」に基づいてロールを付与します。
- Bot が起動し、処理が完了すると自動でシャットダウンします。

---

## 🚀 起動方法

### 1. リポジトリをクローン

```bash
git clone https://github.com/your-username/discord-role-bot.git
cd discord-role-bot
```

### 2. 必要なライブラリをインストール

```bash
pip install -r requirements.txt
```

#### 📄 requirements.txt の内容

```text
discord.py
pandas
python-dotenv
```

---

### 3. `.env` ファイルを作成

```bash
cp .env.example .env
```

#### `.env` の内容例

```env
DISCORD_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GUILD_ID=123456789012345678
```

---

## 🔑 DISCORD_TOKEN と GUILD_ID の取得方法

### ✅ DISCORD_TOKEN の取得手順

1. [Discord Developer Portal](https://discord.com/developers/applications) にアクセス
2. 「New Application」でアプリケーションを作成
3. 左側の「Bot」タブから「Add Bot」
4. 「Token」→「Copy」でトークンをコピー（この値を `DISCORD_TOKEN` に使う）

> ⚠️ 一度公開したトークンは絶対に再利用しないこと。流出した場合は「Regenerate」で新しいトークンを発行してください。

---

### ✅ GUILD_ID（サーバー ID）の取得手順

1. Discord を開き、左下の歯車アイコン → 「詳細設定」→「開発者モード」を ON にする
2. 任意のサーバーを右クリック → 「サーバー ID をコピー」
3. その値を `GUILD_ID` に設定

---

### 4. `members.csv` を準備

#### 構造例（UTF-8）

```csv
メンバー名,Discord名
A,username1
B,username2
C,username3
```

💡 可能であれば「Discord 名」ではなく「Discord ID（数値）」の使用を推奨します。

---

## ⚙️ Bot に必要な設定

### ✅ Bot の権限（招待 URL で設定）

- Manage Roles
- View Channels
- Read Message History

> Bot の招待 URL は Discord Developer Portal の「OAuth2 → URL Generator」で scope に `bot` を選択し、上記権限を付けて生成します。

---

### ✅ Discord Developer Portal での設定

- Bot → **Privileged Gateway Intents** にて：
  - `SERVER MEMBERS INTENT` を有効にする（メンバー情報を取得するために必須）

---

### ✅ Discord サーバー内での準備

- Bot のロールを、付与したいロールより **上位に配置**
- 対象のロールは事前に作成しておく

---

## ⚠️ 注意事項

- `.env` や `members.csv` は**個人情報を含む可能性**があるため、**絶対に公開しない**
- Bot トークンが漏洩した場合は、すぐに**再生成と無効化**
- `Discord名` ベースの検索は不安定なため、可能であれば `Discord ID` に切り替える

---

## 💡 補足

- Bot は起動時に CSV ファイルを読み込み、ユーザーに順番にロールを付与します
- 付与後、自動でプロセスが終了します
- 実行結果はすべてターミナルに出力されます

---

## 📄 ライセンス

MIT
