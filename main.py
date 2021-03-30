# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import instaloader
import difflib
import os
from time import sleep

#Login
instaLoad = instaloader.Instaloader()
username = 'xxxx' #username
password = 'xxx' #password
instaLoad.login(username, password)
profile = instaloader.Profile.from_username(instaLoad.context, 'xxxx')

def download_data(save_path):
    followers_list = []
    count = 0
    for follower in profile.get_followers():
        followers_list.append(follower.username)
        file = open(save_path, 'a+')
        file.write(followers_list[count])
        file.write("\n")
        file.close()
        count = count + 1

def update_backup(usr):
    os.remove(str(usr) + ' – followers_BACKUP.txt')
    sleep(1)
    os.rename(str(usr) + ' – followers.txt', str(usr) + ' – followers_BACKUP.txt')

try:
    #Controllo se c'è un backup
    backup = open(str(username) + ' – followers_BACKUP.txt', 'r').readlines()
    print('File backup presente')

    #Ottengo i dati riguardo i followers
    download_data(str(username) + ' – followers.txt')

    #Compariamo i due testi
    print('Comparo...')

    file = open(username + ' – followers.txt', 'r').readlines()

    for line in difflib.unified_diff(backup, file):
        if line[0] == '-' and line[1] != '-':
            print(line[1:len(line) - 1] + ' – UNFOLLOW' )

    remove_bck = int(input('Vuoi aggiornare il backup?'))
    if remove_bck == 0:
        update_backup(username)
        print('Ho aggiornato il file')
    elif remove_bck == 1:
        os.remove(username + ' – followers.txt')
        print('Non ho eseguito alcune operazione')

except:
    print('File backup non presente')
    download_data(str(username) + ' – followers_BACKUP.txt')


