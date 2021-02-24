import functools
from time import time

def wrapper(func):
    """Template for decorators"""

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        """The wrapper function replacing the original"""
        # Do something before calling the function
        value = func(*args, **kwargs)
        # Do something after calling the function
        return value

    return _wrapper

def timer(func):
    """Template for decorators"""

    @functools.wraps(func)
    def _timer(*args, **kwargs):
        """The wrapper function replacing the original"""
        # Do something before calling the function
        bgn_time = time()
        value = func(*args, **kwargs)
        elpsed_time = time() - bgn_time
        print("Elapsed time: " + format(elpsed_time, '.2f'))
        return value
    return _timer

def trace(func):
    """Template for decorators"""

    @functools.wraps(func)
    def _trace(*args, **kwargs):
        params = ''
        for item in args:
            if item == args[-1]:
                params += f"'{str(item)}'"
            else:
                params += f"'{str(item)}'" + ","
        for key,value in kwargs.items():
            if key == list(kwargs.keys())[-1]:
                params += f", {str(key)}='{value}'"
            else:
                params += f", '{str(key)}={value}'" + ","

        """The wrapper function replacing the original"""
        print(f"Calling {func.__name__}({params})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}({params}) returned {value}")
        return value

    return _trace