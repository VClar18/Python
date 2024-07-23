#Set the variable called first  to your first name.
#Set the variable called last  to your last name.
#Then set the variable called formatted  to a new string that interpolates both values (from the first and last variables) using f-strings or the .format()  method.  Make sure you follow this exact pattern for the new string that you store to the formatted variable (pay attention to capital/lowercase letters, spaces, commas, etc):
#"First Name: Colt, Last Name: Steele"

#Reused Variables
first = "Victoria" 
last = "Clarchick"
 
# #Using .format()

formatted_dot = "First Name: {}, Last Name: {}".format(first, last)

#Using f-strings, I think it's a much nicer syntax:

formatted_string = f"First Name: {first}, Last Name: {last}"

#Print out results of both
print(f"{formatted_dot}\n{formatted_string}")