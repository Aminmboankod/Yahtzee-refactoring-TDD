'''
En este fichero escribiré los casos test que se vayan planteando posteriores a la lectura y comprensión del juego y las funciones de cada rutina.
'''
import pytest
from src.yahtzee import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.

@pytest.mark.chance
def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)

@pytest.mark.yahtzee_bonus
def test_yahtzee():
    bonus = [1,1,1,1,1]
    assert 50 == Yatzy.yahtzee(bonus)
    bonus = [6,6,6,6,6]
    assert 50 == Yatzy.yahtzee(bonus)

@pytest.mark.yahtzee_nonbonus
def test_failyahtzee():
    nonbonus = [1,1,1,2,1]
    assert 0 == Yatzy.yahtzee(nonbonus)
    nonbonus = [3,1,1,2,1]
    assert 0 == Yatzy.yahtzee(nonbonus)