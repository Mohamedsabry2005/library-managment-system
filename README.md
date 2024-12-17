**Library App**

This is a simple Python application that creates a library management app. It uses the following libraries:

* **customtkinter:** A custom Tkinter theme for a more modern look and feel.
* **Pillow (PIL Fork):** Used for loading and displaying images.
* **json:** Used for working with JSON data (potentially for storing library data)
* **sys:** Provides access to system specific parameters and functions.
* **datetime:** Used for working with dates and times (potentially for tracking borrowing and returning of items).
* **uuid:** Used for generating unique identifiers (potentially for record identification).
* **os:** Used for interacting with the operating system (potentially for file operations).

**Installation**

1. Make sure you have Python 3 installed on your system. You can check by running `python3 --version` in your terminal. If you don't have it, download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Open a terminal window and navigate to the directory containing this project.
3. Install the required libraries by running the following command:

```
pip install -r requirements.txt
```

# UML Diagram

## Book

### Attributes:
- **id**: int
- **title**: string
- **description**: string
- **author**: string
- **status**: string
- **categories**: list
- **ISBN**: string
- **image**: string
- **price**: float
- **quantity**: int
- **borrowable**: bool
- **buyable**: bool

### Methods:
- `+ get_Book_id(): int`
- `+ set_Book_id(id: int): void`
- `+ to_dict(): dict`

---

## Client

### Attributes:
- **phone_num**: string
- **id**: int
- **name**: string
- **age**: int
- **id_num**: string
- **address**: string
- **reading_history**: list[Order]
- **orders_num**: int

### Methods:
- `+ get_reading_history(): list`
- `+ set_reading_history(list): void`
- `+ get_orders_num(): int`
- `+ set_orders_num(num: int): void`
- `+ to_dict(): dict`

---

## Order

### Attributes:
- **id**: int
- **date**: string
- **client_id**: int
- **book_id**: int
- **status**: string
- **order_type**: string
- **price**: float

### Methods:
- `+ get_id(): int`
- `+ set_id(id: int): void`
- `+ to_dict(): dict`
- `+ from_dict(data: dict): Order`
