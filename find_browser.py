#
# Find the Browser Profiles
#

import os
#import config
#base = os.path.dirname(os.path.realpath(__file__))

#os.get_exec_path

#
# List of available browsers
_find_browser_list = [
	"google-chrome-stable",
	"google-chrome-beta",
	"google-chrome-canary",
	"firefox-bin",
	"firefox",
	"midori",
	"opera",
	"opera-developer",
	"otter",
	"seamonkey",
	"seamonkey-bin",
	"vivaldi",
	"links"
	"lynx"
	"w3m"
]

def get_browser_list():

	browser_list = []

	path_list = os.get_exec_path()
	print(path_list)

	for b in sorted(_find_browser_list):
		for p in path_list:
			full_path = p + "/" + b
			print(full_path)
			if os.path.isdir(full_path):
				browser_list.append(full_path)

	return browser_list



	#end-for
#end-def
