from instaloader import Instaloader, Profile

# L = Instaloader()
# PROFILE = input('username: ')
# profile = Profile.from_username(L.context, PROFILE)

# posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes,reverse=True)

# for post in posts_sorted_by_likes:
#     L.download_post(post, PROFILE)

#loader = Instaloader()
#loader.load_session_from_file(input('username: '))           #to download last 20 pics that the user liked
#loader.download_feed_posts(max_count=20, fast_update=True,      
                           #post_filter=lambda post: post.viewer_has_liked)


#loader = Instaloader()                          # to download 30 pics from the specific location
#loader.download_location(362629379, max_count=30)


#loader = Instaloader()                          # to download 30 pics with hashtags
#loader.download_hashtag('cat', max_count=30)

L = Instaloader()
PROFILE = input("username: ")
profile = Profile.from_username(L.context, PROFILE)
L.download_tagged(profile, fast_update=False)
tagged_post = sorted(profile.get_tagged_posts(), key=lambda post: post.likes,reverse=True)
for post in tagged_post:
    L.download_post(post, PROFILE)