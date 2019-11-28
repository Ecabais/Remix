from tkinter import *
from tkinter import messagebox
import turtle
import random

class GameMenu:
    def __init__(self):
        window = Tk()
        window.title("Learning Turtle")
        window.geometry("+{}+{}".format(0,200))
        window.geometry("700x630")
        window.resizable(False, False)
        window.configure(background = "black")
        
        frame1 = Frame(window)
        frame1.pack()
        
        #create a canvas
        #self.canvas1 = Canvas(frame1, bg = "white", width = 780, height = 480)
        #self.canvas1.pack()
        self.drawingCode = Text(window, width = 50, height = 30, font = 14)
        self.drawingCode.pack()

        self.currentDrawing = 1
        self.drawingList = ['rectangularprism','Triangle']
        self.getDrawing()

        turtle.screensize(780, 480)
        turtle.getscreen()
        

        frame2 = Frame(window)
        frame2.pack()
        hintBtn = Button(frame2, text = "Hint?", command = self.drawHint, bg = "orange")
        hintBtn.pack(side = LEFT)
        solutionBtn = Button(frame2, text = "Show Solution?", command = self.drawSolution, bg = "orange")
        solutionBtn.pack(pady = 3,padx = 6,side = LEFT)

        frameChoices = Frame(window)
        frameChoices.pack()
        
        Answer1Btn = Button(frameChoices, text = "Rectangular Prism", command = self.AnswerCheck, bg = "orange")
        Answer1Btn.pack(side = LEFT)

        
        


        window.mainloop()

    def drawHint(self):
        turtle.screensize(780, 480)
        turtle.getscreen()
        import rectangularprismHint
        
    def drawSolution(self):
        turtle.clear()
        turtle.reset()
        turtle.screensize(780, 480)
        import rectangularprism
        

    def getDrawing(self):
        filename = 'Drawings/' + self.drawingList[0] +'.txt'
        stringTxt = open(filename, 'r').read()
        self.drawingCode.insert(INSERT, stringTxt)

    def AnswerCheck(self):
        if (self.currentDrawing == 1):
            messagebox.showinfo("Correct", "You Guessed Correctly!")
        

GameMenu()
