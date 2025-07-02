import tweepy

def post_to_twitter(text: str, image_path=None):
    auth = tweepy.OAuth1UserHandler(
        "API_KEY", "API_SECRET", "ACCESS_TOKEN", "ACCESS_SECRET"
    )
    api = tweepy.API(auth)
    if image_path:
        api.update_status_with_media(text, image_path)
    else:
        api.update_status(text)