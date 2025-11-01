import time

k = None
s = None
m = 0
T = []
R = []
output = 'unknown'

SIGMA = [chr(i) for i in range(ord('a'), ord('z')+1)]
GAMMA = [chr(i) for i in range(ord('A'), ord('Z')+1)]

filename = r'../test06.swe'
# filename = input()

with open(filename, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

k = int(lines[0])
s = lines[1]
T = lines[2:2 + k]
R = []

unique_Ts = {c for t in T for c in t}
indexMapping = {}
for line in lines[2 + k:]:
    if ":" in line:
        t, values = line.split(":", 1)
        if t not in unique_Ts: continue
        indexMapping[t] = m
        items = [v.strip() for v in values.split(",") if v.strip() and v in s]
        R.append(items)
        m += 1

for i in range(k):
    if len(T[i]) > len(s):
        output = 'NO'
        break
    for letter in T[i]:
        if letter not in GAMMA and letter not in SIGMA:
            output = 'NO'
            break

for j in range(m):
    for r_i in R[j]:
        for letter in r_i:
            if letter not in SIGMA:
                output = 'NO'
                break


# desiscion
def Decision(X):
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


# brute force approach

indices = [0 for _ in range(m)]

start = time.time()
while output != 'NO':
    # make current combination
    current_combination = [R[i][indices[i]] for i in range(m)]

    # test current combination
    print(current_combination)
    decision, X = Decision(current_combination)
    if decision:
        output = 'YES'
        print('YES')
        solution = {list(indexMapping.keys())[i]: r for i, r in enumerate(X)}
        for letter, exp in solution.items():
            print(letter + " --> " + exp)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        break

    # increment indices
    pos = 0
    while pos <= m - 1:
        indices[pos] = indices[pos] + 1
        if indices[pos] < len(R[pos]):
            break
        else:
            indices[pos] = 0
            pos = pos + 1
    if pos > m - 1:
        output = 'NO'
        break

if output == 'NO':
    print('NO')

    end = time.time()
    print(f"Execution time: {end - start:.6f} seconds")
