print('Welcome to the username generator, this program creates a username with the exponential'
    'distribution (pdf and CDF), the number evaluated in the pdf and CDF will be in your username!')

number = int(input("What is your favorite number between 0 and infinity?"))
lamd = float(input("What is your favourite lamda?"))
zodiac = input("What is your zodiac sign?")


pdf = lamd * pow(2.7182, -lamd * number)
CDF = 1-pow(2.7182, -lamd * number)
print(f'Your user name is: {CDF}{zodiac}{pdf}')



