# Western Suburbs Croquet Club
# PairList = input("Please input [Age,Handicap]")
def Check(PairList,What,Amount,Length):
    for i in range(Length):
        if PairList[i][What] < Amount:
            PairResult[i] = 'Open'

PairList = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]

Length = len(PairList)

PairResult = ['Senior']*Length

AgeCheck(PairList,0,55,Length)
AgeCheck(PairList,1,7,Length)

print(PairResult)
