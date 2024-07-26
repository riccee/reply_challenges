import sys
from numpy import any
import time

sys.stdin = open("input.txt", "r")

# Creates an "Enemy" object, which has 5 inputs, id, health, x, y, and alive status
class Enemy:
    count = 0
    def __init__(self, id, he, x, y, alive):
        self.id = int(id)
        self.he = int(he)
        self.x = int(x)
        self.y = int(y)
        self.alive = bool(alive)

    def getHe(self):
        return self.he
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getAlive(self):
        return self.alive

    #method that moves each enemy object foward by 1
    def move(self, rows):
        if self.x == 0:
            self.x = rows-1
        else:
            self.x -= 1

    # Method that takes 3 argument, damage,range, and reduction, and applies the damage calcualted to the specified object
    def damage(self, damage, range, reduction):
        if (damage - (range * reduction)) <= 0:
            pass
        else:
            self.he -= (damage - (range * reduction))
            if self.he <= 0:
                self.he = 0
                self.alive=False

#Function that determines what enemy object to damage (using x coord), damages said objects, then moves all remaining enemies foward
def nextTurn():

    #this is an attempt to speed the for loops up
    getX = Enemy.getX
    getY = Enemy.getY
    getHe = Enemy.getHe
    move = Enemy.move

    for j in range(shots):
        #checks if any enemies are on the board
        check = [i.getAlive() for i in enemies]

        if True in check:
            #adds one to the shot count
            Enemy.count +=1

            #finds which enemy(s) are closest to x = 0 and stores in the list named "temp"
            temp = []
            iter = 0
            while len(temp) == 0:
                temp = [enemies[i] for i in range(numOfEnemies) if getX(enemies[i]) == iter and getHe(enemies[i]) >0]
                iter +=1

            #iterates over the temp list and applies damage on the closest row
            [i.damage(damage, getX(i), reduction) for i in temp]

    #moves all enemies foward 1
    for i in range(numOfEnemies):
        move(enemies[i], rows)

for testCase in range(int(input())):

    #sets all the inputs to their respective variables
    rows, cols, numOfEnemies, shots, damage, reduction = [int(i) for i in input().split()]
    enemies = []
    append = enemies.append

    # using the input, it appends new "enemy" objects to the enemies list
    for i in range(numOfEnemies):
        stats = input().split()
        append(Enemy(stats[0], stats[1], stats[2], stats[3], True))

    # runs the "nextTurn" function until there are no enemies on the board
    isAlive = [i.getAlive() for i in enemies]
    while True in isAlive:
        nextTurn()
        isAlive = [i.getAlive() for i in enemies]

    # open the output file and appends number of shots
    f = open("output.txt", "a")
    f.write("Case #" + str(testCase+1) + ": " + str(Enemy.count) + '\n')
    f.close()

    # resets the shot count
    Enemy.count = 0
