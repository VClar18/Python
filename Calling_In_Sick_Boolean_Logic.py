# In this exercise you will be given a few variables that will be set randomly to Boolean values (True  or False ):
# actually_sick  - when you legit have the flu!
# kinda_sick  - you're feeling under the weather and it's enough to treat yoself with a day off if you can spare it
# hate_your_job  - work sucks, I know... 
# You're also given a random number of sick_days between 0 and 10.
# Finally, there is a variable called calling_in_sick  that you must set to True  or False  based on the following scenarios:
# Set to True if: 
# you're actually_sick  and you have sick_days  remaining
# you're kinda_sick  and hate_your_job  and you have sick_days  remaining
# Otherwise, set to False.
# The tests check that the value of calling_in_sick  is correct based on the conditions specified above.

# NO TOUCHING ======================================

from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

# NO TOUCHING ======================================

calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

print(f"Actually sick: {actually_sick}")
print(f"Kinda sick: {kinda_sick}")
print(f"Hate your job: {hate_your_job}")
print(f"Sick days: {sick_days}")

# Note, we don't need to check if actually_sick == True
#  Instead, just check if actually_sick, since it's a boolean
if actually_sick  and sick_days > 0:
    calling_in_sick=True
    print("You can call off")
elif kinda_sick  and hate_your_job  and sick_days > 0:
    calling_in_sick=True
    print("You can call off")
else:
    calling_in_sick ==False
    print("You cannot call off")



# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
