
k = None
s = None
m = 0
T = []
R = []
output = 'NO'
SIGMA = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
GAMMA = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
indexMapping = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
    'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
    'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
    'Y': 24, 'Z': 25
}



filename = r'C:\Users\Lenovo\Downloads\test02.swe'
#filename = input()

with open(filename, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]  # remove blank lines if any are prescent

k = int(lines[0])
s = lines[1]
T = lines[2:2 + k]
R = []
for line in lines[2 + k:]:
    if ":" in line:
        _, values = line.split(":", 1)
        items = [v.strip() for v in values.split(",") if v.strip()]
        R.append(items)
        m += 1
		


for i in range(k):
    if len(T[i]) > len(s):  #if a T_i value is longer than s, there is no possible solution where the expansion can be a subset of s
        output = 'NO'
        break
    for letter in T[i]:  #checking that all letters in all T_i's are in either SIGMA or LAMBDA
        if letter not in (SIGMA or GAMMA):
            output = 'NO'
            break
	
		
for j in range(m):
    for r_i in R[j]:
        for letter in r_i:
            if letter not in SIGMA: #checking that all letters in all R_j's are in SIGMA
                output = 'NO'
                break



#desiscion 
def Decision(X):   #X is a list of choices of r_j from each R_j in order
    for i in range(k):
        T_i = ''
        for letter in T[i]:
            if letter in GAMMA:
                T_i += expansion(letter, X)
            else:
                T_i += letter
        if T_i in s:
            continue
        else: 
            return False, []
    return True, X


def expansion(letter, X):
	index = indexMapping[letter]
	return X[index]

		 
#brute force approach

indicies = [] 
for i in range(m):
	indicies.append(0)

while True:
	#make current combination
	current_combination = []
	for i in range(m):
		current_combination.append(R[i][indicies[i]])
	
	#test current combination
	if (Decision(current_combination)[0]):
		output = 'YES'
		print('YES')
		print(Decision(current_combination)[1])
		break
	
	#increment indicies to next combination
	pos = m-1
	while pos >= 0:
		indicies[pos] = indicies[pos] + 1
		if indicies[pos] < len(R[pos]):
			break
		else:
			indicies[pos] = 0
			pos = pos - 1
	if pos < 0:
		break
		
		
if output == 'NO':
	print('NO')











