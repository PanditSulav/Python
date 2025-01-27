f=open("percentage.txt", "w")
def per(tot):
    num = tot/500*100
    return num
staa =int(input("Enter Business Statistes Number:"))
eng = int(input("Enter English Number:"))
man = int(input("Enter principle of management Number:"))
acc = int(input("Enter Financial Account Number:"))
eco = int(input("Enter Micro Economics Number:"))
if staa>=40 and eng>=40 and man>=40 and acc>=40 and eco>=40:
    tot=sum((staa,eng,man,acc,eco))
    print("Total Number", tot)
    x = per(tot)
    print("Total Percentage:", round(x,2))
    print("You Passed")
else:
    print("You Failed")
f.close()