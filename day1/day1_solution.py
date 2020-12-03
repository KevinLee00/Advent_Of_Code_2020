file = open("day1_input.txt", "r")

def naiveFindPair(file, x):
    data = file.read().splitlines()
    for i in range(len(data)):
        for j in range(1,len(data)):
            num_i = int(data[i])
            num_j = int(data[j])
            sum = num_i + num_j
            if sum == x:
                return num_i * num_j


def naiveFindTrio(file, x):
	data = file.read().splitlines()
	for i in range(len(data)):
		for j in range(1,len(data)):
			for k in range(2,len(data)):
				num_i = int(data[i])
				num_j = int(data[j])
				num_k = int(data[k])
				print(num_i + num_j + num_k)
				if num_i + num_j + num_k == x:
					return num_i * num_j * num_k

# pair = findPair(file, 2020)
# print(pair)
# print(pair[0] * pair[1])

trio = findTrio(file, 2020)
print(trio)
print(trio[0] * trio[1] * trio[2])