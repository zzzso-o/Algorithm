import sys
sys.stdin = open("input1.txt")
input = sys.stdin.readline

# n=트럭의 개수, w=다리의 길이, L=다리의 최대하중
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

# bridge, weight를 만들어 주는 것이 포인트이다.
# bridge = 다리 위에 올라와있는 트럭들을 저장해줄 리스트
bridge = [0] * w
weight, time = 0, 0

while True:
    if not bridge:
        break
    out = bridge.pop(0)
    # 다리에서 트럭이 빠져나가면 그 무게만큼 빼준다.
    weight -= out

    if trucks:
        if weight + trucks[0] <= L:
            bridge.append(trucks[0])
            weight += trucks[0]
            trucks.pop(0)
        else:
            # 0을 추가하여 다리 위 트럭을 움직인다.
            bridge.append(0)
    time += 1

print(time)
