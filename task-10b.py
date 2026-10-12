# Library Knowledge Base

books = {
    "Python_Basics": "John",
    "AI_Fundamentals": "Hemanth",
    "Java_Programming": "Uday"
}

title = input("Enter book title: ")

if title in books:
    print("Author:", books[title])
else:
    print("Book not found")
