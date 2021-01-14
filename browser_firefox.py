#
# Launch Firefox
#

import os

#
#
def launch(prof, args=None):

	print("browser_firefox.launch()")

	cmd = []
	cmd.append("firefox-bin")
	cmd.append("--profile " + prof['path'])
	#cmd.append("--new-tab " + url)
	#cmd.append("--new-window " + url)
	cmd.append(args['link'])
	cmd.append(">/dev/null")
	cmd.append("2>&1")
	cmd.append("&")

	cmd = " ".join(cmd)

	print(cmd)

	os.system(cmd)

	#return PID;
#end-def
