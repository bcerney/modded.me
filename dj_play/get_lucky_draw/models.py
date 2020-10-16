from random import choice, choices, randint

from django.db import models


# Create your models here.
class ActionBodyPartCard:

    # TODO: which verbs do we actually want? This can be configurable
    ACTIONS = ["Massage", "Kiss", "Lick", "Blow", "Suck", "Pat"]
    ACTIONS_WEIGHTS = [0.6, 0.3, 0.025, 0.025, 0.025, 0.025]
    BODY_PARTS = [
        "Player Choice",
        "Neck",
        "Shoulders",
        "Back",
        "Hips",
        "Thighs",
        "Calves",
        "Navel",
        "Ear",
        "Lips",
        "Chest",
        "Butt",
        "Groin",
    ]
    BODY_PARTS_WEIGHTS = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.025, 0.025, 0.025, 0.025]

    def __init__(self):
        self.title = "Action Card"
        self.action = choices(
            population=ActionBodyPartCard.ACTIONS,
            weights=ActionBodyPartCard.ACTIONS_WEIGHTS,
            k=1,
        )[0]
        self.body_part = choices(
            population=ActionBodyPartCard.BODY_PARTS,
            weights=ActionBodyPartCard.BODY_PARTS_WEIGHTS,
            k=1,
        )[0]
        # seconds
        self.time = randint(30, 60)

    def __str__(self):
        return f"{self.title} | {self.action} | {self.body_part} | {self.time} seconds"


class StripGameCard:
    def __init__(self):
        self.title = "Strip Poker Card"
        self.action = "Play a round of Strip Poker!"
        pass

    def __str__(self):
        return f"{self.title} | {self.action}"
