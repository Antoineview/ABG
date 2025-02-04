# -*- coding: utf-8 -*-
"""
Matrices: basics
"""


#-------------------------------------------------------------------------------
# 1.1 Displays

def printmat(M):
    for L in M:
        for e in L:
            print(e, end=' ')
        print()
    
################ BONUS     
def prettyprint(M, d=0):
    l = len(M)
    c = len(M[0])
    if d == 0:
        for line in M:
            for e in line:
                d = max(d, len(str(e))) # triche....
    line = ""
    for i in range(c*(d+3)+1):
        line = line + '-'
    for i in range(l):
        print(line)
        for j in range(c):
            s = "| {:" + str(d) + "d}"
            print(s.format(M[i][j]), end=' ')
        print('|')
    print(line)
    
#-------------------------------------------------------------------------------
# 1.2 Init

def init(l, c, val):
    '''
    Init a l x c matrix full of "val"
    '''
    M = []
    for i in range(l):
        M.append([])
        for j in range(c):
            M[i].append(val)
    return M

#-------------------------------------------------------------------------------

def __str2intlist(s):
    L = []
    (i, n) = (0, len(s))
    while i < n:
        word = ""
        while i < n and s[i] != ' ' and s[i] != '\n':
            word += s[i]
            i += 1
        L.append(int(word))
        i += 1
    return L

def load(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    M = []
    for line in lines:
        M.append(__str2intlist(line))
    return M
