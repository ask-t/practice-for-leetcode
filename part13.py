s = "XIII"
result = 0
out = ""
sList = list(s)
length = len(sList)
# if(sList[0] == "I"):
#     if(sList[1] == "I"):
#         if (sList[2] == "I"):
#             result = 3
#     elif (sList[1] == "V"):
#         result = 4
#     elif (sList[1] == "X"):
#         result = 9

print(length)

try:
    for i in range(length):
        if(sList[i] == "M"):
            if(sList[i-1] == "C"):continue
            else: result += 1000
        elif(sList[i] == "C"):
            if(sList[i-1] =="X"): continue
            elif(sList[i+1] =="M"):
                result+= 900
            elif(sList[i+1] =="D"):
                result+=400;
            else: result+= 100
        elif(sList[i] == "D"):
            if(sList[i-1] =="C"):continue
            else: result+= 500
        elif(sList[i]== "X"):
            if(sList[i+1] == "C"):
                result+= 90
            elif(sList[i+1]== "L"):
                result+=40
            else: result+= 10
        elif(sList[i]== "L"):
            if(sList[i-1]=="X"):continue
            else: result+= 50
        elif(sList[i] == "V"):
            if(sList[i-1]=="I"):continue
            else: result+=5
        elif(sList[i]=="I"):
            if(sList[i+1]=="V"):result+=4
            else:result+=1
        print(result)
except:
    result+=1
print(result)


