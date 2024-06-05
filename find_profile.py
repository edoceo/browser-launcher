#
# Find the Browser Profiles
#

import os
#base = os.path.dirname(os.path.realpath(__file__))

import sys
sys.dont_write_bytecode = True

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf

import glob

ICON = "applications-internet"
ICON_SIZE = 64


#class ProfileData:

profile_path_list = [
	"/home/atom/Chrome",
	"/home/atom/.mozilla/firefox"
]

def load_browser_profiles():

	prof_list = []

	# Default Chrome
	prof = {}
	prof['path'] = "/home/atom/.config/chromium"
	prof['name'] = "Default"
	prof['type'] = "chrome"
	prof['icon'] = _find_browser_profile_icon(prof)
	prof_list.append(prof)

	# Default Firefox
	# prof = {}
	# prof['path'] = "/home/atom/.config/chromium"
	# prof['name'] = "Default"
	# prof['type'] = "chrome"
	# prof['icon'] = _find_browser_profile_icon(prof)
	# prof_list.append(prof)

	for path in profile_path_list:
		list0 = _find_browser_profiles(path)
		for p in list0:
			prof_list.append(p)

	return prof_list
# end-def

#
# Find the Profiles
def _find_browser_profiles(path):

	print("Find: " + path)

	prof_list = []

	dir_list = sorted(glob.glob(path + "/*"))
	for d in dir_list:
		if os.path.isdir(d):

			prof = {}
			prof['path'] = d
			prof['name'] = os.path.basename(d)
			prof['type'] = _find_browser_profile_type(prof)
			prof['icon'] = _find_browser_profile_icon(prof)
			prof_list.append(prof)

	return prof_list
# end-def

#
def _find_browser_profile_icon(prof):

	# print("Icon: " + prof['path'])

	# Default Icon
	icon = Gtk.IconTheme.get_default().load_icon(ICON, ICON_SIZE, 0)

	if "chrome" == prof['type']:
		icon = Gtk.IconTheme.get_default().load_icon("google-chrome", ICON_SIZE, 0)

	# Firefox Icon
	if "firefox" == prof['type']:
		icon = Gtk.IconTheme.get_default().load_icon("firefox-bin", ICON_SIZE, 0)

	# Specific Icon
	file = prof['path'] + "/icon.png"
	if os.path.isfile(file):
		print("With Icon File: " + file)
		icon = Pixbuf.new_from_file(file)

	icon0 = icon.scale_simple(ICON_SIZE, ICON_SIZE, 2)

	return icon0
# end-def

#
def _find_browser_profile_type(prof):

	# Old Chrome
	if os.path.isfile(prof['path'] + "/Profile 1/README"):
		return "chrome"

	# New Chrome
	if os.path.isfile(prof['path'] + "/Default/README"):
		return "chrome"

	# Firefox
	if os.path.isfile(prof['path'] + "/key3.db"):
		return "firefox"

	return "chrome"

# end-def
