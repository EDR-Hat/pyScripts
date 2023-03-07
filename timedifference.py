import sys

if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' startTimestamp endTimestamp')
    exit()

start = sys.argv[1]
end = sys.argv[2]

mid = []

while len(start) < len(end):
    start = "00:" + start 

start = start.split(':')
end = end.split(':')
start.reverse()
end.reverse()

carry = False
val = 0
for i in range(2):
    val = int(end[i]) - int(start[i])
    if carry:
        val = val - 1
        carry = False
    if val < 0:
        carry = True
        val = val + 60
    mid.append(val)
if len(end) > 2:
    val = int(end[2]) - int(start[2])
    if carry:
        val = val - 1
    carry = False
    mid.append(val)

mid.reverse()

for t in range(len(mid)):
    if(t == 0):
        print(mid[t], end='')
    else:
        print(':' + str(mid[t]), end='')
print('')
