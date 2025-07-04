import asyncio
from telegram import Bot
from telegram.constants import ParseMode
import telegram.error
import time

# Use environment variables or a secure vault for real deployment
BOT_TOKEN = "8105144524:AAG3Fguk29tG5VifIrXVSHrRI9yhFpN6ejo"
CHAT_ID = "-1002752208616"  # Can be a user ID, group ID, or @channelusername
INTERVAL_MINUTES = 30  # Message interval in minutes

async def post_to_telegram(text_content):
    """
    Sends a text message to a specified Telegram chat or channel.

    Args:
        text_content (str): The message to send.
    """
    if not text_content:
        print("Error: Text content cannot be empty.")
        return

    print("Attempting to post to Telegram...")

    try:
        # Create bot instance
        bot = Bot(token=BOT_TOKEN)

        # Send the message (must be awaited)
        await bot.send_message(
            chat_id=CHAT_ID,
            text=text_content,
            parse_mode=ParseMode.MARKDOWN
        )

        print("✅ Successfully posted to Telegram!")

    except telegram.error.TelegramError as e:
        print(f"❌ Telegram API error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

async def scheduled_posting():
    """Main scheduling loop that runs indefinitely"""
    while True:
        # Define your post content
        my_post = "Hello from my Python bot! 🤖\n\nThis is your scheduled message every 30 minutes."
        
        # Post the message
        await post_to_telegram(my_post)
        
        # Wait for the specified interval before posting again
        print(f"⏳ Waiting for {INTERVAL_MINUTES} minutes before next post...")
        await asyncio.sleep(INTERVAL_MINUTES * 60)

if __name__ == "__main__":
    # Run the scheduled posting
    asyncio.run(scheduled_posting())