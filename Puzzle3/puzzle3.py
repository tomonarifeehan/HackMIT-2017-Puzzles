import requests
from random_words import RandomWords
from random_words import RandomNicknames
import random
import sys
import subprocess
import time
import csv
 
url = "https://the.delorean.codes/api/decode"
alphabet ="etaoinshrdlcumwfgypbvkjxqz"
 
rw = RandomWords()
found_words = ["back", "to", "the", "future", "produced", "by", "bob", "gale", "neil", "canton", "screenplay", "robert", "zemeckis", "directed", "transcribed", "eric", "dienstfrey", "radio", "is", "inventory", "time", "so", "right", "now", "statler", "toyota"]
 
def words():
    while True:
        input = "is " + rw.random_word()
        resp = requests.post(url, data={"username":"tomonarifeehan", "codeword": input}).json()
        print("Input: " + input)
        print(resp["message"])
        print(resp["well_formed"])
        print("\n\n")
 
        if resp["message"] != None and resp["message"] == "th":
            return
 
def csv_boiii():
    with open('script.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            temp = ', '.join(row)
            tempArr = temp.split(",")
            newArr = []
            for item in tempArr:
                if item != '':
                    newArr.append(item)
            for item in newArr:
                input = "is a missing can " + item
                resp = requests.post(url, data={"username":"tomonarifeehan", "codeword": input}).json()
                print("Input: " + input)
                print(resp["message"])
                print(resp["well_formed"])
                print("\n\n")
                if resp["message"] != None and resp["message"] == "the w":
                    return
csv_boiii()