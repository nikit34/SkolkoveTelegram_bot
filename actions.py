from screens import StartMenu, TakeBook, ListBooks, SearchBook, ShareBook, RecordBook


def start(update, context):
    if context.args and context.args[0] == 'return':
        ShareBook(update, context)
        context.bot.send_sticker(chat_id=update.effective_chat.id, sticker='CAACAgIAAxkBAAECFgNgV0B2dK7o9XsJTl--i28HBoQ3uQACsw8AAiJVuEqjk_I7TYr_aR4E')
    elif context.args and context.args[0] == 'return2':
        context.bot.send_sticker(chat_id=update.effective_chat.id,
                                 sticker='CAACAgIAAxkBAAECFgNgV0B2dK7o9XsJTl--i28HBoQ3uQACsw8AAiJVuEqjk_I7TYr_aR4E')
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



