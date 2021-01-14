#!/usr/bin/python
#
# Chrome - Profile Launcher for Chrome
# @see http://stackoverflow.com/questions/16410852/keyboard-interrupt-with-with-python-gtk
# https://pygobject.readthedocs.io/en/latest/getting_started.html
# https://lazka.github.io/pgi-docs/
# http://www.programcreek.com/python/example/9059/gtk.IconView

import os

import sys

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib
from gi.repository.GdkPixbuf import Pixbuf

import glob

import find_browser
import find_profile

import browser_chrome
import browser_firefox
import browser_links


NAME="Browser Launcher"
#ICON="google-chrome"
ICON="applications-internet"

# @see http://stackoverflow.com/questions/16410852/keyboard-interrupt-with-with-python-gtk
#if __name__ == '__main__':
#	import signal
#	signal.signal(signal.SIGINT, signal.SIG_DFL)
#	your_application_main()

#
# My Window Class
class Fabula_Window(Gtk.Window):

	def __init__(self):

		Gtk.Window.__init__(self, title=NAME)
		self.set_border_width(1)
		self.set_default_size(640, 480)
		self.set_size_request(640, 480)
		self.set_decorated(True)
		self.set_double_buffered(True)
		self.set_hide_titlebar_when_maximized(True)
		self.set_icon( Gtk.IconTheme.get_default().load_icon(ICON, 64, 0) )
		self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
		self.set_resizable(True)

		# CTRL+Q to Quit
		ag = Gtk.AccelGroup()
		ag.connect(Gdk.keyval_from_name('Q'), Gdk.ModifierType.CONTROL_MASK, 0, Gtk.main_quit)
		self.add_accel_group(ag)

		self.add_head()

		self.vbox = Gtk.VBox(False, 0)
		self.add(self.vbox)

		self.add_profile_list()
		# self.add_options()
		self.add_buttons()

		if (len(sys.argv) >= 2):
			sb = Gtk.Statusbar()
			sb.set_size_request(200, 25)
			#sb.set_has_resize_grip(True)
			sbc = sb.get_context_id("url")
			sb.push(sbc, "URL: " + sys.argv[1])
			self.vbox.pack_end(sb, False, False, 0)
		#end-if

	#
	# Add our Magic Headerbar
	def add_head(self):
		hb = Gtk.HeaderBar()
		hb.set_title(NAME)
		hb.set_subtitle("Select Binary and Profile")
		hb.set_decoration_layout("icon,menu:minimize,maximize,close")
		hb.set_show_close_button(True)
		self.set_titlebar(hb)
	#end-def

	#
	# Profile
	def add_profile_list(self):

		liststore = Gtk.ListStore(str, Pixbuf, object)
		iconview = Gtk.IconView.new()
		iconview.set_model(liststore)
		iconview.set_columns(3)
		iconview.set_item_padding(0)
		iconview.set_item_width((640 - 16) / 6)
		iconview.set_margin(0)
		iconview.set_pixbuf_column(1)
		iconview.set_row_spacing(0)
		iconview.set_spacing(0)
		iconview.set_text_column(0)

		prof_list = find_profile.load_browser_profiles()
		for prof in prof_list:
			#print(prof)
			liststore.append([ prof['name'], prof['icon'], prof ])
		# end-for

		#
		#
		wrapview = Gtk.ScrolledWindow()
		#wrapview.set_shadow_type(Gtk.ShadowType.NONE)
		wrapview.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
		wrapview.add(iconview)

		iconview.connect("item-activated", self.profile_launch)
		iconview.connect("selection-changed", self.profile_selected)

		self.vbox.pack_start(wrapview, True, True, 0)
		#self.add(iconview)
	#end-def

	def add_buttons(self):

		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)

		b0 = Gtk.Button(label="Launch")
		b0.connect("clicked", self.launch_browser)
		hbox.pack_start(b0, True, True, 0)

		b1 = Gtk.Button(label="Incognito")
		b1.connect("clicked", self.launch_browser_incognito)
		hbox.pack_start(b1, True, True, 0)

		b2 = Gtk.Button(label="Cancel")
		b2.connect("clicked", Gtk.main_quit)
		hbox.pack_start(b2, True, True, 0)

		self.vbox.pack_start(hbox, False, False, 0)

	#end-def

	def profile_selected(self, view):

		print("profile_selected")
		#print(view)
		data = view.get_model()
		path = view.get_selected_items()
		#print(listdata)
		#sel_list = listdata.get_selected_items()
		#print(sel_list)
		self._prof = data[path][2]
		#print(self._prof)

	#end-def

	def profile_launch(self, view, path):

		print("profile_launch")

		#print(self._prof)
		self.launch_browser(False)

	#end-def

	#
	#
	def launch_browser(self, x):

		print("launch_browser")
		#print(self)
		#print(view)
		#print(path)
		#listdata = view.get_model()
		#print(listdata)
		#prof = listdata[path][2]
		print(self._prof)

		args = {}
		args['link'] = None
		args['private'] = False

		if (len(sys.argv) >= 2):
			args['link'] = sys.argv[1]
		#end-if

		if "chrome" == self._prof['type']:
			browser_chrome.launch(self._prof, args)
		elif "firefox" == self._prof['type']:
			browser_firefox.launch(self._prof, args)
		elif "links" == self._prof['type']:
			browser_links.launch(self._prof, args)
		#end-if

		#self.hide()
		Gtk.main_quit()

	#end-def

	#
	#
	def launch_browser_incognito(self, x):

		print("launch_browser_incognito")

		args = {}
		args['link'] = None
		args['private'] = True

		if (len(sys.argv) >= 2):
			args['link'] = sys.argv[1]
		#end-if

		if "chrome" == self._prof['type']:
			browser_chrome.launch(self._prof, args)
		elif "firefox" == self._prof['type']:
			browser_firefox.launch(self._prof, args)
		elif "links" == self._prof['type']:
			browser_links.launch(self._prof, args)
		#end-if

		#self.hide()
		Gtk.main_quit()

	#end-def

#end-class

#
# main()
win = Fabula_Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
#print(dir(win.props))
#print(dir(Gtk.Window))
Gtk.main()
#GLib.MainLoop().run()
