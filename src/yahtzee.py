'''
    Código que nos ha aportado nuestro tutor y que debemos refactorizar y testear
'''



class Yatzy:

    @staticmethod
    def chance(*dice):
        return sum(dice)

    @staticmethod
    def yahtzee(*dice):
        if len(set(dice)) == 1:
            return 50
        return 0
    
    @staticmethod
    def ones(*dice):
        return dice.count(1)*1
    

    @staticmethod
    def twos(*dice):
        return dice.count(2)*2

    
    @staticmethod
    def threes(*dice):
        return dice.count(3)*3

    @staticmethod
    def fours(*dice):
        return dice.count(4)*4
    
    @staticmethod
    def fives(*dice):
        return dice.count(5)*5
    
    @staticmethod
    def sixes(*dice):
        return dice.count(6)*6

    @staticmethod
    def score_pair(*dice):
        for i in range(6, 0 ,-1):
            if dice.count(i) == 2:
                return i*2
        return 0



    @staticmethod
    def two_pair(*dice):
        counts = []
        score = 0
        for die in dice:
            if dice.count(die) > 1:
                if die not in counts:
                    counts.append(die)
                    die = die * dice.count(die)
                    score += die
                    if len(counts) == 2:
                        return score
                    else:
                        pass
        return 0

    @staticmethod
    def three_of_a_kind(*dice):
        for die in dice:
            if dice.count(die) == 3:
                return die * 3
            else:
                pass
        return 0



    @staticmethod
    def four_of_a_kind(*dice):
        for die in dice:
            if dice.count(die) == 4:
                return die * 4
            else:
                pass
        return 0
    
    

    @staticmethod
    def smallStraight(*dice):
        for num in range(1,6):
            count = dice.count(num)
            if count != 1:
                return 0
        return 15
    

    @staticmethod
    def largeStraight(*dice):
        for num in range(2,6):
            count = dice.count(num)
            if count != 1:
                return 0
        return 20
    

    @staticmethod
    def fullHouse(*dice):
        if Yatzy.score_pair(*dice) and Yatzy.three_of_a_kind(*dice):
            return Yatzy.score_pair(*dice) + Yatzy.three_of_a_kind(*dice)
        else:
            return 0
