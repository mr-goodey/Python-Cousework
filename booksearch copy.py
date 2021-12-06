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

def numberOfBooks(title):
    """This function calculates the number of books based on the title"""
    books=getBooks()
    count=0
    for book in books:
        if book[2]==title:
            count=count+1
    return count

def findBook(title):
    """This function returns appropriate information about books with a certain title\
    If there is more than 1 book it returns list of information that can differ"""
    books=getBooks()
    if numberOfBooks(title)>1:
        ids=[]
        genres=[]
        titles=[]
        authors=[]
        dates=[]
        members=[]
        for book in books:
            if book[2]==title:
                ids.append(book[0])
                genres.append(book[1])
                titles.append(book[2])
                authors.append(book[3])
                dates.append(book[4])
                members.append(book[5])
        return("ID: "+str(ids)+"\n\
Genre: "+genres[0]+"\n\
Title: "+titles[0]+"\n\
Author: "+authors[0]+"\n\
Purchase Date: "+dates[0]+"\n\
Member ID: "+str(members))
    elif numberOfBooks(title)==1:
        ids=[]
        genres=[]
        titles=[]
        authors=[]
        dates=[]
        members=[]
        for book in books:
            if book[2]==title:
                ids.append(book[0])
                genres.append(book[1])
                titles.append(book[2])
                authors.append(book[3])
                dates.append(book[4])
                members.append(book[5])
        return("ID: "+ids[0]+"\n\
Genre: "+genres[0]+"\n\
Title: "+titles[0]+"\n\
Author: "+authors[0]+"\n\
Purchase Date: "+dates[0]+"\n\
Member ID: "+members[0])
    else:
        return("This book is not in the system")

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

def numberOfDays1(book_id):
    """This function returns the number of days a book has been on loan for\
    If it not on loan it returns 0 so that the exceeding60 function works"""
    loans=getLoans()
    if onLoanLogfile(book_id)==False:
        return 0
    else:
        loans=getLoans()
        for loan in loans:
            if loan[0]==book_id:
                if loan[2]=='0':
                    x=loan[1]
                    y=x.split("/")
        from datetime import date
        f_date=date(int(y[2]),int(y[1]),int(y[0]))
        year=int(input("Current Year: "))
        month=int(input("Current Month: "))
        day=int(input("Current Day: "))
        l_date=date(year,month,day)
        number=l_date-f_date
        return(number.days)

def exceeding60(title):
    """Returns an appropriate message if a book has been on loan for more than 60 days"""
    ids=[]
    books=getBooks()
    for book in books:
        if book[2]==title:
            ids.append(book[0])
    for book_id in ids:
        if numberOfDays1(book_id)>60:
            return("Book "+book_id+" has been on loan for more than 60 days!")
        else:
            return("")

def booksearch():
    """This provides the desired functionality"""
    books=getBooks()
    loans=getLoans()
    title=input("Search for...\n")
    print(findBook(title))
    print(exceeding60(title))

'''
books=[]
print(getBooks())
print(numberOfBooks("Berserk"))
print(numberOfBooks("Dune"))
print(numberOfBooks("abc"))
print(findBook("Berserk"))
print(findBook("Dune"))
print(findBook("abc"))
loans=[]
print(getLoans())
print(onLoanLogfile("5"))
print(onLoanLogfile("4"))
print(numberOfDays1("5"))
print(numberOfDays1("4"))
print(exceeding60("Dune"))
print(exceeding60("Gone Girl"))
print(exceeding60("a"))
booksearch()
'''
#Tests for previous functions
