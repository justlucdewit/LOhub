from json import *
import datetime
from sys import argv
from os import system as s

if len(argv) > 1 and argv[1] == "send":
	s("git add .")
	s("git commit -m \"added more submissions\"")
	s("git push origin master")
	exit()


months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]



def submit(name, time, link, moves, date):
	now = datetime.datetime.now()
	submission = {'name':None, 'time':None, 'date':None, 'evidence':None, 'comments':None}
	submission['name'] = name
	submission['time'] = time
	submission['date'] = date#f'{now.year}-{months[now.month-1]}-{now.day}'
	#submission['date'] = f'{input("year: ")}-{input("year: ")}-{input("day: ")}'
	submission['evidence'] = link
	submission['comments'] = f'{moves}'

	json_array.append(submission)
	print("----submission----")
	print(f"name: {name}")
	print(f"event: {event}")
	print(f"time: {time}")
	with open(f'data/{event}.json', 'w', encoding='utf-8') as outfile:
		#outfile.write(str(json_array))
		dump(json_array, outfile, ensure_ascii=False, indent=2)

evnt = input("event: ")

if evnt == "3x3b5":
	event = "3x3 blind ao5"

if evnt == "4x4s":
	event = "4x4 single"
if evnt == "4x45":
	event = "4x4 ao5"
if evnt == "4x4f":
	event = "4x4 FMC"
if evnt == "4x4b":
	event = "4x4 blind"

if evnt == "5x55":
	event = "5x5 ao5"
if evnt == "5x55":
	event = "5x5 ao5"
if evnt == "5x5b":
	event = "5x5 blind"
if evnt == "5x5f":
	event = "5x5 FMC"
if evnt == "5x5s":
	event = "5x5 single"

if evnt == "6x65":
	event = "6x6 ao5"
if evnt == "6x6f":
	event = "6x6 FMC"
if evnt == "6x6s":
	event = "6x6 single"

if evnt == "7x75":
	event = "7x7 ao5"
if evnt == "7x7f":
	event = "7x7 FMC"
if evnt == "7x7s":
	event = "7x7 single"

print(f"pusing to {event}")

while True:
	#submit name event time link [moves]
	name = input("name: ")
	time = input("time: ")
	date = input("date: ").upper()
	link = input("evidence: ")
	moves = input("comments: ")

	file = open(f'data/{event}.json')

	json_array = load(file)
	submit(name, time, link, moves, date)
	print("------------------")
	print()