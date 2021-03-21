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
        nums = wks.get_col(2)
        num=nums.index('')+1
        print(num)
        print(update.message)
        wks.update_row(num, [num, context.chat_data['user'], context.chat_data['book'], str(date.today()), 0])
        sh = gc.open('all_books')
        wks = sh.sheet1
        books = wks.get_col(4)
        num = books.index(context.chat_data['book'])+1
        wks.cell((num, 10)).set_value(context.chat_data['user'])
        wks.cell((num, 6)).set_value(str(date.today()))
    elif act == 'return':
        num = search_book(wks)
        wks.update_cells((num, 5), str(date.today))
        # return books[people.index(update['message']['chat']['username'])] # []


def current_books(update, context):
    gc = pygsheets.authorize()
    sh = gc.open('all_books')
    wks = sh.sheet1
    books = wks.get_col(4)
    people = wks.get_col(10)
    u = context.chat_data['user']
    books_taken = []
    for i, p in enumerate(people):
        if p == u:
            books_taken.append(books[i])
    return books_taken

def search_books(update, context):
    gc = pygsheets.authorize()
    sh = gc.open('all_books')
    wks = sh.sheet1
    books = wks.get_col(4)
    the_book = str(context.chat_data['book'])
    results = []
    for b in books:
        if the_book in b:
            results.append(b)
    return results
