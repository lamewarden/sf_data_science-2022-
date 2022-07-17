import numpy as np

def fractions_of_100_predict(number:int=1) -> int:    #number:int - type of value expected on input
                                                      # -> int - type of value expected on output (works as auto stringline tag)
    """We compare the secret number with the fractions of 100 devided by 2. On every attempt we divide 

    Args:
        number (int, optional): the secret number. Defaults to 1.

    Returns:
        int: num of tries required
    """
    
    count = 0
    guess = 0   #variable representing the size of step from the previous guess
    predict_number = 50     # We are starting from the middle of the 100
    
    while True:
        count += 1


        predict_number = predict_number + guess # previous prediction plus (or minus)
        if number < predict_number:
            guess = -(100//(2**(count+1)))
            if guess > -1:  #avoiding the trap of guess rounded to 0
                guess = -1
        elif number > predict_number:
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


        