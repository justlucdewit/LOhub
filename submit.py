from json import *
import datetime
from sys import argv
from os import system as s

events = ["3x3 blind ao5", "4nrg", "4x4 ao5", "4x4 blind", "4x4 FMC", "4x4 single", "5nrg", "5x5 ao5", "5x5 blind", "5x5 FMC", "5x5 single", "6nrg", "6x6 ao5", "6x6 FMC", "6x6 single", "7nrg", "7x7 ao5", "7x7 FMC", "7x7 single", "8x8 ao5", "8x8 single", "9x9 ao5", "9x9 single", "10x10 ao5", "10x10 single", "11x11 ao5", "11x11 single", "12x12 ao5", "12x12 single", "13x13 ao5", "13x13 single", "14x14 ao5", "14x14 single", "15x15 mo3", "15x15 single", "20x20 mo3", "20x20 single", "hexaloop 3x3 FMC", "hexaloop 3x3 single", "hexaloop 4x4 single"]

def sortfirst(val):
	return val[0]

if len(argv) > 1 and argv[1] == "send":
	s("git add .")
	s("git commit -m \"added more submissions\"")
	s("git push origin master")
	exit()

if len(argv) > 1 and argv[1] == "correct":
	for event in events:
		with open(f"data/{event}.json", "r") as file:
			json_array = load(file)

		#resorting
		found = []
		for i, submission in enumerate(json_array):
			name = submission["name"]
			time = submission["time"]
			time = [int(i) for i in time.replace(".", ":").split(":")]
			time.reverse()

			if len(time) > 1:#add the secs to the mils
				time[0] += 1000*time[1]
				time[1] = 0
			if len(time) > 2:#add the mins to the mills
				time[0] += 60000*time[2]
				time[2] = 0
			if len(time) > 3:#add hours to the mills
				time[0] += 3600000*time[3]
				time[3] = 0

			time = time[0]
			found.append([time, submission])
		
		found.sort(key=sortfirst)
		newarr = []
		for i in found:
			newarr.append(i[1])
		json_array = newarr
		#remove doubles
		found = []
		for i, submission in enumerate(json_array):
			name = submission['name']
			if name in found:
				print(f"removing double sumbission from {name} in event {event}")
				json_array.pop(i)
			else:
				found.append(name)

		with open(f'data/{event}.json', 'w', encoding='utf-8') as outfile:
			#outfile.write(str(json_array))
			dump(json_array, outfile, ensure_ascii=False, indent=2)
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

if evnt == "4nrg":
	event = "4nrg"
if evnt == "5nrg":
	event = "5nrg"
if evnt == "6nrg":
	event = "6nrg"
if evnt == "7nrg":
	event = "7nrg"

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