import csv
from pathlib import Path
import functools
from sys import stderr
from datetime import datetime
from time import perf_counter


def write_to_csv(fpath, logged_data):
    try:
        new_file = not fpath.exists()
        with open(fpath, 'a') as fobj:
            csv_writer = csv.writer(fobj)
            if new_file:
                csv_writer.writerow(('func_call_dt', 'execution_time', 'func_call'))
            csv_writer.writerow(logged_data)
    except OSError as err:
        stderr.write(f"ERROR from execution logger\n:{err}\n")


def execution_logger(func):
    @functools.wraps(func)
    def wrapper_execution_logger(*args, **kwargs):

        start_dt = datetime.now()
        start_time = perf_counter()

        value = func(*args, **kwargs)

        exec_time_ms = (perf_counter() - start_time)*1000

        func_name = func.__name__ + "("
        if args:
            func_name += ",".join([str(a) for a in args])
        if kwargs:
            func_name += ",".join([f"{arg_name}={arg_val}" for arg_name, arg_val in kwargs.items()])
        func_name += ")"

        write_to_csv(Path.cwd() / 'execution_log.csv', (start_dt, exec_time_ms, func_name))

        return value

    return wrapper_execution_logger
