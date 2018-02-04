import functools
import inspect


def arg_pairs(arg_names, args, kwargs):
    yield from zip(arg_names, args)
    yield from kwargs.items()
        

def pretty_function_name(f):
    return f.__name__


def print_function_name(func):
    func_name = pretty_function_name(func)
    print(func_name)
    print('=' * len(func_name))
     
 
def print_args(kwargs):
    for name, value in kwargs.items():
        print(name)
        print('-' * len(name))
        print(value)
        
    
def print_debug_info(func):
    arg_names = inspect.getfullargspec(func)[0]
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pairs = arg_pairs(arg_names, args, kwargs)
        
        print()
        print_function_name(func)
        print_args(dict(pairs))
        
        result = func(*args, **kwargs)
        
        print()
        print_args({'Result ({})'.format(pretty_function_name(func)): result})
        print()
        
        return result
    
    return wrapper
        
        