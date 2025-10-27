from config import dp
from bot.keyboard import private_keyboard
from aiogram.types import FSInputFile
from bot.text import PROFILE_TEXT, POINTS_TEXT, JORNEY_TEXT
from bot.database.func_db import select_user, update_user
from aiogram.filters import Command

async def send_profile(message_or_cq_message, user_info, username):
    try:
        await message_or_cq_message.answer(
            text=PROFILE_TEXT.format(
                username=username,
                count_point=len(user_info.places_visited),
                time_register=user_info.time_register,
            ),
            reply_markup=private_keyboard.profile()
        )
    except Exception as e:
        await message_or_cq_message.answer(f"Unknown error {e}")

@dp.message(Command('menu'))
async def start(message):
    user_id = message.from_user.id
    user_info = await select_user(user_id)
    await send_profile(message, user_info, message.from_user.username)
@dp.callback_query()
async def handlers(data):

    info = data.data
    user_id = data.from_user.id
    user_info = await select_user(user_id)

    if info == 'profile':
        await data.message.delete()
        await send_profile(data.message, user_info, data.from_user.username)
        await data.answer()
    elif info == 'start_path':
        await data.message.edit_text(text=JORNEY_TEXT, reply_markup=private_keyboard.back(), parse_mode='HTML')
        await data.answer()
    elif info.startswith("point"):
        _ , when_to, numer_point = info.split(":")
        numer_point = int(numer_point)
        if when_to == 'next':
            numer_point += 1
        else:
            numer_point -= 1
        await data.message.delete()
        await data.message.answer_photo(
            photo=FSInputFile(f'photos/place_{numer_point}.jpg'),
            caption=f"{POINTS_TEXT[numer_point]['title']}\n{POINTS_TEXT[numer_point]['description']}{"\n✅ Ты уже посетил эту точку" if numer_point in user_info.places_visited else ""}",
            reply_markup=private_keyboard.point(numer_point, user_info.places_visited),
            parse_mode="HTML"
        )
        await data.answer()

    elif info.startswith("audio_guide"):
        _ , numer_point = info.split(":")
        numer_point = int(numer_point)

        await data.message.answer_audio(
            audio=FSInputFile(f"audio/audio_{numer_point}.mp3"),
            title=f"Точка {numer_point}",
            performer="Аудиогид",
            caption=POINTS_TEXT[numer_point]['title'],
            parse_mode="HTML"
        )
        await data.answer()

    elif info.startswith("complete_point"):
        _, numer_point = info.split(":")
        numer_point = int(numer_point)


        old_list_visited = user_info.places_visited
        if numer_point not in old_list_visited:
            old_list_visited.append(numer_point)
        else:
            await data.answer("Error: btn already clicked")
            return#может уйти в беск длины массив если пользак ахуеет

        await data.answer("🌟 Екатеринбург умеет удивлять, правда? 😉")
        await data.message.edit_reply_markup(reply_markup=private_keyboard.point(numer_point, old_list_visited))
        await update_user(
            user_id=user_id,
            column="places_visited",
            value=old_list_visited
        )

