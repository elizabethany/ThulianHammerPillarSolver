import math

# Function to round the given value to the nearest specified interval
def roundToInterval(
    inputValue,
    interval
    ):
    
    return round (inputValue / interval) * interval

#  | h i j k
# -|--------
# 0|   1 2 3
# 1| 1 2   3
# 2| 2   2 1
# 3| 3 2 1  
mathsH = tuple((0, 1, 2, 3))
mathsI = tuple((1, 2, 0, 2))
mathsJ = tuple((2, 0, 2, 1))
mathsK = tuple((3, 2, 1, 0))

def getBlocks(
    ):

    print("Enter the # of rotations needed to get to the front for each of the following blocks: ")
    
    blockA = int(input("A: "))
    blockB = int(input("B: "))
    blockC = int(input("C: "))
    blockD = int(input("D: "))
    
    # P = mathsH, Q = mathsI, R = mathsJ, S = mathsK
    # 13 = 0, 14 = 1, 15 = 2, 16 = 3
    # E4 = blockA, F4 = blockB, G4 = blockC, H4 = blockD
    totalH = (mathsH[1] * blockB) + (mathsH[2] * blockC) + (mathsH[3] * blockD) # = (P14 * F4) + (P15 * G4) + (P16 * H4)
    totalI = (mathsI[0] * blockA) + (mathsI[1] * blockB) + (mathsI[3] * blockD) # = (Q13 * E4) + (Q14 * F4) + (Q16 * H4)
    totalJ = (mathsJ[0] * blockA) + (mathsJ[2] * blockC) + (mathsJ[3] * blockD) # = (R13 * E4) + (R15 * G4) + (R16 * H4)
    totalK = (mathsK[0] * blockA) + (mathsK[1] * blockB) + (blockC * mathsK[2]) # = (S13 * E4) + (S14 * F4) + (G4 * S15)
    
    # print(totalH)
    # print(totalI)
    # print(totalJ)
    # print(totalK)
    
    shotsA = math.fmod(totalH, 4)
    shotsB = math.fmod(totalI, 4)
    shotsC = math.fmod(totalJ, 4)
    shotsD = math.fmod(totalK, 4)
    
    print("These are the # of shots needed for each block: ")
    print("A: " + str(roundToInterval(shotsA, 1)))
    print("B: " + str(roundToInterval(shotsB, 1)))
    print("C: " + str(roundToInterval(shotsC, 1)))
    print("D: " + str(roundToInterval(shotsD, 1)))

print("\nBlocks rotate counter-clockwise\nBlock lettering starts from the top")
while True:
    getBlocks()