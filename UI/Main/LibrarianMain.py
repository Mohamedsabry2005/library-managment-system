import customtkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from UI.Main.MainAbstractClass import MainApp
from Resources.data.Data import read_books,show_all_orders,delete_book,add_book
book_info=read_books()
orders=show_all_orders()
book_states={}

class BookCard(tk.CTkFrame):
    def __init__(self, parent, book_info,app, width=200, height=250, corner_radius=10, fg_color="#fff"):
        super().__init__(parent, width=width, height=height, corner_radius=corner_radius, fg_color=fg_color)
        self.app=app
        self.book_info=book_info
        # Image
        self.image = Image.open(book_info.image) 
        self.image = self.image.resize((width, 150))
        self.image = ImageTk.PhotoImage(self.image)
        self.book_image_label = tk.CTkLabel(self, image=self.image, text="")
        self.book_image_label.pack(side="top", fill="both", expand=True, pady=5, padx=5)

        # Book details
        self.book_details = tk.CTkFrame(self, width=width, height=150, corner_radius=corner_radius, fg_color=fg_color)
        self.book_details.pack(side="bottom", fill="x", pady=10, padx=5)

        self.title = tk.CTkLabel(self.book_details, text=book_info.title, font=("Arial", 18), text_color="#000",width=int(width/13),wraplength=int(width*0.8))
        self.title.pack(side='top', anchor='w', padx=10)

        self.author = tk.CTkLabel(self.book_details, text=f"Author: {book_info.author}", font=("Arial", 14), text_color="#000",width=int(width/13))
        self.author.pack(side='top', anchor='w', padx=10)

        self.category = tk.CTkLabel(self.book_details, text=f"Category: {", ".join(book_info.categories)}", font=("Arial", 14), text_color="#000",width=int(width / 13), wraplength=int(width * 0.8))
        self.category.pack(side='top', anchor='w', padx=10, pady=5)

        self.delete_button = tk.CTkButton(self.book_details, text="Delete Book", command=lambda: self.delete_book(book_info.get_Book_id()))
        self.delete_button.pack(pady=10, padx=20)


        self.borrowable_toggle = tk.CTkSwitch(self.book_details,font=('Arial',15), text="Borrowable",fg_color="black" ,text_color="black",command=lambda: self.change_state("borrow",book_info.get_Book_id()))
        self.borrowable_toggle.select() if book_info.get_Book_borrowable() else self.borrowable_toggle.deselect()
        self.borrowable_toggle.pack(side="left",pady=10, padx=20)
        self.purchasable_toggle = tk.CTkSwitch(self.book_details, text="Purchasable",fg_color="black",text_color="black",command=lambda: self.change_state("buy",book_info.get_Book_id()))
        self.purchasable_toggle.select() if book_info.get_Book_buyable() else self.purchasable_toggle.deselect()
        self.purchasable_toggle.pack(side='left',pady=10, padx=20)
    def delete_book(self,book_id):
      delete_book(book_id)
      book_info=read_books()
      self.app.list_books(book_info)
    def change_state(self, state, name):
        for book in book_info:
            if book.get_Book_id() == name:
                if state == 'buy':
                    book.set_Book_buyable(not book.get_Book_buyable()) 
                elif state == "borrow":
                    book.set_Book_borrowable(not book.get_Book_borrowable())
                book_states[name]={
                  'borrowed':book.get_Book_borrowable(),
                  'Bought':book.get_Book_buyable()
                }
        print(book_states)


