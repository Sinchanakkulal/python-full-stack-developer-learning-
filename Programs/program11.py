#v-number of vehicle(2 wheeler(TW) and four wheeler(FW))
#w=number of wheels

v = int(input())
w= int(input())

# v=TW + FW
# w= 2*TW + 4*FW
# Solving: FW = (w - 2*v) / 2 and TW = v - FW
FW = (w - 2*v) // 2
TW = v - FW
print(TW)
print(FW)


