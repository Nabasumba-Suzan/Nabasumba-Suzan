import tweepy
import os

def post_to_twitter(text: str, image_path=None):
    # Get credentials from environment variables (recommended)
    API_KEY = os.getenv('TWITTER_API_KEY')
    API_SECRET = os.getenv('TWITTER_API_SECRET')
    ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
    ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')

    if not all([API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET]):
        print("Error: Twitter API credentials not set!")
        return False

    try:
        # Authenticate
        auth = tweepy.OAuth1UserHandler(
            API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET
        )
        api = tweepy.API(auth)

        # Post with/without media
        if image_path:
            api.update_status_with_media(text, image_path)
            print(f"Posted with image: {text[:50]}...")
        else:
            api.update_status(text)
            print(f"Posted: {text[:50]}...")
        return True
        
    except Exception as e:
        print(f"Twitter posting failed: {str(e)}")
        return False

# Test function
if __name__ == "__main__":
    print("--- Testing Twitter Poster ---")
    test_post = "Hello Twitter from my AI agent! #Python #Automation"
    success = post_to_twitter(test_post)
    print("Success!" if success else "Failed!")