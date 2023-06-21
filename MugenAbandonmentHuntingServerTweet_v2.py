import requests

# Twitter APIエンドポイントとパラメータを設定
url = "https://api.twitter.com/1.1/statuses/update.json"

# リクエストヘッダーにBearerトークンを設定
headers = {
    "Authorization": "AAAAAAAAAAAAAAAAAAAAAAAv%2FoAEAAAAAat9Pvv1CrzIth2uJEetDiGLHtKo%3D7LpNqp4grFIPuiQ6BZYNY3LBKpsj22aBcFFuaMjRI5Jx3jgAEw",
    "Content-Type": "application/json"
}

# ツイートを作成
tweet_text = "ムゲン放置狩りサーバーを立ててみました！\r\n以下リンクでサーバーに参加出来ますので、興味ある方は参加お願いします～\r\nhttps://discord.gg/ab7vVRwJ3K"
data = {
    "status": tweet_text
}

# リクエストを送信
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Tweet sent successfully!")
else:
    print("Failed to send tweet.")
    print(response.text)
