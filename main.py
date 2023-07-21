import instaloader

ig = instaloader.Instaloader()
user = input("Enter the Instagram username: ")
isdp = input("Enter 1 for dp_only or 2 for all_post: ")
if isdp=="1":
    isdp=True
else:
    isdp=False
ig.download_profile(user,profile_pic_only=isdp)
# ig.download_profile(user,profile_pic_only=False)

