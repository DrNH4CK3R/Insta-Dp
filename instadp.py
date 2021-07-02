
import sys
import os
import time
import instaloader

os.system("clear")

os.system("figlet Insta-Dp ")
print('                         ')
print(' Author: DrNH4CK3R       ')
print('                         ')
print('---  ---  ---  ---  ---  ')



dp = instaloader.Instaloader()

acc = input('Enter the Account Username: ')

print('                                   ')
print('Searching for the given Username...')
time.sleep(3)
print('                                   ')
print('Fetching details...                ')
time.sleep(3)
print('                                   ')

dp.download_profile(acc, profile_pic_only = True)
