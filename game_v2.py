import numpy as np

def random_predict(number:int=1) -> int:    #number:int - type of value expected on input
                                            # -> int - type of value expected on output (works as auto stringline tag)
    """randomly guess a correct value

    Args:
        number (int, optional): the secret number. Defaults to 1.

    Returns:
        int: num of tries required
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # some random guess
        if number == predict_number:
            break #cancel the cycle if the guess is right
    return(count)

def score_game(random_predict) ->int:
    """mean of 1000 tries

    Args:
        random_predict (value): guessing function

    Returns:
        int: mean number of attempts in 1000 tries
    """
    count_ls = [] #list with tries num
    np.random.seed(1)   #to make results reproducible
    random_array = np.random.randint(1, 101, size=(1000))   #list of guessed numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':  #will not be executed if the file is imported as a library
# RUN
    score_game(random_predict)


        