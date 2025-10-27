from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.text import LOCATION

def profile():
    builder = InlineKeyboardBuilder()
    builder.button(text = '🗺️ Перейти к Маршруту', callback_data='point:next:0')
    builder.button(text='📚 О Маршруте', callback_data='start_path')
    builder.adjust(1)
    return builder.as_markup()

def point(numer_point: int, visited_place: list):
    builder = InlineKeyboardBuilder()
    if numer_point > 1:
        builder.button(text='⬇️ Назад', callback_data=f'point:previous:{numer_point}')
    if numer_point < 10:
        builder.button(text='⬆️ Вперед', callback_data=f'point:next:{numer_point}')
    if numer_point not in visited_place:
        builder.button(text='✅ Я здесь был!', callback_data=f'complete_point:{numer_point}')
    builder.button(text='📍 Открыть в Яндекс.Картах', url=LOCATION[numer_point])
    builder.button(text='▶ Слушать гид по локации', callback_data=f'audio_guide:{numer_point}')
    if numer_point == 1 or numer_point == 10:
        builder.adjust(1)
    else:
        builder.adjust(2, 1, 1)
    return builder.as_markup()

def back():
    builder = InlineKeyboardBuilder()
    builder.button(text = 'Назад', callback_data='profile')
    return builder.as_markup()