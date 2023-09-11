"""
Purpose: Using numeric lists to identify count of Bigfoot sightings in the United States.

"""

# import some standard modules first
import statistics
import math


# TODO: import from local util_datafun_logger.py 
# import from local files
from util_datafun_logger import setup_logger

# Set up logging .............................................
# TODO: Call the setup_logger function to create a logger and get the log file name

# Call the setup_logger function
logger, logname = setup_logger(__file__)

# Define shared data ..........................................
# TODO: Create some shared data lists if you like - or just create them in your functions

# Number of Bigfoot sightings per State from a sample list of 25 States
state_sightings_list = [
    22,
    102,
    111,
    85,
    461,
    130,
    22,
    5,
    339,
    140,
    76,
    103,
    303,
    82,
    49,
    115,
    44,
    37,
    35,
    21,
    225,
    77,
    167,
    24,
    53,
]

# xtimes list represents months of the year
# yvalues list represents number of sightings per month in the most widely reported county, Humboldt County - CA
xtimes_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
yvalues_list = [2, 1, 2, 4, 2, 7, 7, 7, 3, 3, 3, 0]

# TODO: define some custom functions


def illustrate_list_statistics():
    """This function illustrates descriptive statistics for a numric list."""

    logger.info(f"state_sightings_list: {state_sightings_list}")

    #Calculate Mean, Median, & Mode of the State Sightings list
    #Find Standard Deviation and Variance of the State Sightings list

    mean = statistics.mean(state_sightings_list)
    median = statistics.median(state_sightings_list)
    mode = statistics.mode(state_sightings_list)

    logger.info(f"mean: {mean}")
    logger.info(f"median: {median}")
    logger.info(f"mode: {mode}")

    stdev = statistics.stdev(state_sightings_list)
    variance = statistics.variance(state_sightings_list)

    logger.info(f"stdev: {stdev}")
    logger.info(f"variance: {variance}")

#Use the Statistics Module to find the correlation between x & y lists


def illustrate_list_correlation_and_prediction():
    """This function illustrates correlation and prediction for a numric list."""

    logger.info(f"xtimes_list: {xtimes_list}")
    logger.info(f"yvalues_list: {yvalues_list}")

    correlationxy = statistics.correlation(xtimes_list, yvalues_list)
    logger.info(f"correlation between x and y: {correlationxy}")

    #Calculate the slope intercept using statistics.linear_regression
    x_max = max(xtimes_list)
    newx = x_max * 15  # predict for a future x value

    # Use the slope and intercept to predict a y value for the future x value
    # y = mx + b

    newy = slope * newx + intercept

    logger.info("We predict that when x = {newx}, y will be about {newy}")

    # Predictive: Machine Learning - Linear Regression
    # Use the slope and intercept and an unknown (future) x to predict a y value

    slope, intercept = statistics.linear_regression(xtimes_list, yvalues_list)
    logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")


def illustrate_list_built_in_functions():

    # Using the state sightings list provided above, do the following:
    # Calcuate the max and min sightings
    max_value = max(state_sightings_list)
    min_value = min(state_sightings_list)

    logger.info(f"Given state sightings list: {state_sightings_list}")
    logger.info(f"The max() is {max_value}")
    logger.info(f"The min() is {min_value}")

    # Calculate the length of the list
    len_list = len(state_sightings_list)
    logger.info(f"The len() is {len_list}")

    # Calculate the sum of the list
    sum_list = sum(state_sightings_list)
    logger.info(f"The sum() is {sum_list}")

    # Calculate the average of the list
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list}")

    logger.info(f"Given state sightings list: {state_sightings_list}")
    # Return a new list soreted in ascending order
    asc_sightings = sorted(state_sightings_list)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_sightings}")

    # Return a new list soreted in descending order
    desc_sightings = sorted(state_sightings_list, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_sightings}"
    )


