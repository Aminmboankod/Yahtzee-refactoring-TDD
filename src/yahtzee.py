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
        sum = 0
        for i in dice:
            if i == 1:
                sum += 1
        return sum
    

    @staticmethod
    def twos(*dice):
        sum = 0
        for i in dice:
            if i == 2:
                sum += 2
        return sum

    
    @staticmethod
    def threes(*dice):
        sum = 0
        for i in dice:
            if i == 3:
                sum += 3
        return sum

    @staticmethod
    def fours(*dice):
        sum = 0
        for i in dice:
            if i == 4:
                sum += 4
        return sum
    
    @staticmethod
    def fives(*dice):
        sum = 0
        for i in dice:
            if i == 5:
                sum += 5
        return sum
    
    @staticmethod
    def sixes(*dice):
        sum = 0
        for i in dice:
            if i == 6:
                sum += 6
        return sum

    @staticmethod
    def score_pair(*dice):
        for i in range(6, 0 ,-1):
            if dice.count(i) > 1:
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
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
