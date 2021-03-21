from screens import StartMenu, TakeBook, ListBooks, SearchBook, ShareBook, RecordBook, ReturnBook, InfoBook, HistoryBook


def start(update, context):
    context.chat_data["user"] = update.message.chat.username
    if context.args and context.args[0] == 'return':
        ReturnBook(update, context)
    else:
        context.chat_data['reply'] = False
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
        RecordBook(update, context)
    elif query.data == 'list_book':
        ListBooks(update, context)
    elif query.data == 'share_book':
        ShareBook(update, context)
    elif query.data == 'info_book':
        InfoBook(update, context)
    elif query.data.startswith('return_book'):
        name_book = context.chat_data['list_book'][int(query.data[12:])]
        context.chat_data['book'] = name_book
        HistoryBook(update, context)
    elif query.data == 'start_menu':
        context.chat_data['reply'] = True
        StartMenu(update, context)


def input_text(update, context):
    if context.chat_data['screen'] == 'SearchBook':
        SearchBook(update, context)
    elif context.chat_data['screen'] == 'TakeBook':
        TakeBook(update, context)
    else:
        pass



