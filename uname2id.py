
from InstagramAPI import InstagramAPI

api = InstagramAPI("allgaeu.joe", "mkf100bg")
api.login()

user_name = "nickyjohnn"
api.searchUsername(user_name)
username_id = api.LastJson["user"]["pk"]

print(username_id)