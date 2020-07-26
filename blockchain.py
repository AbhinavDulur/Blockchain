#!/usr/bin/python
# -*- coding: utf-8 -*-

from hashlib import sha256


#Using the sha256 package to create a "hash" for each block - or a unique string combination
def updatehash(*args):
    hashing_text = ""
    h = sha256()
    for arg in args:
        hashing_text = hashing_text + str(arg)

    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()




#The building block for each "block" in our blockchain
class Block():
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    #Each block has some data associated with it
    def __init__(self, data, number = 0):
        self.data = data
        self.number = number

    def hash(self):
        return updatehash(self.previous_hash,
                          self.number,
                          self.data,
                          self.nonce)

    #Making my object readable - this will print out if someone does str(Block()) or print(Block())
    def __str__(self):
        return str("Block: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n"
        %(self.number, self.hash(), self.previous_hash, self.data, self.nonce))






#The actual blockchain itself - this will be composed of basic building "blocks"
class Blockchain():
    difficulty = 4

    def __init__(self, chain = []):
        self.chain = chain

    def add(self, block):
        self.chain.append(block)

    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].hash()
        except IndexError:
            pass

        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block)
                break
            else:
                block.nonce = block.nonce + 1

    #This will test the validity of our blockchain, by chacking to make sure the hashes and previous hashes are valid
    def isValid(self):
        for i in range(1, len(self.chain)):
            previoushash = self.chain[i].previous_hash
            _currenthash = self.chain[i - 1].hash()
            if previoushash != _currenthash or _currenthash[0:self.difficulty] != '0' * self.difficulty:
                return False

        return True




def main():

    x = True

    while x == True:
        try:
           n = int(input("How many coins would you like? (< 20)"))
           if n > 0 and n <= 20 :
               x = False
           else:
               print("Please input a valid number.")
        except ValueError:
             print("Please input a valid number.")

    blockchain = Blockchain()

    database = []
    for i in range(n):
        database.append('Coin ' + str(i + 1))

    num = 0
    for data in database:
        num = num + 1
        blockchain.mine(Block(data, num))


    for block in blockchain.chain:
        print(block)

    if blockchain.isValid():
        print('Blockchain is valid')
    else:
        print('Blockchain is not valid')


if __name__ == '__main__':
    main()
