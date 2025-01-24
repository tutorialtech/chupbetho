from pyrogram import filters
from pyrogram.types import Message

from VIKRANT import app
from VIKRANT.core.call import vikrant

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await vikrant.stop_stream_force(message.chat.id)
