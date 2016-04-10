#! usr/bin/Python
#Python project that does a danish/english flash card game
#4/9/16
#Nova Hackathon 2016
# -*- coding: utf-8 -*-

import os, random, codecs, pygame

pygame.init()

count = 0
score = 0

fileE = open('english.txt','r')
fileD = codecs.open('danish.txt', 'r','utf-8')

FEcontent = fileE.readlines()
FDcontent = fileD.readlines()

print "ENGELSK TIL DANSK FLASHCARD SPIL"
print "ENGLISH TO DANISH FLASHCARD GAME"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

print "This is a flashcard game. After 5 failures you lose. Good luck!!"
print "Dette er et flashcard spil. Efter fem fejl mister du. Godt lykke!!\n"

while count < 5:
    os.system('cls')

    wordnum = random.randint(0, len(FEcontent)-1)

    print 'Word:', FEcontent[wordnum], ''

    options = [random.randint(0, len(FDcontent)-1),
        random.randint(0, len(FDcontent)-1),
        random.randint(0, len(FDcontent)-1)]

    options[random.randint(0, 2)] = wordnum

    print '1 -', FDcontent[options[0]],
    print '2 -', FDcontent[options[1]],
    print '3 -', FDcontent[options[2]],
    answer = input('\nPlease input your choice: ')

    if options[answer-1] == wordnum:
        raw_input('Correct!^_^ Please hit enter...')
        score = score + 1
    else:
        raw_input('Wrong!!;_; Please hit enter...')
        count = count + 1

print '\nYour score is:', score