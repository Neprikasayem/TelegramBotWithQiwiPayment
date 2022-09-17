from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btnTopup = InlineKeyboardButton(text="Пополнить", callback_data="top_up")
topUpMenu = InlineKeyboardMarkup(row_width=1)
topUpMenu.insert(btnTopup)

def buy_menu(isUrl=True, url="", bill=""):
    qiwiMenu = InlineKeyboardMarkup(row_width=1)
    if isUrl:
        btnUrlQIWI = InlineKeyboardButton(text="Ссылка на оплату", url=url)
        qiwiMenu.insert(btnUrlQIWI)

    btnCheckQIWI = InlineKeyboardButton(text="Проверить оплату", callback_data="check_"+bill)
    qiwiMenu.insert(btnCheckQIWI)
    return qiwiMenu