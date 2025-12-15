from aiogram import Router, types, Bot
from aiogram.types import FSInputFile
from bot.config import DEBUG_LOG_PATH, tg_ids


tg_id1 =tg_ids.get(1)
tg_id2 = tg_ids.get(2)

# Отправка сообщения пользователю
async def send_new_ad_to_user(bot: Bot, message, photo_url):

    await bot.send_photo(
        chat_id=tg_id1,
        photo=photo_url,
        caption=message,
        parse_mode="HTML",)
    await bot.send_photo(
        chat_id=tg_id2,
        photo=photo_url,
        caption=message,
        parse_mode="HTML",)

# Уведомления для админа. В случае ошибки, бот отправляет лог файл в телеграм админу
async def send_log_to_admin(bot: Bot):
    pass
  #  file = FSInputFile(DEBUG_LOG_PATH)

  #  await bot.send_message(chat_id=tg_id1,text='Произошла ошибка в работе бота. Отправляю лог-файл...')
   # await bot.send_document(chat_id=tg_id1,
              #              document=file,)