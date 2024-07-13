from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


welcome_panel = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='Log in', callback_data='login')],
        ],
        resize_keyboard=True
        )

main_panel = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Login again', callback_data='login')],
        [InlineKeyboardButton(text='Post now', callback_data='post now'),
        InlineKeyboardButton(text='Start posting', callback_data='start posting')],
        [InlineKeyboardButton(text='Stop posting', callback_data='stop posting')],
    ],
    resize_keyboard=True,
    input_field_placeholder='Choose option'
    )