log_file = open("um-server-01.txt") #this line is opening um-server-01.txt and saving it to a variable to be access later.


def sales_reports(log_file): #this line is creating a function via def declaration, naming function sales_reports
    for line in log_file: # setting up a for loop for every row of data in the linked file
        line = line.rstrip() #this sets value of line to line.rstrip() which removes any trailing characters
        day = line[0:3] # declaring variable named day, which is the characters of line from index 0 to index 3
        if day == "Tue": # if statement checking if variable day is equal to string of 'Tue'
            print(line) # if so print that line it came cfrom


sales_reports(log_file) #this is calling the created function over the linked file / database


