#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 17:04:46 2018

@author: stephanosarampatzes
"""

from slang import slanger

slang_list = ['wassup lil bruh',
              'omg! dat shit lit',
              '1 luv fam, xo wit ma boi',
              'tbh, ma gal a bad bitch',
              's/o to my nigga, fly af',
              'no slang right here']

for word in slang_list:
    print(slanger(word))