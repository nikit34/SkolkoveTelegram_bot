from screens import StartMenu, TakeBook, ListBooks, SearchBook, ShareBook, RecordBook


def start(update, context):
    if context.args and context.args[0] == 'return':
        context.bot.send_message(chat_id=update.effective_chat.id, text='return')
    else:
        StartMenu(update)


def buttons(update, context):
    query = update.callback_query
    query.answer()
    if query.data == 'take_book':
        TakeBook(update, context)
    elif query.data.startswith('record_book'):
        context.bot.send_message(
            chat_id='https://t.me/joinchat/pI3uWSfsbPZjY2Qy', # TODO testing
            text=f'{update.message.chat.username} взял почитать книгу {context.chat_data["book"]}'
        )
        # change table (nik, data)
        pass
        RecordBook(update, context)
    elif query.data == 'list_book':
        ListBooks(update, context)
        StartMenu(update)
    elif query.data == 'share_book':
        ShareBook(update, context)


def input_text(update, context):
    if context.chat_data['screen'] == 'SearchBook':
        SearchBook(update, context)
    else:
        pass



