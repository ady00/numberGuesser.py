import random
n = random.randint(1, 9)
guess_count = 0
guess_limit = 4     



while guess_count <= guess_limit :
    guess = int(input("Enter an integer from 1 to 9: "))
    guess_count += 1   

    if guess == n:
        print("Good job! you guessed it in ", guess_count,"guesses.")
        break

    elif guess > n:
        print("Too high! Go a bit lower.")

    elif guess < n:
        print("Too low! Go a bit higher.")

    
else:

    print ("You are out of tries! The correct number was", n)



    
    


