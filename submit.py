from json import *
import datetime

file = open('data/5x5.json')
json_array = load(file)
months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]

def submit(name, time, link, moves):
	now = datetime.datetime.now()
	submission = {'name':None, 'time':None, 'date':None, 'evidence':None, 'comments':None}
	submission['name'] = name
	submission['time'] = time
	submission['date'] = f'{now.year}-{months[now.month]}-{now.day}'
	submission['date'] = f'{input("year: ")}-{input("year: ")}-{input("day: ")}'
	submission['evidence'] = link
	if (link == "none"):
		submission['evidence'] = '/'
	if (moves != "none"):
		submission['comments'] = f'{moves} moves'
	else:
		submission['comments'] = "/"

	json_array.append(submission)
	with open('data/5x5.json', 'w', encoding='utf-8') as outfile:
		dump(json_array, outfile, ensure_ascii=False, indent=2)

while True:
	submit(input('name: '), input('time: '), input('link: '), input('moves: '))
	print('-------------submitted-------------')