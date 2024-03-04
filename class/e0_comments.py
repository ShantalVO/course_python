a = 5  # (inline comment) this is an instance of an object
"""
This is a block comment
We can add a lot of lines
"""

def f(x):
    """
    This is a docstring
    A docstring explains what a function docs
    :param x:
    :return:
    """
    return x * x  # Returns the square of x


for item in 'python':
    # An indented comment
    if item == 'p':
        # Another indetented comment
        print('Found!')
