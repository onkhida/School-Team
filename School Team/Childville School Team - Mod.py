import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

connect = sqlite3.connect('School Team Database.db')
db_cursor = connect.cursor()
        
class Application:

    def __init__(self, master):

        self.master = master

        def rg():
            self.left.destroy()

            self.reg = Frame(master, width=1366, height = 768)

            self.reg.place(x=0, y=0)

            self.sign = PhotoImage(file = 'sign.png')
            self.sign_label = Label(self.reg, image = self.sign)
            self.sign_label.place(x = 366, y = 0)

            #==========================================LABELS======================================================

            self.label = Label(self.reg, text = 'Register a new player', font = ('garamond 17 bold'))

            self.label.place(x=50, y=50)

            self.fname = Label(self.reg, text = 'Enter the first name: ', font = ('garamond 12 bold'))
            self.fname.place(x = 50, y = 125)

            self.sname = Label(self.reg, text = 'Enter the second name: ', font = ('garamond 12 bold'))
            self.sname.place(x = 50, y = 200)

            self.age = Label(self.reg, text = 'Please fill in the age: ', font = ('garamond 12 bold'))
            self.age.place(x = 50, y = 275)

            self.position = Label(self.reg, text = 'Please fill in the position:   ', font = ('garamond 12 bold'))
            self.position.place(x = 50, y = 350)

            self.shirtnumber = Label(self.reg, text = 'Please fill in the Shirt Number: ', font = ('garamond 12 bold'))
            self.shirtnumber.place(x = 50, y = 425)

            self.attributes = Label(self.reg, text = 'Please fill in the attributes: ', font = ('garamond 12 bold'))
            self.attributes.place(x = 50, y = 500)

            #=================================================ENTRIES================================================

            self.fname_ent = Entry(self.reg, width = 20, font = ('garamond 15'))
            self.fname_ent.place(x = 50, y = 160)

            self.sname_ent = Entry(self.reg, width = 20, font = ('garamond 15'))
            self.sname_ent.place(x = 50, y = 235)

            self.age_ent = Entry(self.reg, width = 20, font = ('garamond 15'))
            self.age_ent.place(x = 50, y = 310)

            self.position_ent = Entry(self.reg, width = 20, font = ('garamond 15'))
            self.position_ent.place(x = 50, y = 385)

            self.shirt_ent = Entry(self.reg, width = 20, font = ('garamond 15'))
            self.shirt_ent.place(x = 50, y = 460)

            self.attrib_ent = Entry(self.reg, width = 20, font = ('garamond 15'))
            self.attrib_ent.place(x = 50, y = 535)

            self.submit = Button(self.reg, text = 'Submit', font = ('garamond 20 bold'), command = lambda: get_values())
            self.submit.place(x = 75, y = 580)


            def get_values():

                self.player_fname = self.fname_ent.get()

                self.player_sname = self.sname_ent.get()

                self.player_age = self.age_ent.get()

                self.player_pos = self.position_ent.get()

                self.player_shirt = self.shirt_ent.get()

                self.player_attrib = self.attrib_ent.get()

                if self.player_fname == '' or self.player_sname == '' or self.player_age == '' or self.player_pos == '' or self.player_shirt == '' or self.player_attrib == '':
                    tkinter.messagebox.showinfo('Warning', 'Please fill in all the criteria')#Validation

                else:
                    sql = "INSERT INTO Players (ShirtNumber, Player_FirstName, Player_SecondName, Player_Age, Player_Position, Player_Attributes) VALUES(?,?,?,?,?,?) "
                    db_cursor.execute(sql, (self.player_shirt, self.player_fname, self.player_sname, self.player_age, self.player_pos, self.player_attrib))
                    connect.commit()

                    print('Succesfully added to database')

            

        self.left = Frame(master, width=1366, height = 768)

        self.left.place(x=0, y=0)

        self.label = Label(self.left, text = 'The Childville Soccer Squad 2018/19', font = ('garamond 17 bold'))

        self.label.place(x=490, y=35)

        self.photo = PhotoImage(file='childville.png')
        
        self.label2 = Label(self.left, image = self.photo)
        self.label2.place(x = 380, y = 0)

        self.label3 = Label(self.left, image = self.photo)
        self.label3.place(x = 915, y = 0)

        self.button = Button(self.left, text = 'Register Player', font = ('garamond 15 bold'), command = lambda: rg())

        self.button.place(x = 230, y = 600)

        self.button2 = Button(self.left, text = 'Lookup Players', font = ('garamond 15 bold'))

        self.button2.place(x = 630, y = 600)

        self.button3 = Button(self.left, text = 'Build LineUps', font = ('garamond 15 bold'))

        self.button3.place(x = 1030, y = 600)

        self.register = PhotoImage(file='register.png')

        self.reg_label = Label(self.left, image=self.register)
        self.reg_label.place(x = 150, y = 150)

        self.lookup = PhotoImage(file = 'lookup players.png')
        self.lookup_label = Label(self.left, image=self.lookup)
        self.lookup_label.place(x = 550, y = 150)

        self.build = PhotoImage(file = 'buildlineup.png')
        self.build_label = Label(self.left, image=self.build)
        self.build_label.place(x = 950, y = 150)

        
        

app = Tk()
app.title('The Childville Soccer Squad 2018/19')

root = Application(app)

app.geometry('1200x720+0+0')

app.mainloop()


#rg()

