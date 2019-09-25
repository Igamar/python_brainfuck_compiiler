import sys
if len(sys.argv) == 1:
	filename = input('Input name of your file: ')
else:
	filename = sys.argv[1]

if len(sys.argv) == 3:
	bits = 2**int(sys.argv[2])
else:
	bits = 256
print('Max number: ' + str(bits))
print('File "'+ filename + '" started')
file = open(filename, 'r')
code = file.read()
choosen = 0
data = []
data.append(0)
parse_now = 0
moves_counter = 0
while parse_now < len(code):
	x = code[parse_now]	
	if x.lower() == '+':
		moves_counter += 1
		data[choosen] += 1
		if data[choosen] >= bits:
			data[choosen] = 0
	elif x.lower() == '-':
		moves_counter += 1
		data[choosen] += -1
		if data[choosen] <= -1:
			data[choosen] = bits - 1
	elif x.lower() == '>':
		moves_counter += 1
		choosen += 1
		if choosen == len(data):
			data.append(0)
	elif x.lower() == '<':
		moves_counter += 1
		choosen += -1
		if choosen <= -1:
			choosen = 0
	elif x.lower() == '[':
		moves_counter += 1
		if data[choosen] == 0:
			cycle_counter = 1
			while cycle_counter != 0:
				parse_now += 1
				if code[parse_now] == ']':
					cycle_counter += -1
				elif code[parse_now] == '[':
					cycle_counter += 1
	elif x.lower() == ']':
		moves_counter += 1
		if data[choosen] != 0:
			cycle_counter = 1
			while  cycle_counter != 0:
				parse_now += -1
				if code[parse_now] == '[':
					cycle_counter += -1
				elif code[parse_now] == ']':
					cycle_counter += 1
	elif x.lower() == '.':
		moves_counter += 1
		print(chr(data[choosen]), end='')
	elif x.lower() == ',':
		moves_counter += 1
		data[choosen] == ord(input())
	parse_now += 1
file.close()
print('Program ended by ' + str(moves_counter) + ' steps')
