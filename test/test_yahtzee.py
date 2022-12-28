import pytest
from src.yahtzee import Yatzy


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
    assert 50 == Yatzy.yahtzee(1,1,1,1,1)
    assert 50 == Yatzy.yahtzee(6,6,6,6,6)

@pytest.mark.yahtzee_nonbonus
def test_failyahtzee():
    assert 0 == Yatzy.yahtzee(1,1,1,2,1)
    assert 0 == Yatzy.yahtzee(3,1,1,2,1)


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

'''
Test para el método THREES de la clase Yatzy
'''
pytest.mark.threes
def test_threes():
    assert 3 == Yatzy.threes(2,3,1,1,1)
    assert 9 == Yatzy.threes(2,3,3,3,2)
    assert 0 == Yatzy.threes(2,1,1,2,1)

'''
Test para el método FOURS de la clase Yatzy
'''
pytest.mark.fours
def test_fours():
    assert 4 == Yatzy.fours(2,3,4,5,6)
    assert 8 == Yatzy.fours(2,3,4,4,2)
    assert 0 == Yatzy.fours(1,3,2,5,6)


'''
Test para el método FIVES de la clase Yatzy
'''
pytest.mark.fives
def test_fives():
    assert 5 == Yatzy.fives(2,3,4,5,6)
    assert 15 == Yatzy.fives(2,3,5,5,5)
    assert 0 == Yatzy.fives(2,2,2,2,2)

'''
Test para el método SIXES de la clase Yatzy
'''
pytest.mark.sixes
def test_sixes():
    assert 6 == Yatzy.sixes(2,3,4,5,6)
    assert 18 == Yatzy.sixes(2,3,6,6,6)
    assert 0 == Yatzy.sixes(2,2,2,2,2)

'''
Test para el método SCORE PAIR de la clase Yatzy
'''
pytest.mark.score_pair
def test_score_pair():
    assert 8 == Yatzy.score_pair(3,3,3,4,4)
    assert 0 == Yatzy.score_pair(1,2,3,4,5)
    assert 6 == Yatzy.score_pair(3,3,1,2,1)

'''
Test para el método TWO PAIR de la clase Yatzy
'''
pytest.mark.two_pair
def test_two_pair():
    assert 8 == Yatzy.two_pair(1,1,2,3,3)
    assert 0 == Yatzy.two_pair(1,1,2,3,4)

'''
Test para el método THREE OF A KIND de la clase Yatzy
'''
pytest.mark.three_of_kind
def test_three_of_kind():
    assert 9 == Yatzy.three_of_a_kind(3,3,3,4,5)
    assert 0 == Yatzy.three_of_a_kind(3,3,4,5,6)

'''
Test para el método FOUR OF A KIND de la clase Yatzy
'''
pytest.mark.four_of_kind
def test_four_of_kind():
    assert 8 == Yatzy.four_of_a_kind(2,2,2,2,5)
    assert 0 == Yatzy.four_of_a_kind(2,2,2,4,4)

'''
Test para el método SMALLSTRAIGHT de la clase Yatzy
'''
pytest.mark.smallStraight
def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1,2,3,4,5)
    assert 0 == Yatzy.smallStraight(1,3,4,6,3)

'''
Test para el método LARGESTRAIGHT de la clase Yatzy
'''
pytest.mark.largeStraight
def test_largeStraight():
    assert 20 == Yatzy.largeStraight(2,3,4,5,6)
    assert 0 == Yatzy.largeStraight(1,2,4,5,1)

'''
Test para el método FULLHOUSE de la clase Yatzy
'''
pytest.mark.fullHouse
def test_fullHouse():
    assert 8 == Yatzy.fullHouse(1,1,2,2,2)
    assert 0 == Yatzy.fullHouse(2,2,3,3,4)
    assert 0 == Yatzy.fullHouse(4,4,4,4,4)
    