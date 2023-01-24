# Instagram-Video-Downloader.py
Download all posted videos

1.from instaloader import Instaloader, Profile: This imports the Instaloader and Profile classes from the instaloader library.
2.L = Instaloader(): This creates an instance of the Instaloader class and assigns it to the variable L.
3.PROFILE = input("username: "): This prompts the user to input a username and assigns the input to the variable PROFILE.
4.profile = Profile.from_username(L.context, PROFILE): This creates an instance of the Profile class for the specified username and assigns it to the variable profile.
5.L.download_tagged(profile, fast_update=False): This function downloads all posts in which the specified profile is tagged.
6.tagged_post = sorted(profile.get_tagged_posts(), key=lambda post: post.likes,reverse=True): This gets all the tagged posts from the profile and sorts them by number of likes in descending order.
7.for post in tagged_post:: This starts a loop to iterate through each post in the tagged_post list.
8.L.download_post(post, PROFILE): This downloads the current post in the loop. The second parameter is the subfolder name, where it will be saved.
