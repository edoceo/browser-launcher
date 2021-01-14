#
# Launch Chrome
#

import os

def launch(prof, args=None):

	cmd = []
	cmd.append("links")
	cmd.append("-g") # Graphics Mode
	cmd.append(args['link'])
	cmd.append(">/dev/null")
	cmd.append("2>&1")
	cmd.append("&")

	cmd = " ".join(cmd)

	print(cmd)

	os.system(cmd)

#end-def
