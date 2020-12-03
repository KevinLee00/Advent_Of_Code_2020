import sys
import re
import time
sys.path.append("..")

from utilFunctions import extractData


data = extractData("day2_input.txt")


# Input: 2-3 w: gvwcvrggjbk
# Output: [2, 3, w, gvwcvrggjbk]
def extractPasswordInfo(string):
	return re.search("(\d+)-(\d+)\s(\S):\s(.+)", string).groups()

def countCharactersInString(char, string):
	charCount = 0
	for c in string:
		if c == char:
			charCount = charCount + 1
	return charCount

def isPasswordValid(minOccurences, maxOccurances, letter, password):
	letterCount = countCharactersInString(letter, password)
	if minOccurences <= letterCount and letterCount <= maxOccurances:
		return True
	return False

def isPasswordValid2(position1, position2, letter, password):
	if (password[position1 - 1] == letter) ^ (password[position2 - 1] == letter): # Logical XOR
		return True
	return False	

def main():
	validPasswordCount = 0
	for line in data:
		info = extractPasswordInfo(line)
		if isPasswordValid2(int(info[0]), int(info[1]), str(info[2]), str(info[3])):
			validPasswordCount = validPasswordCount + 1

	print validPasswordCount

if __name__ == "__main__":
    main()