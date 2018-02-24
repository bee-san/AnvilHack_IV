import random
Questions = [
    {
        'text': 'What does the following code print to the console?

'var what = function () { return "HI!!!!" };
'console.log(typeof(what));,

        'answers': {
            'a': 'It will return "HI!!!!" ',
            'b':'The typeof function returns the string "function", even though functions are a special type of object, 
                'because it is useful to differentiate between functions and "regular" objects',
            'c': 'It will return "hi!!!!"'
        },
        'correctAnswer': 'b'
    },
    {
        'text': 'What does the following code print?

'class Wire:'
    'def length():'
        'return "short"'

'charger = Wire()'

'print(charger.length())',

        'answers': {
            'a': "Won't compile",
            'b': 'Returns "short"',
            'c': 'This code raises a TypeError '
        },
        'correctAnswer': 'c'
    },
    {
        'text': 'What tag is used to define an interactive field where users can enter data in html?',
        'answers': {
            'a': '<Enterpoint',
            'b': '<Em>',
            'c': '<Input>'
        },
        'correctAnswer': 'c'
    }
]

def get_random_question():
    return random.choice(Questions)
