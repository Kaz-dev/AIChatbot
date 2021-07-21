import random

R_EATING = "I don't eat anything, I'm a bot obviously lol"


def unknown():
    response = ['Could you please re-phrase that?',
                "...",
                "Does not compute :(",
                "What does that mean?"][random.randrange(4)]
    return response


def greeting():
    response = ['Hello',
                'Hi!',
                'Howdy'][random.randrange(3)]
    return response
