"""

   Fredrik Jansson

"""

# ================================
# =           Includes           =
# ================================

import datetime
import os

# ===============================
# =           Classes           =
# ===============================

class Logger:
	""" The different logging types. """
	

	DEFAULT, WARNING, INFORMATION, CRITICAL = 0, 1, 2, 3

	""" Path, path to logfile. removeIfExist = If true, deletes the file if it exists. """
	def __init__(self, path, removeIfExist = False):
		self.path = path
		if removeIfExist:
			if os.path.exists(path):
				os.remove(path)

	def getType(self, inType):
		if inType == 1:
			return "[WARNING]"
		elif inType == 2:
			return "[INFO]"
		elif inType == 3:
			return "[CRITICAL]"
		else:
			return "[DEFAULT]"

	def getTime(self):
		return "[" + str(datetime.datetime.now()) + "]"

	def log(self, info, type = DEFAULT):
		with open(self.path, "a") as f:
			f.write(self.getType(type) + ": " + self.getTime() + ": " + info + "\n")

# ====================================
# =           Main Section           =
# ====================================


if __name__ == "__main__":
	log = Logger("log.txt")
	log.log("Typeless log")
	log.log("Normal", log.DEFAULT)
	log.log("Warning text", log.WARNING)
	log.log("Information", log.INFORMATION)