import schedule
import time
from content_generator import generate_post
from twitter_poster import post_to_twitter

def daily_post():
    topic = "AI in Healthcare"  # Can be dynamic
    post = generate_post(topic, "Twitter")
    post_to_twitter(post)

# Schedule daily at 9 AM
schedule.every().day.at("09:00").do(daily_post)

while True:
    schedule.run_pending()
    time.sleep(60)