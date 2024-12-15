import json
import sys
from datetime import datetime
import uuid
import os

current_folder = os.getcwd()

print("Current Folder Path:", current_folder)
sys.path.insert(2, current_folder)

from Resources.Models.Client import Client
from Resources.Models.Book import Book
from Resources.Models.Librarian import Librarian
from Resources.Models.Order import Order
# from Models.Client import Client

def read_clients():
    with open("Resources/data/clients.json", "r") as f:
        clients_data = json.load(f)
    clients = [
        Client(
            
            client["phone_num"],
            client["id"],
            client["name"],
            client["age"],
            client["id_num"],
            client["address"],
            
            # Deserialize each order dictionary into an Order object
            [Order.from_dict(order) for order in client["reading_history"]],
            client["orders_num"],
        )
        for client in clients_data
    ]

    return clients

def read_librarian():

    with open("Resources/data/librarians.json" ,"r") as f:
        librarians_data = json.load(f)

    librarians = [
        Librarian(
            librarian["id"],
            librarian["name"],
            librarian["age"],
            librarian["id_num"],
            librarian["address"],
            librarian["phone_num"],
            librarian["emp_type"],  
        )
        for librarian in librarians_data
    ]
    
    return librarians

def read_orders():
    with open("Resources/data/orders.json", "r") as f:
        orders_data = json.load(f)

    orders = [
        Order(
            order["id"],
            order["date"],
            order["client_id"],
            order["book_id"],
            order["status"],
            order["order_type"],
            price=order.get("price")  #returns None if the key doesnt exist
        )
        for order in orders_data
    ]

    return orders

def read_books():
    with open("Resources/data/books.json", "r") as f:
        books_data = json.load(f)

    books = [
        Book(
            book["id"],
            book["title"],
            book["description"],
            book["author"],
            book["status"],
            book["categories"],
            book["ISBN"],
            book["image"],
            book["price"],
            book["quantity"],
            book["borrowable"],
            book["buyable"]
        )
        for book in books_data
    ]

    return books

#low to high
def sorted_books():
    sorted_books = sorted(books_data, key=lambda book: book.price)
    return sorted_books

#high to low
def sorted_books_desc():
    sorted_books_desc = sorted(books_data, key=lambda book: book.price, reverse=True)
    return sorted_books_desc

clients_data = read_clients()
librarians_data = read_librarian()
orders_data = read_orders()
books_data = read_books()
books_sorted_data = sorted_books()

def dump_to_json(objects, file_path):
    serialized_data = [obj.to_dict() for obj in objects]
    with open(file_path, "w") as f:
        json.dump(serialized_data, f, indent=4)

#done
def user_sign_in(id:str):
    dataset = clients_data if id.startswith("1") else librarians_data if id.startswith("2") else None
    #  if not dataset:
    #     print("Invalid ID prefix.")
    #     return None

    # if user:
    #     return user
    # else:
    #     print("User not found.")
    #     return None
    user = next((user for user in dataset if user.get_id() == id), None)

    return user

def generate_numeric_id(hieght=10):
    # Generate a UUID and convert it to an integer, then take the first `length` digits
    numeric_id = str(uuid.uuid4().int)[:hieght]
    return str(numeric_id)

def generate_user_id(user_type, egyptian_id):
    id_part = egyptian_id[-5:]
    unique = generate_numeric_id(3)
    if user_type == "client":
        prefix = "1"
    elif user_type == "librarian":
        prefix = "2"
    # else:
    #     raise ValueError("Invalid user type")
    return f"{prefix}{id_part}{unique}"

