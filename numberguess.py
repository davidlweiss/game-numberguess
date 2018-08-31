"""
This program will roll a pair of dice and ask the user to guess the sum. If the user's guess is equal to the total value of the dice roll, the user wins! Otherwise, the computer wins.
"""
from random import randint
from time import sleep

def get_user_guess():
    guess = int(input("Guess a number: "))
    return guess

def guess_lower_number():
    guess = int(input("Guess a lower number: "))
    return guess

number_of_sides = int(input("Pick the number of dice sides to play with between 1 and 6: "))

def roll_dice(number_of_sides):
     max_val = number_of_sides * 2
     print("The maximum value is %d" % max_val)
     guess = get_user_guess()
     first_roll = randint(1,number_of_sides)
     second_roll = randint(1,number_of_sides)
     while guess > max_val:
         print("Remember the maximum value is %d" % max_val)
         guess = guess_lower_number()
     else:
          print("Rolling...")
          sleep(2)
          print("The 1st roll is %d" % first_roll)
          sleep(1)
          print("The 2nd roll is %d" % second_roll)
          total_roll = first_roll + second_roll
          print("Here come the results...")
          sleep(1)
          print("Your guess was %d, and the total was %d" % (guess, total_roll))
          if guess == total_roll:
              print("You got it! Nice work!")
          else:
              print("Nice try! But no dice ;)")

roll_dice(number_of_sides)
