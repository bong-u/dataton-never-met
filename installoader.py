from instaloader import Instaloader

loader = Instaloader()

NUM_POSTS = 10
count = 0

def search_posts(query):
    posts = loader.get_hashtag_posts(query)


    for post in posts:
        print(post.profile)
        print(post.date)

        if count == NUM_POSTS:
            break

search_posts("족발")
