
import os
import csv
#read in file with standard syntax
dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path,'PyBank_data.csv')
#create month list, PL list, and PL chg list
Months = []
PL = []
PLChg = []
PLSum = 0
idx = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
#ignore headers for iteration
# #format PL as float from string 
#months 1st col and PL 2nd col
    for x in csvreader:
        if idx > 0:
            Months.append(x[0])
            PL.append(float(x[1]))
        idx = idx + 1   

#PLSum = 0. 
#iterate through legnth of PL for PL and PL change totaling. PLM1 getting the MoM chg in PL
for i in range(len(PL)):
    PLSum +=  PL[i]
    PLT = PL[i]
    PLM1 = PL[i-1]
    PLChg.append(PLT - PLM1)
    
           
#print(len(PL))
print(Months)
#print(PLSum)
#print(PLChg)

print("")
print("")
print("Financial Analysis")
#print("")
print("")
print(("Number of months:  ") + str(len(PL)))

#print(PLChg)
print((" Total PL:   ")+ str(PLSum))

#summary calcs plus print statements

Average = PLSum / len(PL)

print(("Average ....")+ str(Average))
MaxChange = max(PLChg)
print(("Max Change....")+ str(MaxChange))
#print(MaxChange)
MinChange = min(PLChg)
print(("Min Change....")+ str(MinChange))
#print(MinChange)


dir_path = os.path.dirname(os.path.realpath(__file__))
output_file = os.path.join(dir_path, "output.csv")

with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerows(Months)
    #writer.writerows(PLSum)
    #writer.writerows(Average)
    #writer.writerows(MaxChange)
    #writer.writerows(MinChange)





    

