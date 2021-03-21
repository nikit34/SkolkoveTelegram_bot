from screens import StartMenu, TakeBook, ListBooks, SearchBook, ShareBook, RecordBook, ReturnBook


def start(update, context):
    if context.args and context.args[0] == 'return':
        context.bot.send_message(chat_id=update.effective_chat.id, text='return')
    else:
        context.chat_data['reply'] = False
        context.chat_data["user"] = update.message.chat.username
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
    elif query.data == 'return_book':
        ReturnBook(update, context)
    elif query.data == 'start_menu':
        context.chat_data['reply'] = True
        StartMenu(update, context)


def input_text(update, context):
    if context.chat_data['screen'] == 'SearchBook':
        SearchBook(update, context)
    elif context.chat_data['screen'] == 'TakeBook':
        TakeBook(update, context)



