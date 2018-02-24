import random
Users = {}

def get_user(phone):
    # Initialize this user if they're new to the system
    if phone not in Users:
        Users[phone] = {
            'answered_questions': [],
            'opponent': '',
            'points': 0
        }

    return Users[phone]

def get_random_user_number():
    return random.choice(list(Users.keys()))

def get_random_user():
    return Users[get_random_user_number()]

def update_points(phone, delta):
    usr = get_user(phone)
    usr['points'] += delta

    return usr

get_user('+447534003420')
#get_user('+4915123016551')
