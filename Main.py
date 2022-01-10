import time

X = 1#USED FOR SLEEP

# allow user to enter list of numbers ✔
# use 3 selectible algorithms to order them
#ALLOW UPLOAD OF DATA FILE 
# add UI maybe
def bubbleSort(nts):
 
    nts_len = len(nts)
 
    for i in range(nts_len):
        for p in range(nts_len - i - 1):
            if nts[p] > nts[p + 1]: # change to < for descending
                nts[p], nts[p + 1] = nts[p + 1], nts[p]
    return nts
                                
                

def Select_Sort():

    pass

def Insertion_Sort():
    def insertionSort(datarr):
        print("Just used insertion sort")
 
    for i in range(1, len(datarr)):
        current_num = datarr[i]
        p = i - 1
 
        while p >= 0 and datarr[p] > current_num:
            datarr[p + 1] = datarr[p]
            p -= 1
 
        datarr[p + 1] = current_num
    return datarr
    


#THIS IS PROBABLY NOT NEEDED ANYMORE
def list_maker(): #THIS MAKES USER INPUT INTO A LIST SO ITS EASIER TO WORK WITH, IT ALSO REMOVES THE  COMMAS
    list = data.split(",")
    print(list)
    pass
#THIS IS PROBABLY NOT NEEDED ANYMORE    



print("ENTER DATA LIKE THIS: 10,13,123,1234,45454")
time.sleep(X)#SLEEPS FOR X SECONDS MAKES THE USER HAVE TO READ LOL
nts = input("ENTER DATA TO BE SORTED ")
#nts.append(data)
#print(nts)

#f = open("unsorted.txt","w")#OPENS THE TXT FILE IN WRITE 
#f.write(data)#WRITES THE DATA TO THE FILES
#f.close()#CLOSES IT

time.sleep(X)#SLEEPS FOR X SECONDS MAKES THE USER HAVE TO READ LOL
#list_maker()#THIS MAKES USER INPUT INTO A LIST SO ITS EASIER TO WORK WITH, IT ALSO REMOVES THE  COMMAS

print("1 = Bubble")
print("2 = Select")
print("3 = Insertion")
time.sleep(X)

choice = input("WHAT ALGO WILL BE USED? ")

if choice == "1":
    #BUBBLE SORT
    nts = bubbleSort(nts)

    
elif "2":
    Select_Sort()
elif "3":
    Insertion_Sort()
