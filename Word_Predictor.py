import csv
from tkinter import *
import threading

root = Tk()
root.geometry("300x300")

if __name__ == '__main__':
    class Prediction():
        d = dict()
        l = []
        with open('EnglishDictionary.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                temp = (row[0].split(','))
                d[temp[0]] = temp[1]

        def entryBox(self):
            self.entry = Entry(root)
            self.entry.pack()
            self.entry.bind("<Key>", lambda k: self.thrd1(k))

        def predict(self, event=None):
            # e = input("Enter: ")
            suggest = dict()
            v = []
            for key in self.d:
                if (self.entry.get() in key[:len(self.entry.get())]):
                    suggest[key] = self.d[key]

            suggest = {k: v for k, v in sorted(suggest.items(), key=lambda item: item[1])}
            res = dict(list(suggest.items())[0: 5])

            self.listBox = Listbox(root)
            self.listBox.pack()
            self.listBox.bind("<Button-1>", self.thrd2)

            self.l = []
            for key in res:
                self.l.append(key)
                self.listBox.insert(END, key)
            if(self.entry.get() == ""):
                self.listBox.destroy()
            if(len(self.l) == 0):
                self.listBox.destroy()
                self.label = Label(root, text = "No match found!!")
                self.label.pack()
                exit("#")

            # print(out)

        def thrd1(self, event=None):
            if(65 <= ord(event.char) <= 90 or 97 <= ord(event.char) <= 122 or ord(event.char) == 8):
                try:
                    self.label.destroy()
                except:
                    pass
                try:
                    self.listBox.destroy()

                except:
                    pass
                s = threading.Timer(0, self.predict)
                s.start()

        def choose(self, event=None):
            word = self.listBox.get(self.listBox.curselection())
            self.entry.delete(0,END)
            self.entry.insert(0,word)
            self.listBox.destroy()


        def thrd2(self,event=None):
            t = threading.Timer(0,self.choose)
            t.start()

    obj = Prediction()
    obj.entryBox()


root.mainloop()
