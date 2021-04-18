from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from handler import *

TOKEN='1754107976:AAG-gky1bgfhBYaNxj1WV0kyzDmrGp1nudw'


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("timer", set_timer))

    dp.add_handler(CommandHandler("close", unset_timer, 
                                  pass_chat_data=True))
    print(1)
    dp.add_handler(CommandHandler('start', start))
    print(2)
    dp.add_handler(ConversationHandler(
    entry_points=[CommandHandler('dice', dice)],
    states={
        1: [MessageHandler(Filters.text(['кинуть один шестигранный кубик', 'кинуть 2 шестигранных кубика одновременно',
                                        'кинуть 20-гранный кубик']), cube)]
    },
    fallbacks=[MessageHandler(Filters.text('вернуться назад'), start)]))

    print(3)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


