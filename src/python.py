# this is a comment in Python

print(2+3)
# this would print 5

mckinney_texas_population = 169000
print(mckinney_texas_population)
# will print 169000
mckinney_texas_population = mckinney_texas_population + 11000
print(mckinney_texas_population)
# will print 180000
# similar to JS where you can take an existing variable and reassign a value
print(type(mckinney_texas_population))
# Using type is similar to typeOf in JS. It will return the type of what you are printing. In this case it will return integer.
frisco_texas_population = 170000.15
# frisco_texas_population is now a float
print(mckinney_texas_population < frisco_texas_population)
# will print false
print(type(mckinney_texas_population > frisco_texas_population))
# will print boolean
# type conversion example. We need to convert mckinney_texas_population (an integer) into a string, to use it in a string.
mckinney_string = 'The population of McKinney Texas is ' + str(mckinney_texas_population) + ' as of January 1st 2018.'
# we do this by putting a "str(mckinney_texas_population)" when calling that variable. this says we will use it as a string.
print(type(mckinney_string)) # prints mckinney_string
