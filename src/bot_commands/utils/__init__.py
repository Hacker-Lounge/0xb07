# -*- coding: utf-8 -*-


<<<<<<< HEAD
import functools

def join(separator=' '):
    def actual_decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            args = separator.join(args)
            return func(args)
        return wrapper
    return actual_decorator

@join(' ')
def func(args):
    print(args)
<<<<<<< HEAD

=======
>>>>>>> e07944bec96fd055c6437044309619e0acd82222
=======
>>>>>>> 1a9c2f2b660e61810915b4328220b97c57ce657e
