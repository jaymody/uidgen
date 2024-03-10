import random

from .data import adjectives, nouns


def generate():
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    number = str(random.randint(0, 9))
    return "-".join([adjective, noun, number])
