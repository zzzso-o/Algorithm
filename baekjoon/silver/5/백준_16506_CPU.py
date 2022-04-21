# 55

opcodes = {
    'ADD' : '0000',
    'SUB' : '0001',
    'MOV' : '0010',
    'AND' : '0011',
    'OR' : '0100',
    'NOT' : '0101',
    'MULT' : '0110',
    'LSFTL' : '0111',
    'LSFTR' : '1000',
    'ASFTR' : '1001',
    'RL' : '1010',
    'RR' : '1011',
}

N = int(input())
for _ in range(N):
    code = list(map(str, input().split()))
    result = []
    for i in opcodes:
        if code[0] == i:
            result.append(opcodes[i])
        if code[1] + 'c' == i:
            result.append(opcodes[i]+0)
