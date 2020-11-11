import time


def calculate_time(fn, parameter=None):
    start_time = time.time()
    fn(parameter)
    end_time = time.time()
    return end_time - start_time
