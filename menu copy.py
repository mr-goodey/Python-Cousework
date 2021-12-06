import sys
sys.path.append("Coursework")
from booksearch import *
from bookcheckout import *
from bookreturn import *
from bookrecommend import *

def menu():
    """This provides a user interface"""
    print("Welcome!")
    repeat=True
    while repeat==True:
        request=int(input("What would you like to do?\n\
1 - search\n\
2 - checkout\n\
3 - return\n\
4 - recommend\n\
5 - quit\n"))
        if request==1:
            booksearch()
        elif request==2:
            bookcheckout()
        elif request==3:
            bookreturn()
        elif request==4:
            bookrecommend()
        elif request==5:
            print("Goodbye")
            repeat=False
        else:
            print("Error")

'''
menu()
'''
#Tests for previous functions
