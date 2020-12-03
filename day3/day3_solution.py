import sys
sys.path.append("..")
from utilFunctions import extractData

INPUT_FILE = "day3_input.txt"
data = extractData(INPUT_FILE)

def countTrees(x_increment, y_increment):
	x_pos = 0
	y_pos = 0
	patternWidth = len(data[0])
	treeCount = 0
	
	while y_pos < len(data):
		if data[y_pos][x_pos % patternWidth] == '#':
			treeCount = treeCount + 1
		x_pos = x_pos + x_increment
		y_pos = y_pos + y_increment
		
	return treeCount

def main():
	product = countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2)
	print product

if __name__ == "__main__":
    main()