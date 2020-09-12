'''
Write a timer() decorator that validates if a function it decorates is executed
within (less than) a given seconds interval and returns
a boolean True or False accordingly.

'''

import time
from time import sleep

def timer(limit):
    def wrapper():
        pass
    
@timer(1)
def foo():
    sleep(0.1)

@timer(1)
def bar():
    sleep(1.1)


foo()
bar()

