from pyrogram import Client

# Your Telegram API credentials and session string
api_id = 23212132
api_hash = "1c17efa86bdef8f806ed70e81b473c20"
session_string = "BQFiMGQAhf4JrlOx0d230td4NFd5nlerbkQkVEMJIpYR974l2sOL8883iFRY_ijV_taYcsF9D_y6GdxpFad90Wo6QjUPuqMfVvlvS3nckX_mwz0LtJ2hK2i1yAabE4WOD9QnFiT4hp4NfhqQrxpX4zlEziRdBwWft"

app = Client("fetch_telegram_code", api_id=api_id, api_hash=api_hash, session_string=session_string)

async def main():
    async with app:
        try:
            # Get the latest message from Telegram official account
            tg_messages = await app.get_chat_history("Telegram", limit=1)
            if tg_messages:
                last_msg = tg_messages[0].text
                print("📩 Last message from @Telegram:")
                print(last_msg)

                # Send it to your own Saved Messages
                await app.send_message("me", f"🔐 Code from @Telegram:\n\n{last_msg}")
            else:
                print("❌ No messages found from @Telegram.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

app.run(main())
