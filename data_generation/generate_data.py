from os import path
from random import randint
from sys import argv
from cv2 import imread, resize, cvtColor, COLOR_BGR2GRAY
import numpy as np

class Row():
    def __init__(self, scale: int):
        self.rowImage = np.zeros((248,scale))
        self.text = ''
        self.genRow(scale)

    def genRow(self, scale: int):
        length = randint(5,20)
        for i in range(length):
            self.genElement(i, scale)
    
    def genElement(self, i: int, scale: int):
        #Length of text in row
        nr = randint(0,30)
        if nr >= 20:  #First 20 digits are number. After that there are functions and more integers are needed to be generated
            nr2 = randint(0,19)
            if nr <= 23: #For these cases an additional integer needs to be generated
                nr3 = randint(0,19)
                if nr == 20:
                    row_text += F"\frac{{ {nr2} }}{{ {nr3} }}"
                if nr == 21:
                    row_text += F"{nr2}^{{ {nr3} }}"
                if nr == 22:
                    row_text += F"{nr2}_{{ {nr3} }}"
                if nr == 23:
                    row_text += F"\sqrt[{nr3}]{{ {nr2} }}"
            else:
                if nr == 24:
                    row_text += F"\sin{{ {nr2} }}"
                elif nr == 25:
                    row_text += F"\cos{{ {nr2} }}"
                elif nr == 26:
                    row_text += F"\tan{{ {nr2} }}"
                elif nr == 27:
                    row_text += F"d({nr2},{nr3})"
        else:
            text += str(nr)
            offset = randint(-2,2)
            img = cvtColor(imread(path + str(nr) + ".png"), COLOR_BGR2GRAY)
            self.rowImage[2+offset:(-3+offset),scale] = resize(img, (scale+offset,scale+offset))

        
        #Used for splitting the text later when image is generated.
        text += ";"


# A class for randomly generated image
class Example():
    def __init__(self, exampleNr: int, storeTex: False): #By default does not save .tex file which was used to create .pdf file
        self.rows = []
        self.exampleImage = np.zeros((248,350))
        self.generateText()
        self.text2Pdf(exampleNr, storeTex) #Creates pdf file from generated text and saves it.
        self.createImage(exampleNr) #Creates .png file from generated text and saves it.

    #Generates random mathematical text.
    def generateText(self) -> str:
        #Random amount of rows of mathematical text. From 1 to 10.
        nrows = randint(1,10)
        #Scale parameters determines the image size of text. scale = 15 gives the smallest font text and scale = 30 gives the biggest font text.
        scale = randint(15,30)
        #Store the rows in list.
        for i in range(nrows):
            row = Row(scale)
            self.rows.append(row)


    #Turns LaTex code to image.
    def text2Pdf(self, exampleNr):
        #TODO
        #Create .tex file.

        #Run .tex file in MikTex to convert it to image.
        #Delete .tex file.
        a = 0

    def createImage(self):
        return None

#Argv[0] is amount of examples that will be generated.
#Argv[1] (default False) is an optional parameter to specify whether the .tex file will be saved.
def main():
    if len(argv) == 2:
        for i in range(argv[0]):
            example = Example(i, argv[1])
    else:
        for i in range(argv[0]):
            example = Example(i)
        

