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
    result = [0] * 16

    # 0~4
    for key in opcodes.keys():
        if code[0][-1] == 'c':
            if code[0][0:-1] == key:
                result[:5] = opcodes[key] + '1'
        elif code[0] == key:
            result[:5] = opcodes[key] + '0'

    # 6~8
    result[6:9] = bin(int(code[1]))

    # 9~11
    if code[2] != 0:
        result[9:12] = bin(int(code[2]))

    # 12~15
    if result[4] == 0:
        result[12:15] = bin(int(code[3])) + '0'
    else:
        result[12:15] = bin(int(code[3]))

    print(*result)