from datetime import date
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from sheets import history_books, current_books, search_books


def StartMenu(update):
    keyboard = [
        [InlineKeyboardButton('Взять', callback_data='take_book')],
        [InlineKeyboardButton('Мои книги', callback_data='list_book')],
        [InlineKeyboardButton('Поделиться', callback_data='share_book')],
    ]
    update.message.reply_text('Привет! Добро пожаловать в X-Booking! 🌟', reply_markup=InlineKeyboardMarkup(keyboard))


def TakeBook(update, context):
    keyboard = [
        [InlineKeyboardButton('Взять еще', callback_data='take_book')],
    ]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Введи название / автора',
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    context.chat_data['screen'] = 'SearchBook'


def ListBooks(update, context):
    list_books = current_books(update, context)
    keyboard = []

    for i, name_book in enumerate(list_books):
        row_str = str(i + 1) + '. ' + name_book
        row_book = [InlineKeyboardButton(row_str, callback_data='take_book')]
        keyboard.append(row_book)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Книжки, которые ты взял почитать:',
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Спасибо, что пользуешься нашим сервисом, \n \
             надеемся книжки, которыми мы делимся \n \
             помогают тебе в достижении твоих целей! \n \
             Не забудь вовремя вернуть, участники нашего комьюнити, \n \
             возможно, хотят почитать эти книжки тоже \U000026C4',
    )


def SearchBook(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    results = []  # search_books(update.message.text)
    if len(results) == 0:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Упс! Не получилось найти такую книгу 🙄 \n \
                 Попробуйте еще раз или напишите в личку нашему менеджеру @профиль_менеджера. \n \
                 Вы можете нажать на кнопку ниже, наши менеджеры увидят, какую книжку вы взяли 🙂'
        )
        context.chat_data['screen'] = 'SearchBook'
    elif len(results) > 5:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Мы нашли много схожих вариантов 🙄 \n \
                 Пожалуйста, введи название полностью 🙌🏼'
        )
        context.chat_data['screen'] = 'SearchBook'
    elif len(results) > 1 and len(results) <= 5:
        keyboard = []
        for i, result in enumerate(results):
            keyboard.append([InlineKeyboardButton(f'{result[i]} Забрать', callback_data=f'record_book_{i}')])
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Похоже, ты выбрал одну из этих книг👇🏼 \n \
                 Нажми на ту, которую ты выбрал и забирай читать!',
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif len(results) == 1:
        keyboard = [[InlineKeyboardButton(f'{results[0]} Забрать', callback_data='record_book')]]
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Похоже, ты выбрал эту книжку 👇🏼 \n \
                 Нажми на нее и забирай читать!',
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        context.chat_data['book'] = results[0]


def ShareBook(update, context):
    pass


def RecordBook(update, context):
    keyboard = [
        [InlineKeyboardButton('Взять еще', callback_data='take_book')],
    ]
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Спасибо! Мы записали книжку, которую вы взяли почитать. \n \
            Пожалуйста, постарайтесь вернуть ее в течении 4-х недель 🙌🏼 \n \
            Мы напомним об этом через 3 недели. Если не успеете вернуть, можно \n \
            будет отложить дату возврата на пару недель 😉 \n \
            Не забывайте, что многие тоже хотят прочитать эту книжку! 🙂',
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    context.chat_data['screen'] = 'TakeBook'

    date_take = date
    while time_take - datetime.now() > now.strftime




