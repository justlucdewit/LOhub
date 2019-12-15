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

if evnt == "8x85":
	event = "8x8 ao5"
if evnt == "8x8s":
	event = "8x8 single"

if evnt == "9x95":
	event = "9x9 ao5"
if evnt == "9x9s":
	event = "9x9 single"

if evnt == "10x105":
	event = "10x10 ao5"
if evnt == "10x10s":
	event = "10x10 single"

if evnt == "11x115":
	event = "11x11 ao5"
if evnt == "11x11s":
	event = "11x11 single"

if evnt == "12x125":
	event = "12x12 ao5"
if evnt == "12x12s":
	event = "12x12 single"

if evnt == "13x135":
	event = "13x13 ao5"
if evnt == "13x13s":
	event = "13x13 single"

if evnt == "14x145":
	event = "14x14 ao5"
if evnt == "14x14s":
	event = "14x14 single"

if evnt == "15x153":
	event = "15x15 mo3"
if evnt == "15x15s":
	event = "15x15 single"

if evnt == "20x203":
	event = "20x20 mo3"
if evnt == "20x20s":
	event = "20x20 single"

if evnt == "hex3":
	event = "hexaloop 3x3 single"
if evnt == "hex4":
	event = "hexaloop 4x4 single"
if evnt == "hex3f":
	event = "hexaloop 3x3 FMC"

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