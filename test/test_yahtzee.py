import pytest
from src.yahtzee import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


'''
Test para el método CHANCE de la clase Yatzy
'''
@pytest.mark.chance
def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)




'''
Test para el método YAHTZEE de la clase Yatzy
'''
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




'''
Test para el método ONES de la clase Yatzy
'''
@pytest.mark.ones
def test_ones():
    assert 2 == Yatzy.ones(5,4,3,1,1)
    assert 5 == Yatzy.ones(1,1,1,1,1)
    assert 0 == Yatzy.ones(2,4,2,5,6)




'''
Test para el método TWOS de la clase Yatzy
'''
pytest.mark.twos
def test_twos():
    assert 2 == Yatzy.twos(2,1,1,3,4)
    assert 8 == Yatzy.twos(2,1,2,2,2)
    assert 0 == Yatzy.twos(1,4,4,6,7)

    

