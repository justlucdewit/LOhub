from json import *
import datetime
from sys import argv
from os import system as s

if len(argv) > 1 and argv[1] == "send":
	s("git add .")
	s("git commit -m \"added more submissions\"")
	s("git push origin master")
	exit()

#submit name event time link [moves]
name = input("name: ")
time = input("time: ")
date = input("date: ")
link = input("evidence: ")
moves = input("moves: ")
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

file = open(f'data/{event}.json')

json_array = load(file)
months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]



def submit(name, time, link, moves, date):
	now = datetime.datetime.now()
	submission = {'name':None, 'time':None, 'date':None, 'evidence':None, 'comments':None}
	submission['name'] = name
	submission['time'] = time
	submission['date'] = date#f'{now.year}-{months[now.month-1]}-{now.day}'
	#submission['date'] = f'{input("year: ")}-{input("year: ")}-{input("day: ")}'
	submission['evidence'] = link
	submission['comments'] = f'{moves} moves'

	json_array.append(submission)
	print("----submission----")
	print(f"name: {name}")
	print(f"event: {event}")
	print(f"time: {time}")
	with open(f'data/{event}.json', 'w', encoding='utf-8') as outfile:
		#outfile.write(str(json_array))
		dump(json_array, outfile, ensure_ascii=False, indent=2)

submit(name, time, link, moves, date)