def is_valid_egyptian_id(id_num):
    governorates = {
    2: "Cairo",
    97: "Aswan",
    88: "Asyut",
    3: "Alexandria",
    64: "Ismailia",
    95: "Luxor",
    65: "Red Sea",
    45: "Behira",
    50: "Dakahlia",
    62: "Suez",
    55: "Sharkeya",
    15: "Tenth of Ramadan",
    40: "Gharbeya",
    84: "Fayoum",
    13: "Qalyubia",
    48: "Menoufia",
    86: "Minya",
    92: "Wadi El Gadeed - New Valley",
    82: "Beni Suef",
    66: "Port Said",
    69: "South Sinai",
    57: "Damietta",
    93: "Sohag",
    68: "North Sinai",
    96: "Qena",
    47: "Kafr El Sheikh",
    4: "Marsa Matrouh"
}
    # Step 1: Check if the ID has 14 digits
    if not id_num.isdigit() or len(id_num) != 14:
        return False, "Invalid format: ID must contain exactly 14 digits."
    
    # Step 2: Extract and validate the birth date
    century = {"2": "19", "3": "20"}
    first_digit = id_num[0]
    if first_digit not in century:
        return False, "Invalid century code in ID."
    
    year = century[first_digit] + id_num[1:3]
    month = id_num[3:5]
    day = id_num[5:7]

    try:
        birth_date = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
    except ValueError:
        return False, "Invalid birth date in ID."
    
    # Step 3: Validate governorate code
    governorate_code = int(id_num[7:9])
    if governorate_code not in governorates:
        return False, "Invalid governorate code in ID."
    

    return True,
#done
def client_sign_up(phone_num,name,age,id_num ,address):
    # if is_valid_egyptian_id(id_num):


    # existing_client = next((client for client in clients_data if client.id_num == id_num), None)
    # if existing_client:
    #     print(f"Error: A client with ID number {id_num} already exists.")
    #     return

    
    client_id = generate_user_id("client" , id_num)
    new_client = Client(
        phone_num=phone_num,
        id=client_id,
        name=name,
        age=age,
        id_num=id_num,
        address=address,
        reading_history=[],
        orders_num=0
    )
    clients_data.append(new_client)
    dump_to_json(clients_data , "Resources/data/clients.json")
    return new_client
    #show him his id
#done
def librarian_sign_up(name , age , id_num ,address , phone_num , emp_type):
    # if is_valid_egyptian_id(id_num):

    # existing_librarian = next((librarian for librarian in librarians_data if librarian.id_num == id_num), None)
    # if existing_librarian:
    #     print(f"Error: A librarian with ID number {id_num} already exists.")
    #     return

  
    librarian_id = generate_user_id("librarian" , id_num)
    new_librarian = Librarian(
        id=librarian_id,
        name=name,
        age=age,
        id_num=id_num,
        address=address,
        phone_num=phone_num,
        emp_type=emp_type
        
    )
    librarians_data.append(new_librarian)
    dump_to_json(librarians_data , "data/librarians.json")
    return new_librarian


# The next() function is used to find the first book in the books list that matches the given book_id.
# If a match is found, the next() function returns that book.
# If no match is found, the iterator is exhausted, and the next() function returns the default value None.

#done
def borrow_book(client:Client, book_id):
    # Check if the client is valid
    # if not client:
    #     print("Invalid client. Cannot borrow a book.")
    #     return

    # Step 1: Find the book in the system
    book = next((book for book in books_data if book.get_Book_id() == book_id), None)
    # if not book:
    #     print(f"Book with ID {book_id} could not be found.")
    #     return

    # Step 2: Check if the book is borrowable
    # if not book.borrowable:
    #     print(f"Book '{book.title}' is not available for borrowing.")
    #     return

    # Step 4: Create a new order
    order_id = generate_numeric_id()  
    new_order = Order(
        id=order_id,
        date=str(datetime.now()),
        client_id=client.get_id(),
        book_id=book_id,
        status="active",
        order_type="borrow"
    )

    orders_data.append(new_order)
    client.reading_history.append(new_order)
    client.orders_num += 1
    book.quantity -= 1

    dump_to_json(clients_data , "Resources/data/clients.json")
    dump_to_json(orders_data , "Resources/data/orders.json")
    dump_to_json(books_data , "Resources/data/books.json")

