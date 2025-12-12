from aiogram import Router, types, Bot

# Отправка сообщения пользователю
async def send_new_ad_to_user(tg_ids, bot: Bot, message, photo_url):

    tg_id1 =tg_ids.get(1)
    tg_id2 = tg_ids.get(2)


    await bot.send_photo(
        chat_id=tg_id1,
        photo=photo_url,
        caption=message,
        parse_mode="HTML",
    )
    #await bot.send_photo(
      #  chat_id=tg_id2,
      #  photo=photo_url,
     #   caption=message,
     #   parse_mode="HTML",
#    )