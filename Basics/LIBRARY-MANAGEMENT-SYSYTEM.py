class student:
    name = []
    id = []
    issued = 0
    fine = 0.0

class book:
    id =  []
    title = []
    author = []
    total = None
    avalible = None

class Issue:
    bookid = None
    studentid = None
    returned = True

class Library:
    list[student] = None
    