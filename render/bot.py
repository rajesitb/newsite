import os
bearer_token = os.env.get(bearer_token)
apikey = os.env.get(apikey)
api_secret = os.env.get(api_secret)
access_token = os.env.get(access_token)
access_token_secret = os.env.get(access_token_secret)

client = tweepy.Client(bearer_token=bearer_token, consumer_key=apikey, consumer_secret=api_secret, access_token=access_token,
              access_token_secret=access_token_secret, wait_on_rate_limit=True)
ncc_id = '1359135143185711107'

followers = client.get_users_following(ncc_id)
followers_dict = {item.id: item.name for item in followers.data}
followers_json = json.dumps(followers_dict, indent=4)
with open('follower.json', 'w') as file:
    file.write(followers_json)
