import random

Users = []

def get_user(phone):
    # Initialize this user if they're new to the system
    if phone not in Users:
        Users[phone] = {
            'answered_questions': [],
            'opponent': '',
            'points': 0
        }

    return Users[phone]

def get_random_user():
    return random.choice(Users)

def update_points(phone, delta):
    usr = get_user(phone)
    usr['points'] += delta

    return usr
