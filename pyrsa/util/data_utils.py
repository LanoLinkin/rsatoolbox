#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Collection of helper methods for data module
    check_dict_length: check if each value in dict match length n
    extract_dict:      extract key-value pairs with values given indexes.
@author: baihan
"""

import numpy as np
import pyrsa as rsa

def check_dict_length(dictionary,n):
	for k,v in dictionary:
		if v.shape[0] != n:
			return False
	return True

def extract_dict(dictionary,indices):
	for k,v in dictionary:
		dictionary[k] = v[indices]
	return dictionary