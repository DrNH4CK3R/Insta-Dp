
import sys
import os
import time
import instaloader

os.system("clear")

TITLE="""
 ___           _              ____        
|_ _|_ __  ___| |_ __ _      |  _ \\ _ __  
 | || '_ \\/ __| __/ _` |_____| | | | '_ \\ 
 | || | | \\__ \\ || (_| |_____| |_| | |_) |
|___|_| |_|___/\\__\\__,_|     |____/| .__/ 
                                   |_|    
"""
print(TITLE)
print('                         ')
print(' Author: DrNH4CK3R       ')
print('                         ')
print('---  ---  ---  ---  ---  ')



dp = instaloader.Instaloader()

acc = input('Enter the Account Username: ')

print('                                   ')
print('Searching for the given Username {}'.format(acc))
time.sleep(3)
print('                                   ')
print('Fetching details...                ')
time.sleep(3)
print('                                   ')

dp.download_profile(acc, profile_pic_only = True)
