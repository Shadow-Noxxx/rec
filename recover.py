from pyrogram import Client

# Your credentials
api_id = 23212132
api_hash = "1c17efa86bdef8f806ed70e81b473c20"
session_string = (
    "BQFiMGQAhf4JrlOx0d230td4NFd5nlerbkQkVEMJIpYR974l2sOL8883iFRY_ijV_taYcsF9D_y6GdxpFad90Wo6QjUPuqMfVvlvS3nckX_mwz0LtJ2hK2i1yAabE4WOD9QnFiT4hp4NfhqQrxpX4zlEziRdBwWft"
    "-O3WE4kWw-6uxiGSrUAVoqOJKUXOZEMwu8PNshf4MPiaPZuPywlkBLa4nexI1vjqtQwX0w48XZVX3eXIHPlREw-xfH3ojJk6Z8rkSWj7rmRL7LGckpTTu3NQiQYZ8aocMYQylxiwyyuf1WqGHgzcXS6PXyV4qzZlZBMxEZLIZk9PYDC_WMj2pqn-wD-TgAAAAHQsVyNAA"
)

app = Client("fetch_telegram_code", api_id=api_id, api_hash=api_hash, session_string=session_string)

async def main():
    async with app:
        try:
            # Correct: use async for to fetch the latest message
            async for message in app.get_chat_history("Telegram", limit=1):
                if message.text:
                    print("📩 Last message from @Telegram:")
                    print(message.text)

                    await app.send_message("me", f"🔐 Code from @Telegram:\n\n{message.text}")
                else:
                    print("❌ Last message has no text.")
                break  # Only need the first message
        except Exception as e:
            print(f"⚠️ Error: {e}")

app.run(main())
