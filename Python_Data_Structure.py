# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list.
#  Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, new_book): #This pulls from our list up top, and then uses the new book for what we try to add
    if new_book not in library: # if new book is not inside of library it will then initiate our append
        library.append(new_book)
        print(f"'{new_book[0]}' by {new_book[1]} added to the library!") # here I am using the indexs for what we enter in our tuple
    else:
        print(f"'{new_book[0]}' by {new_book[1]} is already in the library silly.") #This will grab the duplicate information we input for the tuple and places it here

add_book(library, ("The Jungle Book", "Johnny Noxville"))
add_book(library, ("1984", "George Orwell"))