class LibrarianMain(MainApp):
  def __init__(self,Librarian):
    super().__init__()
    self._set_appearance_mode("dark")
    self.Librarian=Librarian
    self.books_per_row=3
    self.book_info=read_books()
    self.orders=show_all_orders()
    self.create_header()
    self.create_content()

  def create_header(self):
    self.header_frame=tk.CTkFrame(self,corner_radius=10)
    self.header_frame.pack(fill="x",pady=20,padx=20)

    self.add=tk.CTkButton(self.header_frame,width=100,text="Add books",command=self.add_book)


    self.greeting_label=tk.CTkLabel(self.header_frame,text=f"Hello {self.Librarian.name}",font=('Arial',16))
    self.greeting_label.pack(side="left",padx=10)
    self.search_frame=tk.CTkFrame(self.header_frame)
    self.search_frame.pack(side="left",expand=True)
    self.search_entry=tk.CTkEntry(self.search_frame,placeholder_text='enter ID',width=300,border_color="#000",text_color='#fff',border_width=3)
    self.search_entry.pack(side="left",padx=10,pady=10)
    self.iconImg=tk.CTkImage(Image.open("UI/Assets/Icons/searchIcon.png"),size=(20,20))
    self.search_button=tk.CTkButton(self.search_frame,width=30,height=30,image=self.iconImg,text='',fg_color="#fff",hover_color="#fff",command=lambda:self.search_orders(self.search_entry.get()))
    self.search_button.pack(side="right",padx=10)

    self.main_button=tk.CTkButton(self.header_frame,width=100,text="Books",command=lambda: self.list_books(self.book_info))
    self.main_button.pack(side='right',padx=10)

  def search_books(self,search_term):
    filtered_books=[]
    if search_term=="":
      for widget in self.book_cards_frame.winfo_children():
        widget.destroy()
      self.list_books(book_info)
    else:
      for book in self.book_info:
          if search_term.lower() in book.title.lower():
            filtered_books.append(book)
      self.book_info=filtered_books
      self.list_books(filtered_books)

  def search_orders(self,search_term):
    filtered_orders=[]
    if search_term=="":
      self.treeview.destroy()
      self.list_of_orders(orders)
    else:
      for order in self.orders:
          if search_term.lower() == str(order.get_id()):
            filtered_orders.append(order)
      self.book_info=filtered_orders
      self.treeview.destroy()
      self.list_of_orders(filtered_orders)

  def create_content(self):
    self.scroll_frame = tk.CTkScrollableFrame(self)
    self.scroll_frame.pack(fill='both', expand=True)
    self.list_of_orders(self.orders)

  def list_of_orders(self,orders):
    self.main_button.configure(text="Books",command=lambda: self.list_books(self.book_info))
    self.search_entry.configure(placeholder_text='enter ID')
    self.search_button.configure(command=lambda: self.search_orders(self.search_entry.get()))
    for widget in self.scroll_frame.winfo_children():
      widget.destroy()
    self.style=ttk.Style()
    self.style.configure(
      "Treeview",
      background="#222222",
      foreground="white",
      rowheight=30,
      font=('Helvetica',12)
    )
    self.style.configure(
      "Treeview.Heading",
      font=('Helvetica',14,"bold"),
    )
    self.style.map('Treeview',background=[('selected','#333333')])
    self.treeview=ttk.Treeview(self.scroll_frame,columns=("Order ID", "Date", "Client ID", "Book ID", "Status", "Order type", "Price"),show="headings",style="Treeview")

    self.treeview.column("#1", width=50)  

    self.treeview.heading("#1", text="ID")
    self.treeview.heading("#2", text="Date")
    self.treeview.heading("#3", text="Client ID")
    self.treeview.heading("#4", text="Book ID")
    self.treeview.heading("#5", text="Status")
    self.treeview.heading("#6", text="Order type")
    self.treeview.heading("#7", text="Price")
    self.treeview.pack(fill="y",expand=True)
    for order in orders:
      self.treeview.insert('','end',values=(order.get_id(), order.get_date(), order.get_client_id(), order.get_book_id(), order.get_status(), order.get_order_type(),order.get_price()))

  def add_book(self):
    self.popup=tk.CTkToplevel(self)
    self.popup.geometry('300x500')
    self.popup.transient(self)
    self.popup.grab_set()
    self.popup.title('Add Book')

    self.book_title_entry = tk.CTkEntry(self.popup, placeholder_text="Book Title")
    self.book_description_entry = tk.CTkEntry(self.popup, placeholder_text="Book description")
    self.book_author_entry = tk.CTkEntry(self.popup, placeholder_text="Author")
    self.book_cat_entry = tk.CTkEntry(self.popup, placeholder_text="Category")
    self.book_ISBN_entry = tk.CTkEntry(self.popup, placeholder_text="Book Title")
    self.book_img_entry = tk.CTkEntry(self.popup, placeholder_text="Image Path (optional)")
    self.book_price_entry = tk.CTkEntry(self.popup, placeholder_text="Book Title")
    self.book_quantity_entry = tk.CTkEntry(self.popup, placeholder_text="Book Title")

    add_button = tk.CTkButton(self.popup, text="Add Book", command=self.add_book_to_list)

    self.book_title_entry.pack(pady=10, padx=20)
    self.book_description_entry.pack(pady=10, padx=20)
    self.book_author_entry.pack(pady=10, padx=20)
    self.book_cat_entry.pack(pady=10, padx=20)
    self.book_ISBN_entry.pack(pady=10, padx=20)
    self.book_img_entry.pack(pady=10, padx=20)
    self.book_price_entry.pack(pady=10, padx=20)
    self.book_quantity_entry.pack(pady=10, padx=20)
    add_button.pack(pady=10, padx=20)

  def add_book_to_list(self):
    def show_error_message(message):
      error_message = tk.CTkLabel(master=self.right_frame, text=message, font=('Arial', 14), text_color="red")
      error_message.pack(pady=10)
      self.after(3000, error_message.destroy) 


    book_title = self.book_title_entry.get()
    book_description = self.book_description_entry.get()
    book_author = self.book_author_entry.get()
    book_cat = self.book_cat_entry.get()
    book_ISBN = self.book_ISBN_entry.get()
    book_img_path = self.book_img_entry.get()
    book_price = self.book_price_entry.get()
    book_quantity = self.book_quantity_entry.get()
    if not self.book_title_entry.get():
      show_error_message("Book Title cannot be empty.")
    if not self.book_description_entry.get():
      show_error_message("Book Description cannot be empty.")
    if not self.book_author_entry.get() or not book_author.isalpha():
      show_error_message("Book Author cannot be empty.")
    if not self.book_cat_entry.get():
      show_error_message("Book Category cannot be empty.")
    if not self.book_ISBN_entry.get():
      show_error_message("ISBN cannot be empty.")
    if not self.book_img_path_entry.get():
      show_error_message("Image Path cannot be empty.")
    if not self.book_price_entry.get():
      show_error_message("Price cannot be empty.")
    if not self.book_quantity_entry.get():
      show_error_message("Quantity cannot be empty.")


    if book_img_path=="":
      add_book(book_title,book_description,book_author,"available",book_cat,book_ISBN,'UI/Assets/Images/books/unavailable.png',book_price,book_quantity,True,True)
    add_book(book_title,book_description,book_author,"available",book_cat,book_ISBN,book_img_path,book_price,book_quantity,True,True)
    self.popup.destroy()

  def list_books(self, book_info):
    for widget in self.scroll_frame.winfo_children():
      widget.destroy()
    self.main_button.configure(text="Orders",command=lambda: self.list_of_orders(self.orders))
    self.search_entry.configure(placeholder_text='enter book name')
    self.search_button.configure(command=lambda: self.search_books(self.search_entry.get()))
    if self.add.winfo_exists():
      self.add.destroy()
    self.add=tk.CTkButton(self.header_frame,width=100,text="Add books",command=self.add_book)
    self.add.pack(side="left",padx=10)


    self.book_cards_frame=tk.CTkFrame(self.scroll_frame)
    self.book_cards_frame.pack(fill="both",expand=True,padx=30,pady=30)

    row_counter=0
    current_row = tk.CTkFrame(self.book_cards_frame)
    current_row.pack(side="top", fill="x", padx=0, pady=10)


    for book in book_info:
      self.book_card=BookCard(current_row,book,self)
      self.book_card.pack(side="left",padx=10,pady=10)
      row_counter+=1

      if row_counter % self.books_per_row == 0 and row_counter < len(book_info):
        current_row = tk.CTkFrame(self.book_cards_frame)
        current_row.pack(side="top", fill="x", padx=0, pady=10)