#done
def buy_book(client:Client , book_id):
    book = next((book for book in books_data if book.get_Book_id() == book_id), None)
    # if not book.buyable:
        #         print(f"Book '{book.title}' is not available for borrowing.")
        #         return
        #     if book.quantity <= 0:
        #         print(f"Book '{book.title}' is out of stock.")
        #         return
    order_id = generate_numeric_id()
    new_order = Order(
        id=order_id,
        date=str(datetime.now()),
        client_id=client.get_id(),
        book_id=book_id,
        status="active",
        order_type="buy",
        price = book.get_Book_price()
    )

    orders_data.append(new_order)
    client.reading_history.append(new_order)
    client.orders_num += 1
    book.quantity -= 1

    dump_to_json(clients_data , "Resources/data/clients.json")
    dump_to_json(orders_data , "Resources/data/orders.json")
    dump_to_json(books_data , "Resources/data/books.json")

#done
def client_orders(client:Client):
    return client.get_reading_history()


#done
def add_book(title,description,author,status, categories , ISBN , image , price , quantity , borrowable:bool , buyable:bool):
    book_id = generate_numeric_id()

    new_book = Book(
        id= book_id,
        title=title,
        description=description,
        author=author,
        status=status,
        categories=categories,
        ISBN=ISBN,
        image=image,
        price=price,
        quantity=quantity,
        borrowable=borrowable,
        buyable=buyable
    )

    books_data.append(new_book)
    dump_to_json(books_data , "Resources/data/books.json")

#done
def delete_book(book_id):
    book = next((book for book in books_data if book.get_Book_id() == book_id), None)
    books_data.remove(book)
    dump_to_json(books_data , "Resources/data/books.json")
#done
def show_all_orders():
    return orders_data

#done
def binary_search_all_books_by_price(price):
    low, high = 0, len(books_sorted_data) - 1
    result = []

    while low <= high:
        mid = (low + high) // 2

        if books_sorted_data[mid].get_Book_price() == price:
            # Collect all matches
            result.append(books_sorted_data[mid])

            # Search to the left of `mid` for more matches
            left = mid - 1
            while left >= 0 and books_sorted_data[left].get_Book_price() == price:
                result.append(books_sorted_data[left])
                left -= 1

            # Search to the right of `mid` for more matches
            right = mid + 1
            while right < len(books_sorted_data) and books_sorted_data[right].get_Book_price() == price:
                result.append(books_sorted_data[right])
                right += 1

            return result  # Return all matches

        elif float(books_sorted_data[mid].get_Book_price()) < float(price):
            low = mid + 1
        else:
            high = mid - 1

    return []  # No matches found


def recommend_books(client:Client):
    # Check if the client has a reading history
    if not client.reading_history:
        return books_data  # Return the full list of books if there is no reading history
    
    # Step 1: Extract book IDs from the client's reading history
    read_book_ids = [order.get_id() for order in client.reading_history]
    
  

    # Step 2: Extract the categories and authors of the books the client has interacted with
    read_authors = set()
    read_categories = set()

    for book in books_data:
        if book.get_Book_id() in read_book_ids:
            read_authors.add(book.author)
            read_categories.update(book.categories)
      
    # Step 3: Classify books into priority groups
    
    priority_1 = []  # Books with same author and matching categories
    priority_2 = []  # Books with matching categories but different authors
    priority_3 = []  # Books with same author but different categories
    priority_4 = []  # All other books
    
    for book in books_data:
        if book.get_Book_id() in read_book_ids:
            # Skip books the client has already read
            continue

        author_match = book.author in read_authors
        category_match = any(category in read_categories for category in book.categories)

        if author_match and category_match:
            priority_1.append(book)  # Same author and matching categories
        elif category_match:
            priority_2.append(book)  # Matching categories only
        elif author_match:
            priority_3.append(book)  # Matching author only
        else:
            priority_4.append(book)  # No match at all

    # Step 4: Combine all priority groups to create the final recommended list
    recommended_books = priority_1 + priority_2 + priority_3 + priority_4
    
    return recommended_books

#done 
def forget_id(id_num):
    for i in (clients_data + librarians_data):
        if i.get_id_num() == id_num:
            return i.get_id()
    else:
        return 'ID not found'

