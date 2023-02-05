
from dataclasses import dataclass


@dataclass
class Player:
    pos: int = 1
    score: int = 0
    universes: int = 0

    def move(self, count):
        self.pos = ((self.pos - 1  + count) % 10) + 1
        self.score += self.pos
        self.universes += 3


class Die:
    def __init__(self):
        self.rolls = 0
        self.current = 0

    def __repr__(self):
        return f'{self.rolls=} {self.current=}'

    def roll(self):
        self.rolls += 1
        self.current = (self.current + 1) % 100
        return self.current

    def triple_roll(self):
        return self.roll(), self.roll(), self.roll()


class DiracDie(Die):
    def roll(self):
        self.rolls += 1
        self.current = (self.current + 1) % 3


def part_one():
    p1 = Player(pos=6)
    p2 = Player(pos=7)
    die = Die()
    max_score = 0
    while max_score < 1000:
        scores = sum(die.triple_roll())
        p1.move(scores)
        if p1.score >= 1000:
            break
        scores = sum(die.triple_roll())
        p2.move(scores)
        max_score = max(p1.score, p2.score)

    print(f'{p1=} {p2=} {die=}')
    print(f'Score {min(p1.score, p2.score) * die.rolls}')


def part_two():
    p1 = Player(pos=6)
    p1 = Player(pos=7)
    die = DiracDie()
    max_score = 0
    while max_score < 21:
        scores = sum(die.triple_roll())
        p1.move(scores)
        if p1.score >= 21:
            break
        scores = sum(die.triple_roll())
        p2.move(scores)
        max_score = max(p1.score, p2.score)


if __name__ == '__main__':
    part_one()
