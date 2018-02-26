import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "h1ta38teiZMGQ77SKZlRoC99C",
    "consumer_secret"     : "ScMnqDCNREkbNeZrawDkVnf0eWAkmtgqnwEVCXUPkAlHA3BHF5",
    "access_token"        : "966151275615260677-Na5X2WZjVhtCHjbviMVKwE9ysJdQA1d",
    "access_token_secret" : "v54jX8LXyoxORFSS1N1aRL4U1ohWk7yvzU3JTzH7J3cl6"
    }

  api = get_api(cfg)
  tweet = "hey guys"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
