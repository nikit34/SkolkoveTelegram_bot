from screens import StartMenu, TakeBook, ListBooks, SearchBook, ShareBook, RecordBook


def start(update, context):
    if context.args and context.args[0] == 'return':
        context.bot.send_message(chat_id=update.effective_chat.id, text='return')
    else:

        StartMenu(update, context)


def buttons(update, context):
    query = update.callback_query
    query.answer()
    if query.data == 'take_book':
        TakeBook(update, context)
    elif query.data.startswith('record_book'):
        name_book = context.chat_data['list_book'][int(query.data[12:])]
        context.chat_data['book'] = name_book
        # change table (nik, data)
        pass
        RecordBook(update, context)
    elif query.data == 'list_book':
        ListBooks(update, context)
        StartMenu(update, context)
    elif query.data == 'share_book':
        ShareBook(update, context)


def input_text(update, context):
    if context.chat_data['screen'] == 'SearchBook':
        SearchBook(update, context)
    elif context.chat_data['screen'] == 'TakeBook':
        TakeBook(update, context)
    else:
        pass



