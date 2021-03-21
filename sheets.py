import pygsheets
from datetime import date


def history_books(update, context, act):
    def search_empty(wks):
        i = 1
        while wks.cell((i, 1)) != '':
            i += 1
        return i
    def search_book(wks):
        i = 1
        while wks.cell((i, 3)) != context.chat_data['book']:
            i += 1
        return i
    gc = pygsheets.authorize()
    sh = gc.open('books_history')
    wks = sh.sheet1
    if act == 'take':
        num = search_empty(wks)
        wks.update_row(num, [update['message']['chat']['username'], context.chat_data['book'], str(date.today)], 0)
        sh = gc.open('all_books')
        wks = sh.sheet1
        books = wks.get_col(4)
        #book = books[]
    elif act == 'return':
        num = search_book(wks)
        wks.update_cells((num, 5), str(date.today))
        # return books[people.index(update['message']['chat']['username'])] # []


def current_books(update, context):
    if context.args[0] == 'return':
        gc = pygsheets.authorize()
        sh = gc.open('all_books')
        wks = sh.sheet1
        books = wks.get_col(4)
        people = wks.get_col(10)
        return books[people.index(update['message']['chat']['username'])]

def search_books(update, context):
    gc = pygsheets.authorize()
    sh = gc.open('all_books')
    wks = sh.sheet1
    books = wks.get_col(4)
    the_book = context.chat_data['book'].lower()
    results = []
    for b in books:
        if the_book in b.lower():
            results.append(b)
    return results
