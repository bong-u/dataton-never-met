from instaloader import Instaloader

loader = Instaloader()

NUM_POSTS = 10


def search_posts(query):
    posts = loader.get_hashtag_posts(query)
    count = 0


    for post in posts:
        print(post.profile)
        print(post.date)

        count += 1
        if count == NUM_POSTS:
            break

search_posts("족발")
