"""Task59"""
def guess_password(password):
    trials = 0
    for i in range(26):
        for j in range(26):
            for k in range(26):
                guess = f"{chr(65+i)}{chr(65+j)}{chr(65+k)}"
                trials += 1
                if guess == password:
                    return guess, trials
    return 0


if __name__ == "__main__":
    password = input('Type a password: ')
    guess, trials = guess_password(password)
    print(f'Guess {guess} is a match for {password}, found in {trials} trials')
