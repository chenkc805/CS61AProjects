"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Roll DICE for NUM_ROLLS times.  Return either the sum of the outcomes,
    or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A zero-argument function that returns an integer outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    "*** YOUR CODE HERE ***"
    a = 0
    while num_rolls:
        b = dice()
        if b != 1:
            a = b + a
            num_rolls -= 1
        else:
            num_rolls -=1
            while num_rolls:
                num_rolls -= 1
                dice()
            return 1
    return a

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    "*** YOUR CODE HERE ***"

    def free_bacon(n):
        first_digit, second_digit = n // 10 , n % 10  
        return 1 + abs(first_digit-second_digit)
    if num_rolls != 0:
        return roll_dice(num_rolls, dice)
    else:
        return free_bacon(opponent_score)


def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    "*** YOUR CODE HERE ***"
    if (score + opponent_score) % 7 == 0:
        return four_sided
    else:
        return six_sided

def bid_for_start(bid0, bid1, goal=GOAL_SCORE):
    """Given the bids BID0 and BID1 of each player, returns three values:

    - the starting score of player 0
    - the starting score of player 1
    - the number of the player who rolls first (0 or 1)
    """
    assert bid0 >= 0 and bid1 >= 0, "Bids should be non-negative!"
    assert type(bid0) == int and type(bid1) == int, "Bids should be integers!"

    # The buggy code is below:
    if bid0 == bid1:
        return goal, goal, 1
    elif bid0 == bid1 - 5:
        return 0, 10, 1
    elif bid1 == bid0 - 5:
        return 10, 0, 0
    elif bid1 > bid0:
        return bid1, bid0, 1
    else:
        return bid1, bid0, 0

def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who   

def swine_swap(score0, score1):
    if score0 == 2 * score1 or score1 == 2 * score0:
        score0_placeholder = score0
        score0 = score1
        score1 = score0_placeholder
        return score0, score1
    return score0, score1

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    "*** YOUR CODE HERE ***"
    while score0 < 100 and score1 < 100:
        if who == 0:
            score0 = score0 + take_turn(strategy0(score0, score1), score1, select_dice(score0, score1))
        else:
            score1 = score1 + take_turn(strategy1(score1, score0), score0, select_dice(score0, score1))
        score0, score1 = swine_swap(score0, score1)
        who = other(who)
    return score0, score1 

#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=5000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    "*** YOUR CODE HERE ***"
    def make_averaged_nested(*args):
        x = 0
        n = num_samples
        while n:
            n -= 1
            x = fn(*args) + x
        return x / num_samples
    return make_averaged_nested

def max_scoring_num_rolls(dice=six_sided):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE.  Print all averages as in
    the doctest below.  Assume that dice always returns positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    "*** YOUR CODE HERE ***"
    n = 1
    best_score = 0
    best_number_of_rolls = 0
    while n <=10:
        averaged_dice = make_averaged(roll_dice)
        a = averaged_dice(n, dice)
        if a > best_score:
            best_score = a
            best_number_of_rolls = n
        n+=1
    return best_number_of_rolls


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False: # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False: # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if True: # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"

# Strategies
def three_steps(score, opponent_score, num_rolls):
    dice = select_dice(score, opponent_score)
    regular_roll = take_turn(num_rolls, opponent_score, dice)
    bacon_roll = take_turn(0,opponent_score,dice)
    return dice, regular_roll, bacon_roll

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    "*** YOUR CODE HERE ***"
    dice, regular_roll, bacon_roll = three_steps(score, opponent_score, num_rolls)
    if bacon_roll >= margin:
        return 0
    return num_rolls

def swap_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it would result in a beneficial swap and
    rolls NUM_ROLLS if it would result in a harmful swap. It also rolls
    0 dice if that gives at least MARGIN points and rolls
    NUM_ROLLS otherwise.
    """
    "*** YOUR CODE HERE ***"
    dice, regular_roll, bacon_roll = three_steps(score, opponent_score, num_rolls)
    after_bacon_roll = score + bacon_roll
    if after_bacon_roll == opponent_score * 2 or opponent_score == after_bacon_roll * 2:
        swine_swap_score, swine_swap_opponent_score = swine_swap(after_bacon_roll, opponent_score)
        if swine_swap_score > swine_swap_opponent_score:
            return 0
        return num_rolls
    return bacon_strategy(after_bacon_roll, opponent_score, margin, num_rolls)


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    If the OPPONENT_SCORE==2*(SCORE+1), then you want to roll 10 times to try to get a 1
    If the OPPONENT_SCORE==2*(SCORE+ the score from FREE_BACON), then roll 0 times. 

    """
    "*** YOUR CODE HERE ***"
    dice = select_dice(score, opponent_score)
    bacon_roll = take_turn(0, opponent_score,dice)
    if score + bacon_roll >= 100 and score + bacon_roll != 2 * opponent_score:
        return 0
    if opponent_score > score:
        if opponent_score == 2*(score + 1) and opponent_score > 30:
            return 10 #swine swap
        if opponent_score == 2 * (score + bacon_roll) and opponent_score > 30:
            return 0 #swine swap and free bacon
        if opponent_score >= score + 20:
            return 6 #regular roll
        if bacon_roll >= 8:
            return 0 #free bacon
    else:
        if ((2 * opponent_score == score + 1) and bacon_roll >=8):
            return 0 #avoiding swine swap
        if (2 * opponent_score == score + 1) or 2 * opponent_score == score + bacon_roll:
            return 5 #regular roll
        if (opponent_score + score + bacon_roll) % 7 == 0:
            return 0 #free bacon to get hog wild
    return swap_strategy(score, opponent_score)



##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
