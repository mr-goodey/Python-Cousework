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

def onLoanLogfile(book_id):
    """This function determines if the book is on loan according to the logfile"""
    loans=getLoans()
    for loan in loans:
        if loan[0]==book_id:
            if loan[2]=='0':
                return True
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

def updateDatabase2(book_id,username):
    """This function updates the database appropriately by changing the member ID"""
    books=getBooks()
    if onLoanDatabase(book_id)==False:
        return("Sorry, this book is already available")
    else:
        for book in books:
            if book[0]==book_id:
                book[5]="0"
        f=open("database.txt","w")
        for book in books:
            f.write(book[0]+":"+book[1]+":"+book[2]+":"+book[3]+":"+book[4]+":"+book[5]+"\n")
        return("Done")

def updateLogfile2(book_id,username,day,month,year):
    """This function updates the logfile appropriately by changing the date returned"""
    loans=getLoans()
    if onLoanLogfile(book_id)==False:
        return("Sorry, this book is already available")
    else:
        for loan in loans:
            if loan[0]==book_id:
                if loan[2]=="0":
                    loan[2]=(str(day)+"/"+str(month)+"/"+str(year))
        f=open("logfile.txt","w")
        for loan in loans:
            f.write(loan[0]+":"+loan[1]+":"+loan[2]+"\n")
        return("Done")

def numberOfDays3(book_id,l_date):
    """This returns a list that will be converted to a date"""
    loans=getLoans()
    date=[]
    for loan in loans:
        if loan[0]==book_id:
            if loan[2]=='0':
                x=loan[1]
                y=x.split("/")
                date.append(y[0])
                date.append(y[1])
                date.append(y[2])
    return date

def numberOfDays4(book_id,l_date):
    """This returns an appropriate message if a book has been on loan for too long"""
    y=numberOfDays3(book_id,l_date)
    if y==[]:
        return("")
    else:
        from datetime import date
        f_date=date(int(y[2]),int(y[1]),int(y[0]))
        number=l_date-f_date
        if number.days>60:
            return("This book is being returned after "+str(number.days)+" days!")
        else:
            return("")

def relevantUsername(book_id,username):
    """This determines if a username is currently associated with a book"""
    books=getBooks()
    for book in books:
        if book[0]==book_id and book[5]==username:
            return True
    return False
    
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

def bookreturn():
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
        if onLoanDatabase(book_id)==True and onLoanLogfile(book_id)==True:
            if relevantUsername(book_id,username)==True:
                print(numberOfDays4(book_id,l_date))
                updateDatabase2(book_id,username)
                clean_file("database.txt")
                updateLogfile2(book_id,username,day,month,year)
                clean_file("logfile.txt")
                print("Done")
            else:
                print("Sorry, you cannot return this book")
        else:
            print("Sorry, this book is already available")
    else:
        print("Error")

'''
books=[]
print(getBooks())
loans=[]
print(getLoans())
print(validID("1"))
print(validID("11"))
print(validUsername("abcd"))
print(validUsername("ABCD"))
print(validUsername("abc"))
print(validUsername("1234"))
print(onLoanLogfile("1"))
print(onLoanLogfile("2"))
print(onLoanDatabase("1"))
print(onLoanDatabase("2"))
year=int(input("Current Year: "))
month=int(input("Current Month: "))
day=int(input("Current Day: "))
l_date=currentDate(day,month,year)
print(updateDatabase2("1","abcd"))
clean_file("database.txt")
print(updateDatabase2("2","abcd"))
clean_file("database.txt")
print(updateLogfile2("1","abcd",day,month,year))
clean_file("logfile.txt")
print(updateLogfile2("2","abcd",day,month,year))
clean_file("logfile.txt")
print(numberOfDays3("5",l_date))
print(numberOfDays3("2",l_date))
print(numberOfDays4("5",l_date))
print(numberOfDays4("2",l_date))
print(relevantUsername("5","abcd"))
print(relevantUsername("5","asdf"))
print(currentDate(day,month,year))
bookreturn()
'''
#Tests for previous functions
