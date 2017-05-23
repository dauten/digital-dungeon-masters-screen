import pygtk
pygtk.require('2.0')
import gtk
import random

ACTIVE = 0
men = []
woman = []

class Roller(gtk.Window):
	
	def __init__(self):

		def roll(MAX):
			rand = random.randint(1,MAX)
			global ACTIVE
			label_app.set_text("Dice size=" + str(ACTIVE) + " | Roll Result=" + str(rand))

		def setd(SIZE):
			global ACTIVE
			ACTIVE = SIZE
			roll(SIZE)

		super(Roller, self).__init__()

		global ACTIVE
		ACTIVE = 6

		# create a new window
		app_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		app_window.set_size_request(500, 350)
		app_window.set_border_width(10)
		app_window.set_title("Dice Roller")


		vbox_app = gtk.VBox(False, 0)
		app_window.add(vbox_app)
		vbox_app.show()

		label_app = gtk.Label("the result will be here.  default dice is d6, choose by clicking button.")
		label_app.show()
		vbox_app.pack_start(label_app, False, False, 6)
		# Use HBox() to layout text and button next to each other:

		hbox_roll = gtk.HBox(False, 0)


		options = gtk.VBox(False,0)


		button_roll1 = gtk.Button("d4")
		button_roll1.connect("clicked", lambda w: setd(4))
		button_roll1.set_flags(gtk.CAN_DEFAULT)
		options.pack_start(button_roll1, True, True, 0)
		button_roll1.show()

		button_roll2 = gtk.Button("d6")
		button_roll2.connect("clicked", lambda w: setd(6))
		button_roll2.set_flags(gtk.CAN_DEFAULT)
		options.pack_start(button_roll2, True, True, 0)
		button_roll2.show()

		button_roll2 = gtk.Button("d8")
		button_roll2.connect("clicked", lambda w: setd(8))
		button_roll2.set_flags(gtk.CAN_DEFAULT)
		options.pack_start(button_roll2, True, True, 0)
		button_roll2.show()
		
		button_roll2 = gtk.Button("d10")
		button_roll2.connect("clicked", lambda w: setd(10))
		button_roll2.set_flags(gtk.CAN_DEFAULT)
		options.pack_start(button_roll2, True, True, 0)
		button_roll2.show()

		button_roll2 = gtk.Button("d12")
		button_roll2.connect("clicked", lambda w: setd(12))
		button_roll2.set_flags(gtk.CAN_DEFAULT)
		options.pack_start(button_roll2, True, True, 0)
		button_roll2.show()

		button_roll2 = gtk.Button("d20")
		button_roll2.connect("clicked", lambda w: setd(20))
		button_roll2.set_flags(gtk.CAN_DEFAULT)
		options.pack_start(button_roll2, True, True, 0)
		button_roll2.show()

		button_roll2 = gtk.Button("d100")
		button_roll2.connect("clicked", lambda w: setd(100))
		button_roll2.set_flags(gtk.CAN_DEFAULT)
		options.pack_start(button_roll2, True, True, 0)
		button_roll2.show()
		
		options.show()
		hbox_roll.pack_start(options, True, True, 0)


		button_roll = gtk.Button("Roll Previous")
		button_roll.connect("clicked", lambda w: roll(ACTIVE))
		button_roll.set_flags(gtk.CAN_DEFAULT)
		hbox_roll.pack_start(button_roll, True, True, 0)
		button_roll.show()

		hbox_roll.show()
		vbox_app.add(hbox_roll)

		# Place after association to hbox/vbox to avoid the following error:
		# GtkWarning: gtkwidget.c:5460: widget not within a GtkWindow
		button_roll.grab_default() 
		app_window.show()

		return

class Names(gtk.Window):
	
	def __init__(self):

		def name():
			global men
			global woman
		

			M = "Male Names:\n"
			for int in range(0,5):
				M = M + men[random.randint(0,len(men)-1)]

			F = "Female Names:\n"
			for int in range(0,5):
				F = F + woman[random.randint(0,len(woman)-1)]

			female.set_text(F)
			male.set_text(M)
			

		super(Names, self).__init__()

		global men
		global woman

		file = open("names(M).txt","r")
		for line in file:
			men.append(line)

		file.close()

		file = open("names(F).txt","r")
		for line in file:
			woman.append(line)


		file.close()

		# create a new window
		app_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		app_window.set_size_request(500, 200)
		app_window.set_border_width(10)
		app_window.set_title("Names")

		vbox = gtk.VBox(False,0)
		app_window.add(vbox)
		vbox.show()

		hbox = gtk.HBox(False,0)
		vbox.pack_start(hbox,True,True,0)
		hbox.show()

		male = gtk.Label("male names will be listed here")
		male.show()
		hbox.pack_start(male, True, True, 6)
		

		female = gtk.Label("female names will be listed here")
		female.show()
		hbox.pack_start(female, True, True, 6)
		

		generate = gtk.Button("Make more names!")
		generate.connect("clicked", lambda w: name())
		generate.set_flags(gtk.CAN_DEFAULT)
		generate.show()	
		
		vbox.pack_start(generate, True, True, 0)


		app_window.show()

		name()

class Master(gtk.Window):
	
	def __init__(self):

		super(Master, self).__init__()

		# create a new window
		app_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		app_window.set_size_request(300, 300)
		app_window.set_border_width(10)
		app_window.set_title("MASTER")
		app_window.connect("delete_event", lambda w,e: gtk.main_quit())

		apps = gtk.VBox(False,0)
		app_window.add(apps)
		apps.show()

		
		roller = gtk.Button("Launch Roller")
		roller.connect("clicked", lambda w: Roller())
		roller.set_flags(gtk.CAN_DEFAULT)
		roller.show()	

		names = gtk.Button("Launch Names")
		names.connect("clicked", lambda w: Names())
		names.set_flags(gtk.CAN_DEFAULT)
		names.show()	
		
		apps.pack_start(roller, True, True, 0)
		apps.pack_start(names, True, True, 0)


		app_window.show()

Master()
gtk.main()
