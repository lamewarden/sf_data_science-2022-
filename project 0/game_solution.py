import numpy as np

def fractions_of_100_predict(number:int=1) -> int:    #number:int - type of value expected on input
                                                      # -> int - type of value expected on output (works as auto stringline tag)
    """The easiest way to guess a number is to divide the original interval into the two equal sub-intervals
    and find in which of them our secret number is (we ask if our secret number is bigger or smaller 
    than the number in the middle of the interval). On every step, the interval shrinks two-fold 
    until it becomes an interval with a single number - our secret number (if it was not found earlier by accident).
    Args:
        number (int, optional): the secret number. Default is 1.

    Returns:
        int: num of guesses required to find a secret number.
    """
    
    count = 0   #the number of attempts
    guess = 0   #variable representing the direction in which our interval will shrink (+ or -)
    predict_number = 50     # We are starting from the middle of the 100
    
    while True:
        count += 1
        predict_number = predict_number + guess # defining the new search interval
        if number < predict_number:     # if a secret number is smaller than the max of the new interval,
                                        # we go lower (-)
            guess = -(100//(2**(count+1)))  #interval is decreasing two-fold each next guess
            if guess > -1:  #avoiding the trap of guess rounded to 0
                guess = -1
        elif number > predict_number:   # if a secret number is bigger the max of the interval, we go higher (+)
            guess = 100//(2**(count+1))
            if guess < 1:   #avoiding the trap of guess rounded to 0
                guess = 1
        else:
            break #cancel the cycle if the guess is right
    return(count)

def score_game(fractions_of_100_predict) ->int:
    """mean of 1000 attempts

    Args:
        fractions_of_100_predict (value): guessing function

    Returns:
        int: mean number of attempts in 1000 tries
    """
    count_ls = [] #list with attempts num
    np.random.seed(1)   #making results reproducible
    random_array = np.random.randint(1, 101, size=(1000))   #list of guessed numbers
    
    for number in random_array:
        count_ls.append(fractions_of_100_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':  #will not be executed if the file is imported as a library
# RUN
    score_game(fractions_of_100_predict)


        