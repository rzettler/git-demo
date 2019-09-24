#Use text editor to edit the script and type in valid Instagram username/password
from InstagramAPI import InstagramAPI
api = InstagramAPI("allgaeu.joe", "mkf100bg")
api.login() # login
"""
api.getSelfUserFollowers()
"""
#api.getUserFollowers(media_id["ranked_items"][0]["user"]["pk"]) # get first media owner followers# #
"""
print(api.LastJson.get('users', []))
"""
#instagram id of the user you want to get the followings of
user_id = '8531802448'
#GET FOLLOWERS
followers = []
next_max_id = True
while next_max_id:
  # first iteration hack
  if next_max_id is True:
    next_max_id = ''
    _ = api.getUserFollowers(user_id, maxid=next_max_id)
    followers.extend(api.LastJson.get('users', []))
    next_max_id = api.LastJson.get('next_max_id', '')

unique_followers = {
f['username']: f
# username vs pk (for id)
for f in followers
}
#Output all the IDs
for f in unique_followers:
  print(str(f))