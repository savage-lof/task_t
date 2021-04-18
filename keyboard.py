from telegram import ReplyKeyboardMarkup


def keyboard_start():
    reply_keyboard = [['/dice', '/timer']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    return markup


def keyboard_dice():
    reply_keyboard_dice = [['кинуть один шестигранный кубик', 'кинуть 2 шестигранных кубика одновременно'],
    ['кинуть 20-гранный кубик', 'вернуться назад']]
    markup_dice = ReplyKeyboardMarkup(reply_keyboard_dice, one_time_keyboard=False, resize_keyboard=True)
    return markup_dice


def keyboard_timer():
    reply_keyboard_timer = [['30 секунд', '1 минута'],
    ['5 минут', 'вернуться назад']]
    markup_timer = ReplyKeyboardMarkup(reply_keyboard_timer, one_time_keyboard=False, resize_keyboard=True)
    return markup_timer

def keyboard_close():
    reply_keyboard_close = [['/close', 'вернуться назад']]
    markup_close = ReplyKeyboardMarkup(reply_keyboard_close, one_time_keyboard=False, resize_keyboard=True)
    return markup_close
