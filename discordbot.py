# インストールした discord.py を読み込む
import discord
import os

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'DISCORD_BOT_TOKEN'
# 接続に必要なオブジェクトを生成
client = discord.Client()
CID = 725325208537530370
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    #条件に当てはまるメッセージかチェックし正しい場合は返す
    def check(msg):
        return msg.author == message.author
    
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
