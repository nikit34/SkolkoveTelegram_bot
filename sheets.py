# import pygsheets
# gc = pygsheets.authorize(client_secret='client_secret.json')
# sh = gc.open('SK.xlsx')
# wks = sh.sheet1
# books = wks.get_col(4)
# people = wks.get_col(10)

def history_books(update, context):
    return ['Donkifot', 'tankist, dylo and transheya', 'hastya & hatasha', 'Kamasytra']
        # return books[people.index(update['message']['chat']['username'])] # []


def current_books(update, context):
    if context.args[0] == 'return':
        pass
    return ['Donkifot', 'tankist, dylo and transheya', 'hastya & hatasha', 'Kamasytra']


def search_books(update, context):
    pass