#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import system

RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'

KEYS = {'A': '.-/',     'B': '-.../',   'C': '-.-./', 
        'D': '-../',    'E': './',      'F': '..-./',
        'G': '--./',    'H': '..../',   'I': '../',
        'J': '.---/',   'K': '-.-/',    'L': '.-../',
        'M': '--/',     'N': '-./',     'O': '---/',
        'P': '.--./',   'Q': '--.-/',   'R': '.-./',
        'S': '.../',    'T': '-/',      'U': '..-/',
        'V': '...-/',   'W': '.--/',    'X': '-..-/',
        'Y': '-.--/',   'Z': '--../',	'Ñ': '--.--/',
        '0': '-----/',  '1': '.----/',  '2': '..---/',
        '3': '...--/',  '4': '....-/',  '5': '...../',
        '6': '-..../',  '7': '--.../',  '8': '---../',
        '9': '----./',  '?': '?',       '¿': '¿',
	'´': '´',	'=': '=',	'(': '(',
	')': ')',	',': ',',	'&': '&',
	'%': '%',	'$': '$',	'#': '#',
	'"': '"',	'!': '!',	'¡': '¡',
	'<': '<',	'>': '>',	'.': '/',
	'_': '_',	'*': '*',       '@': '@',
	']': ']',	'{': '{',	'}': '}',
	'[': '['
	 
        }

KEYS2 = {'.-': 'A',     '-...': 'B',   '-.-.': 'C', 
        '-..': 'D',    '.': 'E',      '..-.': 'F',
        '--.': 'G',    '....': 'H',   '..': 'I',
        '.---': 'J',   '-.-': 'K',    '.-..': 'L',
        '--': 'M',     '-.': 'N',     '---': 'O',
        '.--.': 'P',   '--.-': 'Q',   '.-.': 'R',
        '...': 'S',    '-': 'T',      '..-': 'U',
        '...-': 'V',   '.--': 'W',    '-..-': 'X',
        '-.--': 'Y',   '--..': 'Z',   '--.--': 'Ñ',
        '-----': '0',  '.----': '1',  '..---': '2',
        '...--': '3',  '....-': '4',  '.....': '5',
        '-....': '6',  '--...': '7',  '---..': '8',
        '----.': '9',  '?': '?',       '¿': '¿',
	'´': '´',	'=': '=',	'(': '(',
	')': ')',	',': ',',	'&': '&',
	'%': '%',	'$': '$',	'#': '#',
	'"': '"',	'!': '!',	'¡': '¡',
	'<': '<',	'>': '>',	'[': '[',
	'_': '_',	'*': '*',       '@': '@',
	']': ']',	'{': '{',	'}': '}'
        }

def cypher(message):
    try:
    	words = message.split(' ')
    	cypher_message = []

    	for word in words:
            cypher_word = ''
            for letter in word:
                cypher_word += KEYS[letter]

            cypher_message.append(cypher_word)

    	return ' '.join(cypher_message)
    except:
	print("")
	print("")
	print("        {0}[{1}!{0}]{1}The entered character is not found, try again".format(RED, END,))
	run()

def decypher(message):
    try:
    	words = message.split(' ')
    	tam=len(words)
    	decypher_message = []
    	decypher_word = ''
    	for i in range(tam):
            decypher_word += KEYS2[words[i]]
    
        decypher_message.append(decypher_word)

    	return ''.join(decypher_word)
	
    except:
	print("")
	print("")
	print("        {0}[{1}!{0}]{1}The entered character is not found, try again".format(RED, END,))
	run()

def run():
	
    while True:
        command = raw_input("""
	-----------------------------------------------------------------

           Welcome to morse code cypher. What do you want to do?

           {0}[{1}1{0}]{1} Cypher a message
           {0}[{1}2{0}]{1} Decypher a message  
           {0}[{1}3{0}]{1} Exit 
	""".format(CYAN, END))

        if command == '1':
            message = str(raw_input('Write a Message: ')).upper()
            cypher_message = cypher(message)
            print('Encrypted message = ' + cypher_message)
	
        elif command == '2':
            message = str(raw_input('Write the encrypted message. Make sure to change the "/" for a space " ": '))
            decypher_message = decypher(message)
            print('Decrypted message = ' + decypher_message)
        elif command == '3':
	    print("                                    {0}[{1}{2}Good Bye!{1}{0}]{1}".format(CYAN, END, GREEN))
            exit()
        else:
            print("        {0}[{1}!{0}]{1}Command not found".format(RED, END,))
		

if __name__ == '__main__':
    try:
    	system('clear')

    	print("    ███╗   ███╗ ██████╗ ██████╗ ███████╗███████╗")
    	print("    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██╔════╝")
    	print("    ██╔████╔██║██║   ██║██████╔╝███████╗█████╗")
    	print("    ██║╚██╔╝██║██║   ██║██╔══██╗╚════██║██╔══╝")
    	print("    ██║ ╚═╝ ██║╚██████╔╝██║  ██║███████║███████╗")
    	print("    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝")
    	print("                                    {0}By Luis Scozzese{1} ".format(GREEN, END))

    	run()
    except KeyboardInterrupt:
	print("")
	print("")
	print("")
	print("                                    {0}[{1}{0}Good Bye!{1}{0}]{1}".format(CYAN, END))
	exit(0)
