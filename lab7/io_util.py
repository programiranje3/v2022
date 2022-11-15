"""

Common Input/Output (IO) functions

"""

from pathlib import Path
# A handy tutorial for the pathlib.Path class: https://www.pythontutorial.net/python-standard-library/python-path/

from sys import stderr
import pickle
import json


def get_data_dir():
    data_dir = Path.cwd() / 'data'
    if not data_dir.exists():
        data_dir.mkdir()
    return data_dir


def get_results_dir():
    results_dir = Path.cwd() / 'results'
    results_dir.mkdir(exist_ok=True)
    return results_dir


def write_to_txt_file(*text, fpath):
    try:
        with open(fpath, 'w') as fobj:
            for line in text:
                fobj.write(line + "\n")
    except OSError as err:
        stderr.write(f"Error {type(OSError)} when trying to write to txt file {fpath.name}\n:{err}\n")


def read_from_txt_file(fpath):
    try:
        with open(fpath, "r") as fobj:
            return [line.rstrip('\n') for line in fobj.readlines()]
    except FileNotFoundError as err:
        stderr.write(f"Error: {err}\n")
    except OSError as err:
        stderr.write(f"Error {type(OSError)} occurred when trying to read data from txt file {fpath.name}:\n{err}\n")


def serialise_to_file(obj, fpath):
    try:
        with open(fpath, 'wb') as fobj:
            pickle.dump(obj, fobj)
    except pickle.PicklingError as perr:
        stderr.write(f"Pickling error when trying to serialise object to {fpath.name} file\n:{perr}\n")
    except OSError as err:
        stderr.write(f"Error when serialising object to {fpath.name} file\n:{err}\n")


def unpickle_from_file(fpath):
    try:
        with open(fpath, 'rb') as fobj:
            return pickle.load(fobj)
    except pickle.UnpicklingError as perr:
        stderr.write(f"Error when unpickling object from file {fpath.name}:\n{perr}\n")
    except OSError as err:
        stderr.write(f"Error ({type(OSError)}) in the 'unpickle_from_file' function: {err}\n")


def write_to_json(obj, fpath):
    try:
        with open(fpath, 'w') as fobj:
            json.dump(obj, fobj, indent=4)
    except OSError as err:
        stderr.write(f"Error ({type(OSError)}) when trying to serialise data to json:\n{err}\n")


def read_from_json(fpath):
    try:
        with open(fpath, 'r') as fobj:
            return json.load(fobj)
    except OSError as err:
        stderr.write(f"Error ({type(err)}) occurred when trying to restore obj from JSON file {fpath.name}:{err}")
