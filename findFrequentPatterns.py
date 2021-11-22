def generateChampCombo(frequentSet):
    champs = []
    i = 0
    j = 0
    for c in frequentSet:
        for c2 in frequentSet:
            if(j > i):
                champs.append(c + ", " + c2)
            
            j += 1;
        
        i += 1
        j = 0
        
    return champs

#this is very inefficient due to the nested loops searching for duplicates
def sanitizeCombo(champs, rotation): 
    res = []
    for i in champs:
        sanitizer = {}
        check = i.split(", ")
        entry = ""
        for j in check:
            if(sanitizer.get(j, None) == None):
                entry = entry + j + ", "
            
            sanitizer[j] = 1
        
        if(len(sanitizer) == rotation):
            res.append(entry)
            
    result = []
    for i in res:
        result.append(i[:-2])
    
    remove = True
    for i in range(len(result) - 1):
        check = result[i].split(", ")
        for j in range(i+1, len(result)):
            for f in check:
                if(f not in result[j].split(", ")):
                    remove = False
                    break
                
                remove = True
                
            if(remove):
                remove = True
                result[j] = ""
    
    res = []
    for i in result:
        if (i != ""):
            res.append(i)
            
    return res   
if __name__ == '__main__':
    #the dictionary item that stores the champions
    frequentSet = {
    
    }
    
    #this is the table of all games and champions
    table = []
    
    #open data retrieved from games and put them in an initial dictionary
    #ready to be pruned according to the maximum support
    while(True):
        try:
            file = input("please enter data file name: ")
            f = open(file, "r")
            break
        except:
            print("an error occurred please check for spelling mistakes or if the file exists in the same directory\n")
            
    red = f.readline();
    while(red != ""):
        champs = red.split(",")
        champs = champs[5:]
        del champs[6]
        del champs[0]
        del champs[5]
        champs[9] = champs[9][:-2]
        table.append(champs[0:6])
        
        table.append(champs[6:11])
        
        
        for i in champs:
            frequentSet[i] = frequentSet.get(i, 0) + 1
        
        red = f.readline();
        
    f.close()
    #print(table)   
    #this while loop gets minimum support from the user
    #it also ensures the value is >= 1
    while(True):
        try:
            minimumSupport = int(input("please enter the minimum suppport: "))
            if(minimumSupport > 0):
                break
            else:
                print()
                print("invalid input...")
                print("please enter an integer > 0") 
                print()
        except:    
            print()
            print("invalid input...")
            print("please enter an integer > 0") 
            print()
    
    
    champs = []
    
    frequentSet = {f:frequentSet[f] for f in frequentSet if (frequentSet.get(f, 0)) >= minimumSupport}
    
    print()
    d = open("frequentChampions.txt", "w")
    d.write(str(frequentSet))
    d.write("\n\n")
    print(frequentSet)
    
    champs = generateChampCombo(frequentSet)
    champs = sanitizeCombo(champs, 2)
    
    frequentSet = {}
    #make new frequent item set 
    for i in champs:
        x2 = i.split(", ")
        for j in table:
            if(all(x in j for x in x2)):
                frequentSet[i] = frequentSet.get(i, 0) + 1

    frequentSet = {f:frequentSet[f] for f in frequentSet if (frequentSet.get(f, 0)) >= minimumSupport} 
           
    print()
    d.write(str(frequentSet))
    d.write("\n\n")
    print(frequentSet)

    counter = 3
    
    while(frequentSet != {} and counter < 6):
        champs = generateChampCombo(frequentSet)
        champs = sanitizeCombo(champs, counter)
    
        frequentSet = {}
        #make new frequent item set 
        for i in champs:
            x2 = i.split(", ")
            for j in table:
                if(all(x in j for x in x2)):
                    frequentSet[i] = frequentSet.get(i, 0) + 1
    
        frequentSet = {f:frequentSet[f] for f in frequentSet if (frequentSet.get(f, 0)) >= minimumSupport}        
        print()
        d.write(str(frequentSet))
        d.write("\n\n")
        print(frequentSet)
    
        counter += 1
        
    d.close()