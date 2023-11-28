# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

#input for the year of origin from the user
year =int(input("Greetings! What is your year of origin?"))

#checking if the year is in the past or not
if year <=1900:
    print ("Woah, that's the past!")
#checking if the year is in the present or not
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")
