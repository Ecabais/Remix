from tkinter import *
from tkinter import messagebox
import turtle
#import time
import random

class GameMenu:
    def __init__(self):
        window = Tk()
        window.title("Learning Turtle")
        window.geometry("+{}+{}".format(300,100))
        window.geometry("1100x735")
        window.resizable(False, False)
        window.configure(background = "dodger blue")
        
        menubar = Menu(window)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label = "Help", command = self.helpwindow)
        menubar.add_cascade(label="Help", menu = filemenu)


        window.config(menu=menubar)

        #Gaming Points
        self.PlayerPoints = 0
        self.WinScore = 500
        

        #Text boxes labels
        playerFrame = Frame(window, width = 30, height = 20)
        playerFrame.pack(side = TOP)
        Topframelbl = Frame(window, width = 30, height = 20)
        Topframelbl.pack(side = TOP)
        playerlbl = Label(playerFrame, bg = "#51a9ff", width = 20, height = 2, text = "Your Total Points:",font =('Helvetica 15 bold'))
        playerlbl.pack(side = LEFT)

        
        
        self.PlayerTotal = Text(playerFrame, width = 5, height = 1, font =('Helvetica 18 bold'))
        self.PlayerTotal.pack(side = RIGHT)
        self.PlayerTotal.config(state = DISABLED)

        self.playerPointUpdate()
        
        TextFramelbl = Label(Topframelbl, bg = "gold", width = 27, height = 2, text = "Code", font = ('Helvetica 12 bold'))
        TextFramelbl.pack(side = LEFT, padx = 5)
        TextFramelbl2 = Label(Topframelbl, bg = "gold", width = 25, height = 2, text = "Hint Code", font = ('Helvetica 12 bold'))
        TextFramelbl2.pack(side = LEFT, padx = 5)
        TextFramelbl2 = Label(Topframelbl, bg = "gold", width = 48, height = 2, text = "Turtle Window", font = ('Helvetica 12 bold'))
        TextFramelbl2.pack(side = RIGHT, padx = 5)

        

        #window boxes for the text code
        TextFrame = Frame(window)
        TextFrame.pack()
        
        frame1 = Frame(window)
        frame1.pack(side = RIGHT)
        
        
        
        self.drawingCode = Text(TextFrame, width = 30, height = 30, font = 14)
        self.drawingCode.config(state = DISABLED)
        self.drawingCode.pack(side = LEFT)
        
        self.drawingCodehint = Text(TextFrame, width = 30, height = 30, font = 14)
        self.drawingCodehint.config(state = DISABLED)
        self.drawingCodehint.pack(side = LEFT)

        #create a canvas
        self.canvas1 = Canvas(TextFrame, bg = "white", width = 480, height = 280)
        self.canvas1.pack(side = RIGHT)
        #--------sketch
        frameSketch = Frame(window)
        frameSketch.pack(side = RIGHT, pady = 5)

        sketchlbl = Label(frameSketch, text = "Need to Sketch?", bg = "#51a9ff", font = ('Helvetica 14 bold'))
        sketchlbl.pack(side = TOP)
        self.sketchBtn = Button(frameSketch, text = "Sketch!", bg = "gold", command = self.Sketchwindow, width = 15, height = 2, font = ('Helvetica 12 bold'))
        self.sketchBtn.pack()

        ##################
        

        #list of shapes
        random.randint(1,4)
        self.currentDrawing = random.randint(0,3)
        self.drawingList = ['rectangle','triangle','square','hexagon']
        self.getDrawing()


        TurtleFrame = Frame(window)
        TurtleFrame.pack(side = RIGHT)
        self.t = turtle.RawTurtle(self.canvas1)

        

        frame2 = Frame(window)
        frame2.pack(side = RIGHT)
        self.hintBtn = Button(frame2, text = "Hint?", command = self.drawHint, bg = "gold", font = ('Helvetica 10 bold'))
        self.hintBtn.pack(side = LEFT)
        self.solutionBtn = Button(frame2, text = "Show Solution?", command = self.drawSolution, bg = "gold", font = ('Helvetica 10 bold'))
        self.solutionBtn.pack(pady = 3,padx = 6,side = LEFT)


