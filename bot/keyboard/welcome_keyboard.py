from aiogram.utils.keyboard import InlineKeyboardBuilder

def welcome():
    builder = InlineKeyboardBuilder()
    builder.button(text = 'Начать путешествие', callback_data='profile')
    return builder.as_markup()
