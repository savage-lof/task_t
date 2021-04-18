from telegram.ext import ConversationHandler

from keyboard import *
from random import *

flag = False


def remove_job_if_exists(name, context):
    """Удаляем задачу по имени.
    Возвращаем True если задача была успешно удалена."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


def task(context):
    """Выводит сообщение"""
    job = context.job
    context.bot.send_message(job.context, text='Вернулся!', reply_markup=keyboard_timer())


def unset_timer(update, context):
    global flag
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = 'Хорошо, вернулся сейчас!' if job_removed else 'Нет активного таймера.'
    update.message.reply_text('таймер сброшен', reply_markup=keyboard_timer())
    flag = False


def timer(update, context):
    update.message.reply_text('Выберите одну из четырех кнопок', reply_markup=keyboard_timer())
    return 1


def set(update, context):
    global flag
    times = {'30 секунд': 30, '1 минута': 60, '5 минут': 300}
    words = {'30 секунд': '30 секунд', '1 минута': '1 минуту', '5 минут': '5 минут'}
    due = times[update.message.text]

    chat_id = update.message.chat_id
    try:
        job_removed = remove_job_if_exists(
            str(chat_id), 
            context
        )
        print(job_removed)
        context.job_queue.run_once(
            task,
            due,
            context=chat_id,
            name=str(chat_id)
        )
        text = f'засек {words[update.message.text]}'
        if job_removed:
            text += ' Старая задача удалена.'
        # Присылаем сообщение о том, что всё получилось.
        update.message.reply_text(text, reply_markup=keyboard_close())
        print(flag)
        flag = True

    except (IndexError, ValueError):
        update.message.reply_text('Использование: /set <секунд>')


def start(update, context):
    print(4)
    update.message.reply_text('Выберите одну из двух кнопок', reply_markup=keyboard_start())


def dice(update, context):
    update.message.reply_text('Выберите одну из четырех кнопок', reply_markup=keyboard_dice())
    return 1


def cube(update, context):
    print(6)
    print(update.message.text)
    if update.message.text == 'кинуть один шестигранный кубик':
        number = [randint(1, 6)]
    elif update.message.text == 'кинуть 2 шестигранных кубика одновременно':
        number = [randint(1, 6), randint(1, 6)]
    elif update.message.text == 'кинуть 20-гранный кубик':
        number = [randint(1, 20)]
    line = ', '.join(map(str, number))
    update.message.reply_text(line)


def start_2(update, context):
    if flag:
        unset_timer(update, context)
    update.message.reply_text('Выберите одну из двух кнопок', reply_markup=keyboard_start())
    return ConversationHandler.END

    
        
    