#--------Answer Choices frame

        frameChoiceslbl = Frame(window)
        frameChoiceslbl.pack()

        AnswerChoicelbl = Label(frameChoiceslbl, text = "Guess which shape will be drawn!",font = ('Helvetica 20 bold'),bg = "#51a9ff")
        AnswerChoicelbl.pack()
        
        frameChoices = Frame(window)
        frameChoices.pack(side = BOTTOM)
        self.Answer1Btn = Button(frameChoices, text = "Rectangle", command = self.AnswerCheck1, bg = "gold",width = 10, height = 2, font = ('Helvetica 10 bold'))
        self.Answer1Btn.pack(side = LEFT,padx = 1)
        self.Answer2Btn = Button(frameChoices, text = "Triangle", command = self.AnswerCheck2, bg = "gold",width = 10, height = 2, font = ('Helvetica 10 bold'))
        self.Answer2Btn.pack(side = LEFT,padx = 3)
        self.Answer3Btn = Button(frameChoices, text = "Square", command = self.AnswerCheck3, bg = "gold",width = 10, height = 2, font = ('Helvetica 10 bold'))
        self.Answer3Btn.pack(side = LEFT,padx = 3)
        self.Answer4Btn = Button(frameChoices, text = "Hexagon", command = self.AnswerCheck4, bg = "gold",width = 10, height = 2, font = ('Helvetica 10 bold'))
        self.Answer4Btn.pack(side = LEFT,padx = 1)
        


        window.mainloop()
#---------help menu
    def helpwindow(self):
        window = Tk()
        window.title("Help Window")
        window.resizable(False, False)


        self.helptext = Text(window, width = 70, height = 12, font = 14)
        self.helptext.pack(side = LEFT)

        self.helptext.delete('1.0',END)
        filename = 'help.txt'
        stringhelpTxt = open(filename, 'r').read()
        self.helptext.insert(INSERT, stringhelpTxt)
        self.helptext.config(state = DISABLED)

        window.mainloop()
