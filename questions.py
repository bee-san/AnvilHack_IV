import random
Questions = [
    {
        'text': 'This is a question. The answer is b',
        'answers': {
            'a': 'A',
            'b': 'B',
            'c': 'C'
        },
        'correctAnswer': 'b'
    },
    {
        'text': 'This is a question. The answer is c',
        'answers': {
            'a': 'A',
            'b': 'B',
            'c': 'C'
        },
        'correctAnswer': 'c'
    },
    {
        'text': 'This is a question. The answer is c',
        'answers': {
            'a': 'A',
            'b': 'B',
            'c': 'C'
        },
        'correctAnswer': 'c'
    }
]

def get_random_question():
    return random.choice(Questions)

