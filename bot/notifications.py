from aiogram import Router, types, Bot

async def send_new_ad_to_user(tg_id, bot: Bot, message, photo_url):

    await bot.send_photo(
        chat_id=tg_id,
        photo=photo_url,
        caption=message,
        parse_mode="HTML",
    )