#-------------------------Sketch window-----------------------
    def Sketchwindow(self):
        window = Tk()
        window.title("Sketch Window")
        self.canvas2 = Canvas(window, bg = "white", width = 480, height = 280)
        self.canvas2.pack()
        window.resizable(False, False)
        
 #----create new turtle
        TurtleFrame = Frame(window)
        TurtleFrame.pack(side = RIGHT)
        self.t2 = turtle.RawTurtle(self.canvas2)

        self.turnAngle = 0
        self.advance = 0
        self.ang = 0
        self.angdis = 0
        self.adv50 = 0
        self.adv5 = 0
        self.MoveR = 0
        self.MoveL=0
        self.undocount = 0

        self.movint = 10
        self.moveloc = 0

        self.t2.speed(2)
        self.t2.color("#51a9ff")
        self.t2.width(3)
 #-----------
        
        frameangle = Frame(window)
        frameangle.pack()
        
        Turnlbl = Label(frameangle, text = "Current angle: ")
        Turnlbl.pack(side = LEFT)
        
        #self.getVar = StringVar()
        self.Textbx = Text(frameangle, width = 4, height = 1)
        self.Textbx.config(state = DISABLED)
        self.Textbx.pack(side =LEFT)
        
        goBtn = Button(frameangle,text = "Turn left 10 degrees",command = self.moveAngleLeft)
        goBtn.pack(side = LEFT)
        gobackBtn = Button(frameangle,text = "Turn right 10 degrees",command = self.moveAngleRight)
        gobackBtn.pack(side = LEFT)


        framemove = Frame(window)
        framemove.pack(pady = 5)

        Movelbl = Label(framemove, text = "Move: ")
        Movelbl.pack(side = LEFT)

        self.Textbx2 = Text(framemove, width = 4, height = 1)
        self.Textbx2.config(state = DISABLED)
        self.Textbx2.pack(side =LEFT)
        goBtn5 = Button(framemove,text = "Move Forward 5",command = self.advanceMove5)
        goBtn5.pack(side = LEFT)
        goBtn50 = Button(framemove,text = "Move Forward 50",command = self.advanceMove50)
        goBtn50.pack(side = LEFT)

        undoBtn = Button(window, text = "undo", command = self.undoFunction)
        undoBtn.pack(padx = 10)
        
        clearBtn = Button(window, text = "Clear", command = self.cleart2)
        clearBtn.pack(padx = 10)
        
        

        window.mainloop()
        
        
    def moveAngleRight(self):
        self.undocount += 1
        self.adv50 = 0
        self.adv5 = 0
        self.MoveR = 1
        self.MoveL=0
        self.clearMove()
        self.ang = 10
        self.angdis += self.ang
        self.rightAngle()
        
    def moveAngleLeft(self):
        self.undocount += 1
        self.adv50 = 0
        self.adv5 = 0
        self.MoveR = 0
        self.MoveL=1
        self.clearMove()
        self.ang = 10
        self.angdis -= self.ang
        self.addAngle()

    def rightAngle(self):
        self.t2.right(self.ang)
        self.updateAngleText()
        
    def addAngle(self):
        self.t2.left(self.ang)
        self.updateAngleText()


    def updateAngleText(self):
        self.Textbx.config(state = NORMAL)
        self.Textbx.delete('1.0',END)
        stringangle = str(abs(self.angdis))
        self.Textbx.insert(INSERT, stringangle)
        self.Textbx.config(state = DISABLED)


    def clearAngle(self):
        self.angdis = 0
        self.updateAngleText()        

    def advanceMove5(self):
        self.undocount += 1
        self.adv50 = 0
        self.adv5 = 1
        self.MoveR = 0
        self.MoveL=0
        self.clearAngle()
        self.movint = 5
        self.moveloc += self.movint
        self.addMove()
        
    def advanceMove50(self):
        self.undocount += 1
        self.adv50 = 1
        #if(self.adv50>0):
            
        self.adv5 = 0
        self.MoveR = 0
        self.MoveL=0
        self.clearAngle()
        self.movint = 50
        self.moveloc += self.movint
        self.addMove()


    def addMove(self):
        self.t2.forward(self.movint)
        self.updateMoveText()
        
    def clearMove(self):
        self.moveloc = 0
        self.updateMoveText()

    def updateMoveText(self):
        self.Textbx2.config(state = NORMAL)
        self.Textbx2.delete('1.0',END)
        stringloc = str(self.moveloc)
        self.Textbx2.insert(INSERT, stringloc)
        self.Textbx2.config(state = DISABLED)

    
    def cleart2(self):
        self.undocount = 0
        self.clearMove()
        self.clearAngle()
        self.t2.clear()
        self.t2.reset()
        self.t2.speed(2)
        self.t2.color("#51a9ff")
        self.t2.width(3)
        self.updateAngleText()

    def undoFunction(self):
        if(self.undocount> 0):
            if(self.adv50 == 1):
                self.moveloc -= self.movint
                self.updateMoveText()
            elif(self.adv5 == 1):
                self.moveloc -= self.movint
                self.updateMoveText()
            elif(self.MoveR == 1):
                self.angdis -= self.ang
                self.updateAngleText()
            elif(self.MoveL == 1):
                self.angdis += self.ang
                self.updateAngleText()
            self.t2.undo()
            self.undocount -= 1

  #-------------------------end of sketch

    def playerPointUpdate(self):
        if(self.WinScore == self.PlayerPoints):
            self.PlayerTotal.config(state = NORMAL)
            self.PlayerTotal.delete('1.0',END)
            playerTot = str(self.PlayerPoints)
            self.PlayerTotal.insert(INSERT, playerTot)
            self.PlayerTotal.config(state = DISABLED)
            messageanswer = messagebox.askyesno("YOU WON!", "CONGRATULATIONS YOU WON!!\n Do you want to restart?")
            if(messageanswer == YES):
                self.PlayerPoints = 0
                self.playerPointUpdate()
        else:
            self.PlayerTotal.config(state = NORMAL)
            self.PlayerTotal.delete('1.0',END)
            playerTot = str(self.PlayerPoints)
            self.PlayerTotal.insert(INSERT, playerTot)
            self.PlayerTotal.config(state = DISABLED)
        if(700 == self.PlayerPoints):
            self.PlayerTotal.config(state = NORMAL)
            self.PlayerTotal.delete('1.0',END)
            playerTot = str(self.PlayerPoints)
            self.PlayerTotal.insert(INSERT, playerTot)
            self.PlayerTotal.config(state = DISABLED)
            messageanswer = messagebox.askyesno("YOU WON!", "CONGRATULATIONS you are now eligible for a refund!\n Go get your refund?")
            if(messageanswer == YES):
                messageanswer = messagebox.askyesno("Refund Completed","You have been refunded!\n Do you want to restart?")
                if(messageanswer == YES):
                    self.PlayerPoints = 0
                    self.playerPointUpdate()
            

    def drawHint(self):
        self.disableBtns()
        self.drawingCodehint.config(state = NORMAL)
        self.t.clear()
        self.t.reset()
        self.getDrawingHint()
        if (self.currentDrawing == 0):
            self.rectanglehint()
        elif(self.currentDrawing == 1):
            self.trianglehint()
        elif(self.currentDrawing == 2):
            self.squarehint()
        elif(self.currentDrawing == 3):
            self.hexagonhint()
        self.drawingCodehint.config(state = DISABLED)
        self.enableBtns()
        
    def drawSolution(self):
        self.disableBtns()
        self.t.clear()
        self.t.reset()
        if (self.currentDrawing == 0):
            self.rectangle()
        elif(self.currentDrawing == 1):
            self.triangle()
        elif(self.currentDrawing == 2):
            self.square()
        elif(self.currentDrawing == 3):
            self.hexagon()
        messagebox.showinfo("Continue?", "Click OK to continue!")
        self.drawingCode.config(state = NORMAL)
        self.drawingCodehint.config(state = NORMAL)
        self.drawingCode.delete('1.0',END)
        self.drawingCodehint.delete('1.0',END)
        self.drawingCode.config(state = DISABLED)
        self.drawingCodehint.config(state = DISABLED)
        self.t.clear()
        self.t.reset()
        random.randint(1,4)
        self.currentDrawing = random.randint(0,3)
        self.drawingList = ['rectangle','triangle','square','hexagon']
        self.getDrawing()
        self.enableBtns()



    def getDrawing(self):
        self.drawingCode.config(state = NORMAL)
        filename = 'Drawings/' + self.drawingList[self.currentDrawing] +'.txt'
        stringTxt = open(filename, 'r').read()
        self.drawingCode.insert(INSERT, stringTxt)
        self.drawingCode.config(state = DISABLED)
        

    def AnswerCheck1(self):
        if (self.currentDrawing == 0):
            messagebox.showinfo("Correct", "You Guessed Correctly!")
            self.PlayerPoints += 100
            self.playerPointUpdate()
            self.drawingCode.config(state = NORMAL)
            self.drawingCodehint.config(state = NORMAL)
            self.drawingCode.delete('1.0',END)
            self.drawingCodehint.delete('1.0',END)
            self.drawingCode.config(state = DISABLED)
            self.drawingCodehint.config(state = DISABLED)            
            self.t.clear()
            self.t.reset()
            random.randint(1,4)
            self.currentDrawing = random.randint(0,3)
            self.drawingList = ['rectangle','triangle','square','hexagon']
            self.getDrawing()
            
        else:
            messagebox.showinfo("Incorrect", "Sorry! That's incorrect.")
            self.PlayerPoints -= 100
            self.playerPointUpdate()


    def AnswerCheck2(self):
        if (self.currentDrawing == 1):
            messagebox.showinfo("Correct", "You Guessed Correctly!")
            self.PlayerPoints += 100
            self.playerPointUpdate()
            self.drawingCode.config(state = NORMAL)
            self.drawingCodehint.config(state = NORMAL)
            self.drawingCode.delete('1.0',END)
            self.drawingCodehint.delete('1.0',END)
            self.drawingCode.config(state = DISABLED)
            self.drawingCodehint.config(state = DISABLED)
            self.t.clear()
            self.t.reset()
            random.randint(1,4)
            self.currentDrawing = random.randint(0,3)
            self.drawingList = ['rectangle','triangle','square','hexagon']
            self.getDrawing()
        else:
            messagebox.showinfo("Incorrect", "Sorry! That's incorrect.")
            self.PlayerPoints -= 100
            self.playerPointUpdate()


    def AnswerCheck3(self):
        if (self.currentDrawing == 2):
            messagebox.showinfo("Correct", "You Guessed Correctly!")
            self.PlayerPoints += 100
            self.playerPointUpdate()
            self.drawingCode.config(state = NORMAL)
            self.drawingCodehint.config(state = NORMAL)
            self.drawingCode.delete('1.0',END)
            self.drawingCodehint.delete('1.0',END)
            self.drawingCode.config(state = DISABLED)
            self.drawingCodehint.config(state = DISABLED)
            self.t.clear()
            self.t.reset()
            random.randint(1,4)
            self.currentDrawing = random.randint(0,3)
            self.drawingList = ['rectangle','triangle','square','hexagon']
            self.getDrawing()
        else:
            messagebox.showinfo("Incorrect", "Sorry! That's incorrect.")
            self.PlayerPoints -= 100
            self.playerPointUpdate()

    def AnswerCheck4(self):
        if (self.currentDrawing == 3):
            messagebox.showinfo("Correct", "You Guessed Correctly!")
            self.PlayerPoints += 100
            self.playerPointUpdate()
            self.drawingCode.config(state = NORMAL)
            self.drawingCodehint.config(state = NORMAL)
            self.drawingCode.delete('1.0',END)
            self.drawingCodehint.delete('1.0',END)
            self.drawingCode.config(state = DISABLED)
            self.drawingCodehint.config(state = DISABLED)
            self.t.clear()
            self.t.reset()
            random.randint(1,4)
            self.currentDrawing = random.randint(0,3)
            self.drawingList = ['rectangle','triangle','square','hexagon']
            self.getDrawing()
        else:
            messagebox.showinfo("Incorrect", "Sorry! That's incorrect.")
            self.PlayerPoints -= 100
            self.playerPointUpdate()


    def getDrawingHint(self):
        self.drawingCode.config(state = NORMAL)
        self.drawingCodehint.config(state = NORMAL)
        self.drawingCodehint.delete('1.0',END)
        filename = 'Drawings/' + self.drawingList[self.currentDrawing] +'hint.txt'
        stringhintTxt = open(filename, 'r').read()
        self.drawingCodehint.insert(INSERT, stringhintTxt)
        self.drawingCode.config(state = DISABLED)
        self.drawingCodehint.config(state = DISABLED)

    def disableBtns(self):
        self.Answer1Btn.config(state = DISABLED)
        self.Answer2Btn.config(state = DISABLED)
        self.Answer3Btn.config(state = DISABLED)
        self.Answer4Btn.config(state = DISABLED)        
        self.hintBtn.config(state = DISABLED)
        self.solutionBtn.config(state = DISABLED)
        self.sketchBtn.config(state = DISABLED)

    def enableBtns(self):
        self.Answer1Btn.config(state = NORMAL)
        self.Answer2Btn.config(state = NORMAL)
        self.Answer3Btn.config(state = NORMAL)
        self.Answer4Btn.config(state = NORMAL)
        self.hintBtn.config(state = NORMAL)
        self.sketchBtn.config(state = NORMAL)
        self.solutionBtn.config(state = NORMAL)


            
            
    #draw rectangle
    def rectangle(self):
        self.t.speed(2)
        self.t.color("#51a9ff")
        self.t.width(3)
        self.t.forward(100)
        self.t.left(90)
        self.t.forward(70)
        self.t.left(90)
        self.t.forward(100)
        self.t.left(90)
        self.t.forward(70)
        self.t.hideturtle()

    #rectangle Hint
    def rectanglehint(self):
        self.t.speed(2)
        self.t.color("#51a9ff")
        self.t.width(3)
        self.t.forward(100)
        self.t.left(90)
        self.t.forward(70)
        self.t.left(90)

    #triangle
    def triangle(self):
        self.t.speed(2)
        self.t.color("#51a9ff")
        self.t.width(3)
        self.t.forward(100)
        self.t.left(120)
        self.t.forward(100)
        self.t.left(120)
        self.t.forward(100)
        self.t.hideturtle()


    #triangle Hint
    def trianglehint(self):
        self.t.speed(2)
        self.t.color("#51a9ff")
        self.t.width(3)
        self.t.forward(100)
        self.t.left(120)
        self.t.forward(100)

    #rectangle
    def square(self):
        self.t.speed(2)
        self.t.color("#51a9ff")
        self.t.width(3)
        self.t.forward(100)
        self.t.left(90)
        self.t.forward(100)
        self.t.left(90)
        self.t.forward(100)
        self.t.left(90)
        self.t.forward(100)
        self.t.hideturtle()

    #rectangle Hint
    def squarehint(self):
        self.t.speed(2)
        self.t.color("#51a9ff")
        self.t.width(3)
        self.t.forward(100)
        self.t.left(90)
        self.t.forward(100)
        self.t.left(90)

    #hexagon
    def hexagonhint(self):
        self.t.speed(2)
        self.t.color("#51a9ff")
        self.t.width(3)
        self.t.left(60)
        self.t.forward(75)
        self.t.left(60)
        self.t.forward(75)
        self.t.left(60)
        self.t.forward(75)

    def hexagon(self):
        self.t.speed(2)
        self.t.color("#51a9ff")
        self.t.width(3)
        self.t.left(60)
        self.t.forward(75)
        self.t.left(60)
        self.t.forward(75)
        self.t.left(60)
        self.t.forward(75)
        self.t.left(60)
        self.t.forward(75)
        self.t.left(60)
        self.t.forward(75)
        self.t.left(60)
        self.t.forward(75)

        self.t.hideturtle()

   

GameMenu()
