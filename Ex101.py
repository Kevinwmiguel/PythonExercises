"""
Ex 101 - Create python code that tests whether the pudding site is accessible from the computer used.
"""

import requests as rq

try:
    rq.get('https://www.cursoemvideo.com')
except:
    print('\033[31mThe site is inaccessible\033[m')
else:
    print('\033[32mThe site is accessible\033[m')

input('Enter to exit')
