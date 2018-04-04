# -*- coding: utf-8 -*-

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
	print("El caracter que ingresaste no se encuentra, intenta nuevamente")
	exit()

def decipher(message):
    try:
    	words = message.split(' ')
    	tam=len(words)
    	mensaje_decifrado = []
    	decifrando_letra = ''
    	for i in range(tam):
            decifrando_letra += KEYS2[words[i]]
    
        mensaje_decifrado.append(decifrando_letra)

    	return ''.join(decifrando_letra)
	
    except:
	print("")
	print("")
	print("El cifrado que ingresaste es incorrecto, Lee las instrucciones y vuelve a intentarlo")
	exit()

def run():

    while True:

        command = str(raw_input('''-----------------------------------------------------------------

            Bienvenido a criptografía morse. ¿Qué deseas hacer?

            [1] Cifrar mensaje
            [2] Decifrar mensaje
	    [3] Ayuda
            [4] Salir
        '''))

        if command == '1':
            message = str(raw_input('Escribe tu mensaje: ')).upper()
            cypher_message = cypher(message)
            print('Mensaje cifrado = ' + cypher_message)
	
        elif command == '2':
            message = str(raw_input('Escribe el mensaje cifrado y cambia los "/" por un espacio " ": '))
            decypher_message = decipher(message)
            print('Mensaje descifrado = ' + decypher_message)
	elif command == '3':
	    print('El programa es muy sencillo de usar, al momento de cifrar la informacion no tendras ningun')
	    print('problema al menos que escribas un caracter que no sea valido o no este en los teclados americanos')
	    print('al momento de descifrar tienes que cambiar obligatoriamente los "/" por un espacio " " ya que')
	    print('el programa no entiende cuando estan todos los caracteres unidos, aun asi los juntara en una')
	    print('palabra, por eso se recomienda que cuando son oraciones, se tradusca palabra por palabra')
	    print('o todo se unira en una sola.')
        elif command == '4':
            exit()
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('''
    ███╗   ███╗ ██████╗ ██████╗ ███████╗███████╗
    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██╔════╝
    ██╔████╔██║██║   ██║██████╔╝███████╗█████╗  
    ██║╚██╔╝██║██║   ██║██╔══██╗╚════██║██╔══╝  
    ██║ ╚═╝ ██║╚██████╔╝██║  ██║███████║███████╗
    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
                                           By Luis Scozzese
''')
    run()
