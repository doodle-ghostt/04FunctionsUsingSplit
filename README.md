* hms to seconds

1. `infix_calculator.py``

    You do not have to write functions for this exercise (although you can if you wish). Prompt the user once, for a mathematical expression they want to evaluate. Print the result of evaluating the mathematical expression. The user's expression should consist of a string starting with an integer, followed by a single space, followed by a mathematical operator out of "+", "-", "*", and "/", followed by a single space, followed by another integer. For example "14 - 11" is a valid expression.

1. `functions.py` - `meal_time`
    
    Write a function, `meal_time`, which takes one argument: a string representing the time in "military time". It should return either `"breakfast"`, `"lunch"`, `"dinner"`, or `"nothing right now"` depending on which meal it's appropriate to consume right now. Assume breakfast time is between 07:00 and 08:00 inclusive, lunch time is 12:00 - 13:00 inclusive, and dinner time is 18:00 - 19:00 inclusive.

    Demonstrate your function being used several times in a human readable format.

1. `functions.py` - `get_filename_extension`

    Computer files usually have an "extension", which are letters at the end of their name following a period. For example, "data.csv" has the "csv" extension, which implies it is a CSV (comma separated values) file. Write a function which takes one argument: a filename. The function should return a string representing the extension of the filename.

1. `functions.py` - `is_image_file`

    Write a function that takes a filename as input, and returns `True` if the filename represents an image file, and `False` otherwise. Assume that image files must have one of the following extensions: jpg, jpeg, png, gif, tiff