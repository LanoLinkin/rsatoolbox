"""
saving to and reading from pickle files
"""
from __future__ import annotations
from typing import Union, Dict, IO
import pickle


def write_dict_pkl(fhandle: Union[str, IO], dictionary: Dict) -> None:
    """ writes a nested dictionary containing strings & arrays as data into
    a pickle file

    Args:
        file: a filename or opened writable file
        dictionary(dict): the dict to be saved

    """
    if isinstance(fhandle, str):
        fhandle = open(fhandle, 'wb')
    dictionary['rsatoolbox_version'] = '0.0.1'
    pickle.dump(dictionary, fhandle, protocol=-1)


def read_dict_pkl(fhandle: Union[str, IO]) -> Dict:
    """ writes a nested dictionary containing strings & arrays as data into
    a pickle file

    Args:
        file: a filename or opened readable file

    Returns:
        dictionary(dict): the loaded dict


    """
    if isinstance(fhandle, str):
        fhandle = open(fhandle, 'rb')
    data = pickle.load(fhandle)
    return data
