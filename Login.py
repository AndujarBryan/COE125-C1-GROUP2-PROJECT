import csv

def LoginLogic(un, pw):
    print("LoginLogic")
    login = False

    while login == False:
        data=[]
        with open("file.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        print(data)
                
                
        col0 = [x[0] for x in data]
        col1 = [x[1] for x in data]
                
        if un in col0:
                    
            for k in range (0, len(col0)):
                if col0[k] == un and col1[k] == pw:
                    return 1
                    print("You are logged in")
                    login = True
                
        else:
            print("Wrong username or password")
            return 0
