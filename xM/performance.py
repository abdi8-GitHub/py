from time import time
def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Took {t2 - t1} seconds')
        return result
    return wrapper