#!/usr/bin/env python3.7

# Functional Programming

def call_functional_prg():

    def call_func(func, *args):
        print(f'Calling Function')
        func(*args)
        print(f'Ending Function')
        

    def print_func(*args):
        print(args)    
            
    call_func(print_func, 'Hello, World') 


# Pure Functions

def call_purefunctions():

    def pure_func(x, y):
        return x + y
        
    print(pure_func(7, 8))


# Impure Functions

def call_impurefunctions():

    def impure_func(list_val, value):
        list_val.append(value)

    list_val = list(range(10))
    impure_func(list_val, 20)
    print(list_val)

# Lambda Functions

def call_lambdas():

    # Map Example
    list_val = list(range(20))

    print(f'Input: {list_val}')

    result = list(map(lambda x: x*2, list_val))
    
    print(f'Result: {result}')

    # Filter Example

    result = list(filter(lambda x: x < 10, list_val))

    print(f'Result: {result}')


# Generators

def call_generators():

    def my_range(*args):

        """
            Functional Implementation of In-Built range function
            
            Arguments:
                
                start = starting point 
                stop = ending point
                step = adding steps to my_range
        """

        num_of_args = len(args)
            
        if num_of_args > 3:
            raise TypeError(f'my_range expected at most 3 arguments, got {len(args)}')
        elif num_of_args <= 0:
            raise TypeError(f'my_range expected 1 arguments, got 0')

        start, stop, step = 0, 0, 1
        
        if num_of_args == 1:
            stop = args
        elif num_of_args == 2:
            start, stop = args
            if start < 0 and stop < 0:
                return None
            elif start > stop:
                return None
        else:
            start, stop, step = args
            
        while start < stop:
            yield start
            start += step


    for index in my_range(2, 12, 2):
        print(index)


# Decorators

def call_decorators():

    def message(msg):
        print(f'func-start: message')
        def decor(func):
            print(f'func-start: decor')
            def wrapper(*args):
                print(f'{msg} : Start')
                func(*args)
                print(f'{msg} : End')
            return wrapper
        return decor

    def decor2(func):
        print(f'func-start: decor2')
        def wrapper2(*args):
            print(f'func-start: wrapper2')
            func(*args)
            print(f'func-end: wrapper2')
        return wrapper2

    @message('TESTING')
    @decor2
    def print_args(*args):
        for i in args:
            print(i)

    # Replecating @decor

    # afunc = decor(print_args)
    # afunc('Hello', 'World', 'Check', 'Mate')
   
    # Replecating @message('TESTING')

    # afunc = message('TESTING')
    # afunc = afunc(print_args)
    # afunc('Hello', 'World', 'Check', 'Mate')

    # Replicating @message('TESTING') and @decor2

    # afunc = message('TESTING')
    # afunc = afunc(decor2(print_args))
    # afunc('Hello', 'World', 'Check', 'Mate')

    print_args('Hello', 'World', 'Check', 'Mate')


if __name__ == '__main__':
    
    # Function Programming
    # call_functional_prg()
    
    # Pure Functions
    # call_purefunctions()   

    # Impure Functions
    # call_impurefunctions()
    
    # Lambda Functions
    # call_lambdas()

    # Generators
    # call_generators()

    # Decorators
    call_decorators()

