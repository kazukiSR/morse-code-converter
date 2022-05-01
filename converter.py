import re
AZ_TO_MORSE = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..',
    '1': '.____',
    '2': '..___',
    '3': '...__',
    '4': '...._',
    '5': '.....',
    '6': '_....',
    '7': '__...',
    '8': '___..',
    '9': '____.',
    '0': '_____',
    '.': '._._._',
    ',': '__..__',
    '?': '..__..',
    "'": '.____.',
    '!': '_._.__',
    '/': '_.._.',
    '(': '_.__.',
    ')': '_.__._',
    '&': '._...',
    ':': '___...',
    ';': '_._._.',
    '=': '_..._',
    '+': '._._.',
    '-': '_...._',
    '_': '..__._',
    '"': '._.._.',
    '$': '..._.._',
    '@': '.__._.',
    ' ': '/',
}
az_list = list(AZ_TO_MORSE.keys())
morse_list = list(AZ_TO_MORSE.values())


def convert(msg):
    output_list = []
    # Searches for any occurrence of a character that is not ._/
    if re.search("[^._/ ]", msg):
        for char in msg.lower():
            output_list.append(translate_to_morse(char))
        return " ".join(output_list)
    else:
        for code in msg.split():
            output_list.append(translate_from_morse(code))
        return "".join(output_list)


def translate_to_morse(char):
    pos = az_list.index(char)
    return morse_list[pos]


def translate_from_morse(msg):
    pos = morse_list.index(msg)
    return az_list[pos]
