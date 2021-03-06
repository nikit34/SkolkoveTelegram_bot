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
        num=nums.index('') + 1
        wks.update_row(num, [num, context.chat_data.get('user'), context.chat_data['book'], str(date.today()), 0])
        sh = gc.open('all_books')
        wks_all = sh.worksheet('title', 'Лист1')
        books = wks_all.get_col(4)
        try:
            num_all = books.index(context.chat_data['book']) + 1
        except:
            wks_all = sh.worksheet('title', 'Лист2')
            books = wks_all.get_col(4)
            num_all = books.index(context.chat_data['book']) + 1
        if wks_all.cell((num_all, 10)).value != '':
            wks.cell((num, 7)).set_value(context.chat_data.get('user'))
        wks_all.cell((num_all, 10)).set_value(context.chat_data.get('user'))
        wks_all.cell((num_all, 6)).set_value(str(date.today()))
    elif act == 'return':
        u = context.chat_data.get('user')
        b = context.chat_data['book']
        bks = wks.get_col(3); usrs = wks.get_col(2)
        for i in range(len(bks)):
            if bks[i] == b and usrs[i] == u:
                num = i

                wks.cell((num, 5)).set_value(str(date.today()))
        sh = gc.open('all_books')
        wks_all = sh.sheet1
        books = wks_all.get_col(4)
        try:
            num_all = books.index(context.chat_data['book']) + 1
            wks_all.cell((num_all, 7)).set_value(str(date.today()))
            p = 1
        except:
            wks_all_2 = sh.worksheet('title', 'Лист2')
            books_2 = wks_all_2.get_col(4)

            num_all = books_2.index(context.chat_data['book']) + 1
            wks_all_2.cell((num_all, 7)).set_value(str(date.today()))
            wks_all.update_row(books.index('')+1, wks_all_2.get_row(num_all))
            wks_all_2.delete_rows(num_all)
            wks.cell((num, 8)).set_value(1)
            p = 2
        wks.cell((num, 8)).set_value( p)
    elif act == 'return2':
        u = context.chat_data.get("user")
        b = context.chat_data['book']
        bks = wks.get_col(3);
        usrs = wks.get_col(2)
        for i in range(len(bks)):
            if bks[i] == b and usrs[i] == u:
                num = i

        wks.cell((num, 5)).set_value(str(date.today()))
        sh = gc.open('all_books')
        wks_all = sh.worksheet('title', 'Лист2')
        books = wks_all.get_col(4)
        try:
            num_all = books.index(context.chat_data['book']) + 1
            wks_all.cell((num_all, 7)).set_value(str(date.today()))
        except:
            wks_all_2 = sh.sheet1
            books_2 = wks_all_2.get_col(4)

            num_all = books_2.index(context.chat_data['book']) + 1
            wks_all_2.cell((num_all, 7)).set_value(str(date.today()))
            wks_all.update_row(books.index('')+1, wks_all_2.get_row(num_all))
            wks_all_2.delete_rows(num_all)
            wks.cell((num, 8)).set_value(1)


def current_books(update, context):
    gc = pygsheets.authorize()
    sh = gc.open('all_books')
    sh1 = gc.open('books_history')
    w = sh1.sheet1
    u = context.chat_data.get('user')
    nik = w.get_col(2)[::-1]; dates_return = w.get_col(5)[::-1]
    books = w.get_col(3)[::-1]
    books_taken = []
    for i in range(len(nik)):
        if nik[i] == u and dates_return[i] == '0':
            books_taken.append(books[i])
    return books_taken

def search_books(update, context):
    def process(wks):
        books = wks.get_col(4)
        the_book = context.chat_data['book'].lower()
        results = []
        for b in books:
            if the_book in b.lower():
                results.append(b)
        return results
    gc = pygsheets.authorize()
    sh = gc.open('all_books')
    wks = sh.sheet1
    results = process(wks)
    if len(results) == 0:
        wks = sh.worksheet('title', 'Лист2')
        results = process(wks)
    return results
