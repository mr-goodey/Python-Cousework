def getBooks():
    """This function reads the database and returns a list of each entry"""
    books=[]
    f=open("database.txt","r")
    for line in f:
        s=line.strip()
        book=s.split(":")
        books.append(book)
    return books
    f.close()

def validUsername(username):
    """This function determines whether or not a username is valid"""
    valid=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',\
           'r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H',\
           'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',\
           'Z']
    user_name=list(username)
    if len(user_name)==4:
        for i in range(4):
            if user_name[i] in valid:
                return True
            else:
                return False
    return False

def onLoanDatabase(book_id):
    """This function determines if the book is on loan according to the database"""
    books=getBooks()
    members1=[]
    members2=['0']
    for book in books:
        if book[0]==book_id:
            members1.append(book[5])
    if members1!=members2:
        return True
    else:
        return False

def updateDatabase1(book_id,username):
    """This function updates the database appropriately by changing the member ID"""
    books=getBooks()
    if onLoanDatabase(book_id)==True:
        return("Sorry, this book is already on loan")
    else:
        for book in books:
            if book[0]==book_id:
                book[5]=username
        f=open("database.txt","w")
        for book in books:
            f.write(book[0]+":"+book[1]+":"+book[2]+":"+book[3]+":"+book[4]+":"+book[5]+"\n")
        return("Done")

def getLoans():
    """This function reads the logfile and returns a list of each entry"""
    loans=[]
    f=open("logfile.txt","r")
    for line in f:
        s=line.strip()
        loan=s.split(":")
        loans.append(loan)
    return loans
    f.close()

def onLoanLogfile(book_id):
    """This function determines if the book is on loan according to the logfile"""
    loans=getLoans()
    for loan in loans:
        if loan[0]==book_id:
            if loan[2]=='0':
                return True
    return False

def numberOfDays2(book_id,l_date):
    """This function returns the number of days a book has been on loan for\
    If it not on loan it returns 0 so that the user60Plus function works"""
    loans=getLoans()
    if onLoanLogfile(book_id)==False:
        return 0
    else:
        for loan in loans:
            if loan[0]==book_id:
                if loan[2]=='0':
                    x=loan[1]
                    y=x.split("/")
        from datetime import date
        f_date=date(int(y[2]),int(y[1]),int(y[0]))
        number=l_date-f_date
        return(number.days)

def validID(book_id):
    """This function determines if a book ID is valid"""
    books=getBooks()
    ids=[]
    for book in books:
        ids.append(book[0])
    if book_id in ids:
        return True
    else:
        return False

def updateLogfile1(book_id,l_date,day,month,year):
    """This function updates the logfile appropriately by adding a new line"""
    if onLoanLogfile(book_id)==True:
        return("Sorry, this book is already on loan")
    else:
        f=open("logfile.txt","a")
        f.write("\n"+book_id+":"+str(day)+"/"+str(month)+"/"+str(year)+":0")
        return("Done")

def user60Plus(username,l_date):
    """Returns an appropriate message if a book has been on loan for more than 60 days"""
    books=getBooks()
    member=[]
    excess=[]
    for book in books:
        if book[5]==username:
            member.append(book[0])
    for book_id in member:
        if numberOfDays2(book_id,l_date)>60:
            excess.append(book_id)
    if len(excess)==0:
        return("")
    if len(excess)==1:
        return("Book "+str(excess[0])+" has been on loan for more than 60 days")
    else:
        return("Books "+str(excess)+" have been on loan for more than 60 days")

def currentDate(day,month,year):
    """Converts inputs, day, month, year, into a date"""
    from datetime import date
    l_date=date(year,month,day)
    return l_date

def clean_file(filename):
    """Removes final \n from the file"""
    def is_all_whitespace(line):
        for char in line:
            if char != ' ' and char != '\n':
                return False
        return True
    with open(filename, 'r') as file:
        file_out = []
        for line in file:
            if is_all_whitespace(line):
                line = '\n'
            file_out.append(line)
    while file_out[-1] == '\n':
        file_out.pop(-1)
    if file_out[-1][-1] == '\n':
        file_out[-1] = file_out[-1][:-1]
    with open(filename, 'w') as file:
        file.write(''.join(file_out))

def bookcheckout():
    """This provides the desired functionality"""
    year=int(input("Current Year: "))
    month=int(input("Current Month: "))
    day=int(input("Current Day: "))
    l_date=currentDate(day,month,year)
    books=getBooks()
    loans=getLoans()
    username=input("Username: ")
    book_id=input("Book ID: ")
    if validUsername(username)==True and validID(book_id)==True:
        if onLoanDatabase(book_id)==False and onLoanLogfile(book_id)==False:
            updateDatabase1(book_id,username)
            clean_file("database.txt")
            updateLogfile1(book_id,l_date,day,month,year)
            clean_file("logfile.txt")
            print("Done")
            print(user60Plus(username,l_date))
        else:
            print("Sorry this book is currently on loan")
            print(user60Plus(username,l_date))
    else:
        print("Error")

'''
books=[]
print(getBooks())
print(validUsername("abcd"))
print(validUsername("ABCD"))
print(validUsername("abc"))
print(validUsername("abcd1"))
print(onLoanDatabase("1"))
print(onLoanDatabase("2"))
print(updateDatabase1("1","asdf"))
clean_file("database.txt")
print(updateDatabase1("2","asdf"))
clean_file("database.txt")
loans=[]
print(getLoans())
print(onLoanLogfile("1"))
print(onLoanLogfile("2"))
year=int(input("Current Year: "))
month=int(input("Current Month: "))
day=int(input("Current Day: "))
l_date=currentDate(day,month,year)
print(numberOfDays2("5",l_date))
print(numberOfDays2("2",l_date))
print(validID("1"))
print(validID("11"))
print(updateLogfile1("1",l_date,day,month,year))
clean_file("logfile.txt")
print(updateLogfile1("2",l_date,day,month,year))
clean_file("logfile.txt")
print(user60Plus("abcd",l_date))
print(user60Plus("asdf",l_date))
print(user60Plus("efgh",l_date))
print(currentDate(day,month,year))
bookcheckout()
'''
#Tests for previous functions
