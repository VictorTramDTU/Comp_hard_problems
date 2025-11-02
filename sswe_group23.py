import time
import sys
from functools import partial

verbose = len(sys.argv) > 1 and sys.argv[1] in ('-v', '--verbose')

if verbose:
    debug = partial(print, file=sys.stderr)
else:
    def debug(*args, **kwargs):
        pass

k = None
s = None
m = 0
T = []
R = []
output = 'unknown'

SIGMA = [chr(i) for i in range(ord('a'), ord('z') + 1)]
GAMMA = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

lines = []
try:
    while True:
        lines.append(input())
except EOFError:
    pass

lines = [line for line in lines if line]

k = int(lines[0])
s = lines[1] if len(lines) > 2 else ""
T = lines[2:2 + k]
R = []

# a set of all elements of gamma that appear in any of the t_i strings
gammas_used = {c for t in T for c in t}
# maps an element of gamma to its index in R
gamma2index = {}
for line in lines[2 + k:]:
    if ":" in line:
        t, values = line.split(":", 1)
        if t not in gammas_used:
            # no t_i uses this element of gamma, so just disregard it.
            continue
        gamma2index[t] = m
        # associate with R[i] the set of possible extensions, except those that are not subsets 
        items = [v.strip() for v in values.split(",") if v.strip() and v in s]
        R.append(items)
        m += 1

# --- sanity checks ---
# check that each t_i is shorter than s (otherwise it cannot be a substring), and that all characters of t_i are in GAMMA or SIGMA.
for i in range(k):
    if len(T[i]) > len(s):
        output = 'NO'
        break
    for letter in T[i]:
        if letter not in GAMMA and letter not in SIGMA:
            output = 'NO'
            break

# check that all possible extensions for each element of GAMMA consist only of characters from SIGMA.
for j in range(m):
    for r_i in R[j]:
        for letter in r_i:
            if letter not in SIGMA:
                output = 'NO'
                break

# check that each r_i has at least one possible extension (otherwise it is trivially a NO instance)
for j in range(m):
    if len(R[j]) == 0:
        output = 'NO'
        break

# decision function
def decision(current_combination):
    for i in range(k):
        T_i = ''
        for letter in T[i]:
            if letter in GAMMA:
                T_i += expansion(letter, current_combination)
            else:
                T_i += letter
        if T_i not in s:
            return False
    return True


def expansion(letter, current_combination):
    index = gamma2index[letter]
    return current_combination[index]

# brute force approach


# --- brute-force search ---
indices = [0 for _ in range(m)]

start = time.time()

while output != 'NO':
    # make current combination. Maps an index into R to the expansion for the corresponding element of gamma.
    current_combination = [R[i][indices[i]] for i in range(m)]

    # test current combination
    debug(current_combination)
    if decision(current_combination):
        output = 'YES'
        print('YES')
        solution = {list(gamma2index.keys())[i]: r for i, r in enumerate(current_combination)}
        for letter, exp in solution.items():
            print(letter + " --> " + exp)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds", file=sys.stderr)
        break

    # increment indices
    pos = 0
    while pos <= m - 1:
        indices[pos] += 1
        if indices[pos] < len(R[pos]):
            break
        else:
            indices[pos] = 0
            pos += 1
    if pos > m - 1:
        output = 'NO'
        break

if output == 'unknown' or output == 'NO':
    print('NO')
    end = time.time()
    print(f"Execution time: {end - start:.6f} seconds", file=sys.stderr)
