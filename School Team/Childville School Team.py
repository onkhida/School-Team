import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import time

connect = sqlite3.connect('School Team Database.db')
db_cursor = connect.cursor()
        
class Application:

    def __init__(self, master):

        self.master = master
        def backnow():
        	self.notyetnow.place_forget()
        	self.left.place(x=0, y = 0)

        def rg():
            self.left.place_forget()

            self.reg = Frame(master, width=1366, height = 768)

            self.reg.place(x=0, y=0)

            self.sign = PhotoImage(file = 'sign.png')
            self.sign_label = Label(self.reg, image = self.sign)
            self.sign_label.place(x = 366, y = 0)

            self.newbutt = Button(self.reg, text = 'BACK', font = ('consolas 15 bold'), command = lambda:gohome_rg())
            self.newbutt.place(x = 0, y = 0)

            def gohome_rg():
            	self.reg.place_forget()
            	self.left.place(x = 0, y = 0)

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

                    tkinter.messagebox.showinfo('Success', 'Details on ' + str(self.player_fname) + ' have been added')
        #Problems Here - Fixing
        #Function - widget.place_forget()

        def lk():

            self.left.place_forget()

            self.look = Frame(master, width = 1366, height = 768)
            self.look.place(x=0, y=0)

            self.sign = PhotoImage(file = 'soccercoach.png')
            self.sign_label = Label(self.look, image = self.sign)
            self.sign_label.place(x = 366, y = 0)

            self.somebutt = Button(self.look, text = 'BACK', font = ('consolas 15 bold'), command = lambda: gohome_lk())
            self.somebutt.place(x = 0, y = 0)

            def gohome_lk():
            	self.look.place_forget()
            	self.left.place(x = 0, y = 0)

            def searching(given_val):
            	if given_val == 'fnames':
            		self.butt.place_forget()
            		self.butt2.place_forget()
            		self.butt3.place_forget()
            		self.butt4.place_forget()
            		self.butt5.place_forget()
            		self.butt6.place_forget()
            		self.sign_label.place_forget()
            		self.label.place_forget()
            		self.label_again.place_forget()

            		self.labeler = Label(self.look, text = 'Please fill in the players first name: ', font = ('garamond 23 bold'))
            		self.labeler.place(x=400,y=110)

            		self.newent = Entry(self.look, font = ('garamond 17 bold'))
            		self.newent.config(width = 50)
            		self.newent.place(x = 350, y = 150)

            		self.searchit = Button(self.look, text = 'Search', font = ('garamond 12 bold'), command = lambda: func())
            		self.searchit.place(x = 905, y = 150)
            		#I need to restructure my whole function!

            		def func():
            			somesequel = 'SELECT * FROM Players'

            			theresult = db_cursor.execute(somesequel)

            			value = self.newent.get()
            			#New Function!
            			self.display = Frame(self.look, bg = 'steelblue', width = 1366, height = 500)
            			#Values would be shown in a tabular format.
            			self.display.place(x = 0, y = 200)

            			self.lb = Label(self.display, text = 'First Name',
            				font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb.place(x = 125, y = 0)

            			self.lb2 = Label(self.display, text = 'Second Name', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 325, y = 0)

            			self.lb2 = Label(self.display, text = 'Age', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 575, y = 0)

            			self.lb2 = Label(self.display, text = 'Position', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 725, y = 0)

            			self.lb2 = Label(self.display, text = 'Shirt Number', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 925, y = 0)

            			self.lb2 = Label(self.display, text = 'Attributes', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 1125, y = 0)

            			#X positions for labels
            			fname_x = 125
            			sname_x = 325
            			age_x = 575
            			pos_x = 725
            			shirt_x = 925
            			attrib_x = 1125

            			turn = 0
            			count = 0
            			for line in theresult:
            				count += 1
            				turn += 1
            				#print(line)
            				newval = list(line)

            				basey = 0

            				if str(newval[1]).upper() == str(value).upper():

            					self.fname = Label(self.display, text = str(newval[1]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.fname.place(x = fname_x, y = basey + 20 * turn)

            					self.sname = Label(self.display, text = str(newval[2]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.sname.place(x = sname_x, y = basey + 20 * turn)

            					self.ages = Label(self.display, text = str(newval[3]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.ages.place(x = age_x, y = basey + 20 * turn)

            					self.positions = Label(self.display, text = str(newval[4]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')
            					self.positions.place(x = pos_x, y = basey + 20 * turn)

            					self.shirts = Label(self.display, text = str(newval[0]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')

            					self.shirts.place(x = shirt_x, y = basey + 20 * turn)

            					self.attribs = Label(self.display, text = str(newval[5]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')

            					self.attribs.place(x = attrib_x, y = basey + 20 * turn)


            				

            	elif given_val == 'snames':
            		self.butt.place_forget()
            		self.butt2.place_forget()
            		self.butt3.place_forget()
            		self.butt4.place_forget()
            		self.butt5.place_forget()
            		self.butt6.place_forget()
            		self.sign_label.place_forget()
            		self.label.place_forget()
            		self.label_again.place_forget()

            		self.labeler = Label(self.look, text = 'Please fill in the players second name: ', font = ('garamond 23 bold'))
            		self.labeler.place(x=400,y=110)

            		self.newent = Entry(self.look, font = ('garamond 17 bold'))
            		self.newent.config(width = 50)
            		self.newent.place(x = 350, y = 150)

            		self.searchit = Button(self.look, text = 'Search', font = ('garamond 12 bold'), command = lambda: func())
            		self.searchit.place(x = 905, y = 150)

            		def func():
            			somesequel = 'SELECT * FROM Players'

            			theresult = db_cursor.execute(somesequel)

            			value = self.newent.get()
            			#New Function!
            			self.display = Frame(self.look, bg = 'steelblue', width = 1366, height = 500)
            			#Values would be shown in a tabular format.
            			self.display.place(x = 0, y = 200)

            			self.lb = Label(self.display, text = 'First Name',
            				font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb.place(x = 125, y = 0)

            			self.lb2 = Label(self.display, text = 'Second Name', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 325, y = 0)

            			self.lb2 = Label(self.display, text = 'Age', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 575, y = 0)

            			self.lb2 = Label(self.display, text = 'Position', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 725, y = 0)

            			self.lb2 = Label(self.display, text = 'Shirt Number', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 925, y = 0)

            			self.lb2 = Label(self.display, text = 'Attributes', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 1125, y = 0)

            			#X positions for labels
            			fname_x = 125
            			sname_x = 325
            			age_x = 575
            			pos_x = 725
            			shirt_x = 925
            			attrib_x = 1125

            			turn = 0
            			count = 0
            			for line in theresult:
            				count += 1
            				turn += 1
            				#print(line)
            				newval = list(line)

            				basey = 0

            				if str(newval[2]).upper() == str(value).upper():

            					self.fname = Label(self.display, text = str(newval[1]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.fname.place(x = fname_x, y = basey + 20 * turn)

            					self.sname = Label(self.display, text = str(newval[2]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.sname.place(x = sname_x, y = basey + 20 * turn)

            					self.ages = Label(self.display, text = str(newval[3]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.ages.place(x = age_x, y = basey + 20 * turn)

            					self.positions = Label(self.display, text = str(newval[4]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')
            					self.positions.place(x = pos_x, y = basey + 20 * turn)

            					self.shirts = Label(self.display, text = str(newval[0]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')

            					self.shirts.place(x = shirt_x, y = basey + 20 * turn)

            					self.attribs = Label(self.display, text = str(newval[5]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')

            					self.attribs.place(x = attrib_x, y = basey + 20 * turn)

            	elif given_val == 'shirtnums':
            		self.butt.place_forget()
            		self.butt2.place_forget()
            		self.butt3.place_forget()
            		self.butt4.place_forget()
            		self.butt5.place_forget()
            		self.butt6.place_forget()
            		self.sign_label.place_forget()
            		self.label.place_forget()
            		self.label_again.place_forget()

            		self.labeler = Label(self.look, text = 'Please fill in the players shirt number: ', font = ('garamond 23 bold'))
            		self.labeler.place(x=400,y=110)

            		self.newent = Entry(self.look, font = ('garamond 17 bold'))
            		self.newent.config(width = 50)
            		self.newent.place(x = 350, y = 150)

            		self.searchit = Button(self.look, text = 'Search', font = ('garamond 12 bold'), command = lambda: func())
            		self.searchit.place(x = 905, y = 150)

            		def func():
            			somesequel = 'SELECT * FROM Players'

            			theresult = db_cursor.execute(somesequel)

            			value = self.newent.get()
            			#New Function!
            			self.display = Frame(self.look, bg = 'steelblue', width = 1366, height = 500)
            			#Values would be shown in a tabular format.
            			self.display.place(x = 0, y = 200)

            			self.lb = Label(self.display, text = 'First Name',
            				font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb.place(x = 125, y = 0)

            			self.lb2 = Label(self.display, text = 'Second Name', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 325, y = 0)

            			self.lb2 = Label(self.display, text = 'Age', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 575, y = 0)

            			self.lb2 = Label(self.display, text = 'Position', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 725, y = 0)

            			self.lb2 = Label(self.display, text = 'Shirt Number', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 925, y = 0)

            			self.lb2 = Label(self.display, text = 'Attributes', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 1125, y = 0)

            			#X positions for labels
            			fname_x = 125
            			sname_x = 325
            			age_x = 575
            			pos_x = 725
            			shirt_x = 925
            			attrib_x = 1125

            			turn = 0
            			count = 0
            			for line in theresult:
            				count += 1
            				turn += 1
            				#print(line)
            				newval = list(line)

            				basey = 0

            				if int(newval[0]) == int(value):

            					self.fname = Label(self.display, text = str(newval[1]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.fname.place(x = fname_x, y = basey + 20 * turn)

            					self.sname = Label(self.display, text = str(newval[2]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.sname.place(x = sname_x, y = basey + 20 * turn)

            					self.ages = Label(self.display, text = str(newval[3]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.ages.place(x = age_x, y = basey + 20 * turn)

            					self.positions = Label(self.display, text = str(newval[4]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')
            					self.positions.place(x = pos_x, y = basey + 20 * turn)

            					self.shirts = Label(self.display, text = str(newval[0]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')

            					self.shirts.place(x = shirt_x, y = basey + 20 * turn)

            					self.attribs = Label(self.display, text = str(newval[5]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')

            					self.attribs.place(x = attrib_x, y = basey + 20 * turn)


            	elif given_val == 'ages':

            		self.butt.place_forget()
            		self.butt2.place_forget()
            		self.butt3.place_forget()
            		self.butt4.place_forget()
            		self.butt5.place_forget()
            		self.butt6.place_forget()
            		self.sign_label.place_forget()
            		self.label.place_forget()
            		self.label_again.place_forget()

            		self.labeler = Label(self.look, text = 'Please fill in the players age(s): ', font = ('garamond 23 bold'))
            		self.labeler.place(x=400,y=110)

            		self.newent = Entry(self.look, font = ('garamond 17 bold'))
            		self.newent.config(width = 50)
            		self.newent.place(x = 350, y = 150)

            		self.searchit = Button(self.look, text = 'Search', font = ('garamond 12 bold'), command = lambda: func())
            		self.searchit.place(x = 905, y = 150)

            		def func():
            			somesequel = 'SELECT * FROM Players'

            			theresult = db_cursor.execute(somesequel)

            			value = self.newent.get()
            			#New Function!
            			self.display = Frame(self.look, bg = 'steelblue', width = 1366, height = 500)
            			#Values would be shown in a tabular format.
            			self.display.place(x = 0, y = 200)

            			self.lb = Label(self.display, text = 'First Name',
            				font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb.place(x = 125, y = 0)

            			self.lb2 = Label(self.display, text = 'Second Name', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 325, y = 0)

            			self.lb2 = Label(self.display, text = 'Age', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 575, y = 0)

            			self.lb2 = Label(self.display, text = 'Position', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 725, y = 0)

            			self.lb2 = Label(self.display, text = 'Shirt Number', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 925, y = 0)

            			self.lb2 = Label(self.display, text = 'Attributes', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 1125, y = 0)

            			#X positions for labels
            			fname_x = 125
            			sname_x = 325
            			age_x = 575
            			pos_x = 725
            			shirt_x = 925
            			attrib_x = 1125

            			turn = 0
            			count = 0
            			for line in theresult:
            				count += 1
            				turn += 1
            				#print(line)
            				newval = list(line)

            				basey = 0

            				if str(newval[3]).upper() == str(value).upper():

            					self.fname = Label(self.display, text = str(newval[1]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.fname.place(x = fname_x, y = basey + 20 * turn)

            					self.sname = Label(self.display, text = str(newval[2]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.sname.place(x = sname_x, y = basey + 20 * turn)

            					self.ages = Label(self.display, text = str(newval[3]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.ages.place(x = age_x, y = basey + 20 * turn)

            					self.positions = Label(self.display, text = str(newval[4]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')
            					self.positions.place(x = pos_x, y = basey + 20 * turn)

            					self.shirts = Label(self.display, text = str(newval[0]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')

            					self.shirts.place(x = shirt_x, y = basey + 20 * turn)

            					self.attribs = Label(self.display, text = str(newval[5]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')

            					self.attribs.place(x = attrib_x, y = basey + 20 * turn)

            	elif given_val == 'positions':
            		self.butt.place_forget()
            		self.butt2.place_forget()
            		self.butt3.place_forget()
            		self.butt4.place_forget()
            		self.butt5.place_forget()
            		self.butt6.place_forget()
            		self.sign_label.place_forget()
            		self.label.place_forget()
            		self.label_again.place_forget()

            		self.labeler = Label(self.look, text = 'Please fill in the players position(s): ', font = ('garamond 23 bold'))
            		self.labeler.place(x=400,y=110)

            		self.newent = Entry(self.look, font = ('garamond 17 bold'))
            		self.newent.config(width = 50)
            		self.newent.place(x = 350, y = 150)

            		self.searchit = Button(self.look, text = 'Search', font = ('garamond 12 bold'), command = lambda: func())
            		self.searchit.place(x = 905, y = 150)

            		def func():
            			somesequel = 'SELECT * FROM Players'

            			theresult = db_cursor.execute(somesequel)

            			value = self.newent.get()
            			#New Function!
            			self.display = Frame(self.look, bg = 'steelblue', width = 1366, height = 500)
            			#Values would be shown in a tabular format.
            			self.display.place(x = 0, y = 200)

            			self.lb = Label(self.display, text = 'First Name',
            				font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb.place(x = 125, y = 0)

            			self.lb2 = Label(self.display, text = 'Second Name', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 325, y = 0)

            			self.lb2 = Label(self.display, text = 'Age', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 575, y = 0)

            			self.lb2 = Label(self.display, text = 'Position', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 725, y = 0)

            			self.lb2 = Label(self.display, text = 'Shirt Number', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 925, y = 0)

            			self.lb2 = Label(self.display, text = 'Attributes', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 1125, y = 0)

            			#X positions for labels
            			fname_x = 125
            			sname_x = 325
            			age_x = 575
            			pos_x = 725
            			shirt_x = 925
            			attrib_x = 1125

            			turn = 0
            			count = 0
            			for line in theresult:
            				count += 1
            				turn += 1
            				#print(line)
            				newval = list(line)

            				basey = 0

            				if str(newval[4]).upper() == str(value).upper():

            					self.fname = Label(self.display, text = str(newval[1]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.fname.place(x = fname_x, y = basey + 20 * turn)

            					self.sname = Label(self.display, text = str(newval[2]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.sname.place(x = sname_x, y = basey + 20 * turn)

            					self.ages = Label(self.display, text = str(newval[3]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.ages.place(x = age_x, y = basey + 20 * turn)

            					self.positions = Label(self.display, text = str(newval[4]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')
            					self.positions.place(x = pos_x, y = basey + 20 * turn)

            					self.shirts = Label(self.display, text = str(newval[0]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')

            					self.shirts.place(x = shirt_x, y = basey + 20 * turn)

            					self.attribs = Label(self.display, text = str(newval[5]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')

            					self.attribs.place(x = attrib_x, y = basey + 20 * turn)


				#For some reason, this button functionality isn't running - Fixed
            	else:
            		self.butt.place_forget()
            		self.butt2.place_forget()
            		self.butt3.place_forget()
            		self.butt4.place_forget()
            		self.butt5.place_forget()
            		self.butt6.place_forget()
            		self.sign_label.place_forget()
            		self.label.place_forget()
            		self.label_again.place_forget()

            		self.labeler = Label(self.look, text = 'Please fill in the players position(s): ', font = ('garamond 23 bold'))
            		self.labeler.place(x=400,y=110)

            		self.newent = Entry(self.look, font = ('garamond 17 bold'))
            		self.newent.config(width = 50)
            		self.newent.place(x = 350, y = 150)

            		self.searchit = Button(self.look, text = 'Search', font = ('garamond 12 bold'), command = lambda: func())
            		self.searchit.place(x = 905, y = 150)

            		def func():
            			somesequel = 'SELECT * FROM Players'

            			theresult = db_cursor.execute(somesequel)

            			value = self.newent.get()
            			#New Function!
            			self.display = Frame(self.look, bg = 'steelblue', width = 1366, height = 500)
            			#Values would be shown in a tabular format.
            			self.display.place(x = 0, y = 200)

            			self.lb = Label(self.display, text = 'First Name',
            				font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb.place(x = 125, y = 0)

            			self.lb2 = Label(self.display, text = 'Second Name', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 325, y = 0)

            			self.lb2 = Label(self.display, text = 'Age', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 575, y = 0)

            			self.lb2 = Label(self.display, text = 'Position', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 725, y = 0)

            			self.lb2 = Label(self.display, text = 'Shirt Number', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 925, y = 0)

            			self.lb2 = Label(self.display, text = 'Attributes', font = ('consolas 16 bold'), bg = 'steelblue', fg = 'white')
            			self.lb2.place(x = 1125, y = 0)

            			#X positions for labels
            			fname_x = 125
            			sname_x = 325
            			age_x = 575
            			pos_x = 725
            			shirt_x = 925
            			attrib_x = 1125

            			turn = 0
            			count = 0
            			for line in theresult:
            				count += 1
            				turn += 1
            				#print(line)
            				newval = list(line)

            				basey = 0

            				if str(newval[5]).upper() == str(value).upper():

            					self.fname = Label(self.display, text = str(newval[1]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.fname.place(x = fname_x, y = basey + 20 * turn)

            					self.sname = Label(self.display, text = str(newval[2]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.sname.place(x = sname_x, y = basey + 20 * turn)

            					self.ages = Label(self.display, text = str(newval[3]), font = ('consolas 14 bold'), bg = 'steelblue',
            						fg = 'white')
            					self.ages.place(x = age_x, y = basey + 20 * turn)

            					self.positions = Label(self.display, text = str(newval[4]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')
            					self.positions.place(x = pos_x, y = basey + 20 * turn)

            					self.shirts = Label(self.display, text = str(newval[0]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')

            					self.shirts.place(x = shirt_x, y = basey + 20 * turn)

            					self.attribs = Label(self.display, text = str(newval[5]), font = ('consolas 14 bold'),
            						bg = 'steelblue', fg = 'white')

            					self.attribs.place(x = attrib_x, y = basey + 20 * turn)


            #==============================LABELS============================#

            self.label = Label(self.look, text = 'Look for an existing player', font = ('garamond 17 bold'))

            self.label.place(x=50, y=50)

            self.label_again = Label(self.look, text = 'How do you want to search?', font = ('garamond 15 bold'))
            self.label_again.place(x=50,y=100)

            self.butt = Button(self.look, text = 'First Name', font = ('garamond 15 bold'), command = lambda:searching('fnames'))
            self.butt.config(width=10)
            self.butt.place(x = 100, y = 150)

            self.butt2 = Button(self.look, text = 'Second Name', font = ('garamond 15 bold'), command = lambda:searching('snames'))

            self.butt2.config(width=10)
            self.butt2.place(x = 100, y = 220)

            self.butt3 = Button(self.look, text = 'Shirt Number', font = ('garamond 15 bold'), command = lambda:searching('shirtnums'))

            self.butt3.config(width=10)
            self.butt3.place(x = 100, y = 290)

            self.butt4 = Button(self.look, text = 'Age', font = ('garamond 15 bold'), command = lambda:searching('ages'))
            self.butt4.config(width = 10)
            self.butt4.place(x = 100, y = 360)

            self.butt5 = Button(self.look, text = 'Position', font = ('garamond 15 bold'), command = lambda:searching('positions'))
            self.butt5.config(width = 10)
            self.butt5.place(x = 100, y = 430)

            self.butt6 = Button(self.look, text = 'Attributes', font = ('garamond 15 bold'), command = lambda:searching('atrribute'))
            self.butt6.config(width = 10)
            self.butt6.place(x = 100, y = 500)


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

        self.button2 = Button(self.left, text = 'Lookup Players', font = ('garamond 15 bold'), command = lambda: lk())

        self.button2.place(x = 630, y = 600)

        self.button3 = Button(self.left, text = 'Build LineUps', font = ('garamond 15 bold'), command = lambda:notyet())

        self.button3.place(x = 1030, y = 600)

        def notyet():
        	self.left.place_forget()
        	self.notyetnow = Frame(master, width = 1366, height = 766)
        	self.notyetnow.place(x = 0, y = 0)

        	self.newlabel = Label(self.notyetnow, text = 'THIS FEATURE IS UNAVAILABLE', font = ('consolas 20 bold'), fg = 'steelblue')
        	self.newlabel.place(x= 450, y = 200)

        	self.newlabel = Label(self.notyetnow, text = 'Updates coming soon', font = ('consolas 17 bold'), fg = 'steelblue')
        	self.newlabel.place(x= 520, y = 300)

        	self.somebutton = Button(self.notyetnow, text = 'BACK', font = ('consolas 15 bold'), command = lambda: backnow())
        	self.somebutton.place(x = 0, y = 0)

 

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

