from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)

hello_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Баланс", callback_data="balance"),
     InlineKeyboardButton(text="Категории", callback_data="ch_categories")],
    [InlineKeyboardButton(text="Статистика", callback_data="statistics")]
])

balance_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Указать баланс", callback_data="inp_balance")],
    [InlineKeyboardButton(text="Вернуться назад ↩️", callback_data="back")]
])

back_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Вернуться назад ↩️", callback_data="back")]
])

ch_categories_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Развлечения", callback_data="entert"),
     InlineKeyboardButton(text="Еда", callback_data="eat"),
     InlineKeyboardButton(text="Транспорт", callback_data="transport")],
    [InlineKeyboardButton(text="Ежемесячные расходы", callback_data="mont_expen"),
     InlineKeyboardButton(text="Разовые траты", callback_data="once_expence")]
])





