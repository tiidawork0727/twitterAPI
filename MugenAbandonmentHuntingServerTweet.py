import tweepy

# Twitter APIキーとアクセストークンを設定
local_api_key = ''
local_api_secret = ''
local_access_token = ''
local_access_token_secret = ''

# ツイートする内容
tweet_text = "ムゲン放置狩りサーバーまだまだメンバー募集中です！\r\n以下リンクでサーバーに参加出来ますので、興味ある方は参加お願いします～\r\nhttps://discord.gg/ab7vVRwJ3K\r\n#グラブル\r\n#ムゲン放置刈り"

#グラブル 
#ムゲン放置狩り"

# ツイートする関数
def tweet():
    # TwitterAPIに接続
    auth = tweepy.OAuthHandler(local_api_key, local_api_secret)
    auth.set_access_token(local_access_token, local_access_token_secret)
    api = tweepy.API(auth)
    
    # オブジェクト設定
    client = tweepy.Client(consumer_key=local_api_key, consumer_secret=local_api_secret, access_token=local_access_token, access_token_secret=local_access_token_secret) 

    # ツイートを投稿
    client.create_tweet(text=tweet_text) 
    return "Tweet posted: " + tweet_text

# ツイートの送信
tweet_text = tweet()
print("Tweet sent:", tweet_text)