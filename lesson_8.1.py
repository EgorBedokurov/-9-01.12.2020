import requests
import json
import datetime

URL = 'https://api.exchangerate.host/convert/from=USD&to=UAH&amount=10000.5&date=2020-09-18'
path = 'symbols.json'

def currency_intput():
    cur_from = 'USD'
    cur_to = 'UA'
    cur_amount = 100
    cur_date = datetime.datetime.now() - datetime.timedelta(days=4)
    data_cur = {'from': cur_from, 'to': cur_to, 'amount': cur_amount, 'date': cur_date,
                }
    print(data_cur)
    r = requests.get(URL, data_cur)
    print(r.json())

currency_intput()

# result = currency_intput()
#
# cur_date = datetime.datetime.now() - datetime.timedelta(days=4)
#
# with open('course_list', 'w') as f:
#     f.writelines([' date', ' from', ' to', ' rate', ' result', '\n'])
#     while cur_date <= datetime.datetime.now():
#         cur_date += datetime.timedelta(days=1)
#         f.writelines([str(['date']) + (' '*2),
#                         ['from'] + (' '*2),
#                         ['to']+ (' '*2),
#                         ['rate'] + (' '*2),
#                         ['result'] + (' '*2),
#                         '\n'])





