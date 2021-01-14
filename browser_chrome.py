#
# Launch Chrome
#

import os

#
#
def launch(prof, args=None):

	print("browser_chrome.launch()")

	cmd = []
	cmd.append("google-chrome-stable")
	cmd.append("--password-store=basic")
	cmd.append("--user-data-dir=" + prof['path'])

	if (args['private']):
		cmd.append("--incognito")
	#end-if

	#cmd.append("--kiosk")
	if (args['link']):
		cmd.append(args['link'])
	#end-if

	cmd.append(">/dev/null")
	cmd.append("2>&1")
	cmd.append("&")

	cmd = " ".join(cmd)

	print(cmd)

	os.system(cmd)

#end-def