def illustrate_list_methods():
    """This function illustrates methods that can be called on a list"""

    # append an item to the end of the list
    lst = [106, 6, 15]
    lst.append(17)

    # extend the list with another list
    lst.extend([17, 75, 43])

    # insert an item at a given position (0 = first item)
    i = 0
    newvalue = 9
    lst.insert(i, newvalue)

    # remove an item
    item_to_remove = 9
    lst.remove(item_to_remove)

    # Count how many times 22 appears in the list
    ct_of_22 = state_sightings_list.count(22)

    # Sort the list in ascending order using the sort() method
    asc_sightings2 = state_sightings_list.sort()

    # Sort the list in descending order using the sort() method
    desc_sightings2 = state_sightings_list.sort(reverse=True)

    # Copy the list to a new list
    new_sightings = state_sightings_list.copy()
    logger.info(f"new_sightings is: {new_sightings}")

    # Remove the first item from the new list
    # The first item in a list is at index 0
    first = new_sightings.pop(0)
    logger.info(
        f"Popped the first (index=0): {first} and now, new_sightings is: {new_sightings}"
    )

    # Remove the last item from the new list
    # The last item in a list is at index -1
    last = new_sightings.pop(-1)
    logger.info(
        f"Popped the last (index=-1): {last} and now, new_sightings is: {new_sightings}"
    )

    # Remove the item at index 3 from the new list
    fourth = new_sightings.pop(3)
    logger.info(
        f"Popped the fourth (index=3): {fourth} and now, new_sightings is: {new_sightings}"
    )


def illustrate_list_transformations():
    """This function illustrates transformations that can be applied to a list"""

    logger.info("state sightings list: {state_sightings_list}")

    # TRANFORMATIONS ............................

    # Use the built-in function filter() anywhere you need to filter a list
    # Filter the new list to only include sightings greater than 100
    sightings_over_100 = [filter(lambda x: x > 100, state_sightings_list)]
    logger.info(f"Sightings over 100: {sightings_over_100}")

    # Use the built-in function map() anywhere you need to transform a list

    # Map each element to its square
    doubled_sightings = [map(lambda x: x * 2, state_sightings_list)]
    logger.info(f"Doubled sightings: {doubled_sightings}")

    # Map each element to its square root
    sqrt_sightings = map(lambda x: math.sqrt(x), state_sightings_list)
    logger.info(f"Square root of sightings: {sqrt_sightings}")

    # Map each element (radius) to its area
    radius_list = [1, 2, 3, 4, 5]
    logger.info(f"Radius list: {radius_list}")
    # Say "map r to pi r squared" given radius_list
    area_list = [map(lambda r: math.pi * r * r, radius_list)]
    logger.info(f"Area of circles: {area_list}")


def illustrate_list_comprehensions():
    """This function illustrates list comprehensions"""

    logger.info("state sightings list: {state_sightings_list}")

    # TRANFORMATIONS - Using List Comprehensions

    # Filter the new list to only include sightings greater than 100

    sightings_over_100 = [x for x in state_sightings_list if x > 100]
    logger.info("Sightings over 100 (using list comprehensions!): {sightings_over_100}")

    # Try again "keep x (for each x in state_sightings_list) IF  x < 50"
    sightings_under_50 = [x for x in state_sightings_list if x < 50]
    logger.info("Sightings under 50 (using list comprehensions!): {sightings_under_50}")

    # Map each element to its square

    doubled_sightings = [x * 2 for x in state_sightings_list]
    logger.info("Doubled sightings (using list comprehensions!): {doubled_sightings}")

    # Map each element to its square root

    sqrt_sightings = [math.sqrt(x) for x in state_sightings_list]

    radius_list = [1, 2, 3, 4, 5]
    logger.info(f"Given radius_list: {radius_list}")

    # Map each element (radius) to its area

    area_list = [math.pi * r * r for r in radius_list]
    logger.info(f"Area of circles: {area_list}")

    # Map each element (radius) to its circumference

    circumference_list = [2 * math.pi * r for r in radius_list]
    logger.info(f"Circumference of circles: {circumference_list}")

    logger.info("Mastering comprehesions is a valuable skill for data scientists.")
    numbers = [1, 2, 3, 4]
    squares = [x**2 for x in numbers]
    logger.info(f"Given numbers: {numbers}")
    logger.info(f"Squares of numbers using [x ** 2 for x in numbers] is {squares}")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())
# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Replace this with calls to your functions." )



