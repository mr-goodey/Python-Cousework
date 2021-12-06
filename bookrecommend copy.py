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

def getTitles(genre):
    """This function returns a list of titles for a particular genre"""
    books=getBooks()
    titles=[]
    for book in books:
        if book[1]==genre:
            titles.append(book[2])
    titles=list(dict.fromkeys(titles)) #This removes duplicates
    return titles

def getIDs1(title):
    """This creates a list of IDs for a particular book"""
    books=getBooks()
    ids_1=[]
    for book in books:
        if book[2]==title:
            ids_1.append(book[0])
    return ids_1

def getIDs2(genre):
    """This returns a list of lists of IDs"""
    titles=getTitles(genre)
    ids=[]
    for title in titles:
        ids.append(getIDs1(title))
    return ids

def numberOfTransactions1(book_id):
    """This returns the number of times a book has been on loan, book ID"""
    loans=getLoans()
    count=0
    for loan in loans:
        if loan[0]==book_id:
            count=count+1
    return count

def numberOfTransactions2(title):
    """This returns the total number of times a particular book has been on loan, title"""
    ids_1=getIDs1(title)
    count=0
    for book_id in ids_1:
        count=count+numberOfTransactions1(book_id)
    return count

def numberOfTransactions3(genre):
    """This returns a list of the number of transactions of each title in a genre"""
    titles=getTitles(genre)
    transactions=[]
    for title in titles:
        transactions.append(numberOfTransactions2(title))
    return transactions

def relevantGenres(username):
    """This returns a list of genres that a user is currently interested in"""
    books=getBooks()
    genres=[]
    for book in books:
        if book[5]==username:
            genres.append(book[1])
    genres=list(dict.fromkeys(genres))
    return genres

def combine(username):
    """This returns a dictionary of titles and number of loans for each relevant book"""
    genres=relevantGenres(username)
    titles=[]
    transactions=[]
    for genre in genres:
        titles=titles+getTitles(genre)
        transactions=transactions+numberOfTransactions3(genre)
    combination=zip(titles,transactions)
    combined=dict(combination)
    return combined

def sortedCombine(username):
    """This sorts the dictionary is descending order"""
    import operator
    combined=combine(username)
    sort_combined=dict(sorted(combined.items(),key=operator.itemgetter(1),reverse=True))
    return sort_combined

def limit(username):
    """This ensures the dictionary has no more than 10 pairs"""
    d=sortedCombine(username)
    if len(d)>10:
        d=d={k: d[k] for k in list(d.keys())[:3]}
    return d

def otherGenres(username):
    """This returns a list of all genres the user isn't intereseted in"""
    books=getBooks()
    genres=relevantGenres(username)
    all_genres=[]
    for book in books:
        all_genres.append(book[1])
    all_genres=list(dict.fromkeys(all_genres))
    for genre in genres:
        if genre in all_genres:
            all_genres.remove(genre)
    other_genres=all_genres
    return other_genres

def otherCombine(username):
    """This returns a dictionary of other titles and the number of transactions"""
    other_genres=otherGenres(username)
    other_titles=[]
    other_transactions=[]
    for genre in other_genres:
        other_titles=other_titles+getTitles(genre)
        other_transactions=other_transactions+numberOfTransactions3(genre)
    other_combination=zip(other_titles,other_transactions)
    other_combined=dict(other_combination)
    return other_combined

def otherSortedCombine(username):
    """This sorts the dictionary"""
    import operator
    other_combined=otherCombine(username)
    sort_combined=dict(sorted(other_combined.items(),key=operator.itemgetter(1),reverse=True))
    return sort_combined

def otherLimit1(username):
    """Most popular other book"""
    d=otherSortedCombine(username)
    d={k: d[k] for k in list(d.keys())[:1]}
    return d

def otherLimit2(username):
    """2 most popular other books"""
    d=otherSortedCombine(username)
    d={k: d[k] for k in list(d.keys())[:2]}
    return d

def otherLimit3(username):
    """3 most popular other books"""
    d=otherSortedCombine(username)
    d={k: d[k] for k in list(d.keys())[:3]}
    return d

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

def bookrecommend():
    """This provides the desired functionality"""
    books=getBooks()
    loans=getLoans()
    username=input("Username: ")
    if validUsername(username)==True:
        recommendations=limit(username)
        if len(recommendations)==0:
            recommendations.update(otherLimit3(username))
        elif len(recommendations)==1:
            recommendations.update(otherLimit2(username))
        elif len(recommendations)==2:
            recommendations.update(otherLimit1(username))
        else:
            recommendations=recommendations
        i=1
        for key in recommendations:
            print(str(i)+") "+key)
            i=i+1
    else:
        print("Invalid username")

'''
books=[]
print(getBooks())
loans=[]
print(getLoans())
print(getTitles("Fantasy"))
print(getIDs1("Berserk"))
print(getIDs1("Dune"))
print(getIDs2("Fantasy"))
print(getIDs2("Science Fiction"))
print(numberOfTransactions1("1"))
print(numberOfTransactions1("10"))
print(numberOfTransactions2("Dune"))
print(numberOfTransactions2("Berserk"))
print(numberOfTransactions3("Science Fiction"))
print(numberOfTransactions3("Adventure"))
print(relevantGenres("abcd"))
print(relevantGenres("efgh"))
print(combine("abcd"))
print(combine("efgh"))
print(sortedCombine("abcd"))
print(sortedCombine("efgh"))
print(limit("abcd"))
print(limit("efgh"))
print(otherGenres("abcd"))
print(otherGenres("aaaa"))
print(otherCombine("abcd"))
print(otherCombine("aaaa"))
print(otherSortedCombine("abcd"))
print(otherSortedCombine("aaaa"))
print(otherLimit1("abcd"))
print(otherLimit1("aaaa"))
print(otherLimit2("abcd"))
print(otherLimit2("aaaa"))
print(otherLimit3("abcd"))
print(otherLimit3("aaaa"))
print(validUsername("abcd"))
print(validUsername("ABCD"))
print(validUsername("abc"))
print(validUsername("1abc"))
bookrecommend()
'''
#Tests for previous functions
