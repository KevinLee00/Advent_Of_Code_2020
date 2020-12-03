def extractData(file):
	file = open(str(file), "r")
	return file.read().splitlines()