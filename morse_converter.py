from tabulate import tabulate

morse_dict = {
	'A': '.-',
	'B': '-...',
	'C': '-.-.',
	'D': '-..',
	'E': '.',
	'F': '..-.',
	'G': '--.',
	'H': '....',
	'I': '..',
	'J': '.---',
	'K': '-.-',
	'L': '.-..',
	'M': '--',
	'N': '-.',
	'O': '---',
	'P': '.--.',
	'Q': '--.-',
	'R': '.-.',
	'S': '...',
	'T': '-',
	'U': '..-',
	'V': '...-',
	'W': '.--',
	'X': '-..-',
	'Y': '-.--',
	'Z': '--..',
	'1': '.----',
	'2': '..---',
	'3': '...--',
	'4': '....-',
	'5': '.....',
	'6': '-....',
	'7': '--...',
	'8': '---..',
	'9': '----.',
	'0': '-----',
	'?': '..--..',
	'!': '-.-.--',
	'.': '.-.-.-',
	',': '--..--',
	';': '-.-.-.',
	':': '---...',
	'+': '.-.-.',
	'-': '-....-',
	'/': '-..-.',
	'=': '-...-',
	' ': '/'
} 

operation_list = [['Operations', 'Definition'], ['1', 'Morse to String'], ['2', 'String to Morse'], ['99', 'Exit']]
table = operation_list
print("Hello! This program is a converter between Morse code and Strings.")
print(tabulate(table))

try:
	while True:
		operation = input('\nPlease enter the number of the operation you want: ')
		result = ''

		if operation == '1':
			print("\nWhen using this operation please put space in every letter for word and put '/' for spaces between words.")
			m_string = input('\nPlease enter your morse code here: ')
			m_string_split = m_string.split()
			for i in m_string_split:
				result = result + list(morse_dict.keys())[list(morse_dict.values()).index(i)]
			print(result)
		elif operation == '2':
			n_string = input('\nPlease enter your message here: ')
			n_string_cap = n_string.upper()
			for i in n_string_cap:
				result = result + morse_dict.get(i) + ' '
			print(result)
		elif operation == '99':
			print('\nExitted the program.')
			break
		else:
			print('Entered an invalid value. Please enter again.\nIf you want to exit please press 99.')

except KeyboardInterrupt:
	print('\nExitted the program.')


