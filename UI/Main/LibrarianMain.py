import customtkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from MainAbstractClass import MainApp
from data import book_info,orders
book_states={}

class BookCard(tk.CTkFrame):
    def __init__(self, parent, book_info,app, width=200, height=250, corner_radius=10, fg_color="#fff"):
        super().__init__(parent, width=width, height=height, corner_radius=corner_radius, fg_color=fg_color)
        self.app=app
        # Image
        self.image = Image.open(book_info['image_path']) 
        self.image = self.image.resize((width, 150))
        self.image = ImageTk.PhotoImage(self.image)
        self.book_image_label = tk.CTkLabel(self, image=self.image, text="")
        self.book_image_label.pack(side="top", fill="both", expand=True, pady=5, padx=5)

        # Book details
        self.book_details = tk.CTkFrame(self, width=width, height=150, corner_radius=corner_radius, fg_color=fg_color)
        self.book_details.pack(side="bottom", fill="x", pady=10, padx=5)

        self.title = tk.CTkLabel(self.book_details, text=book_info['title'], font=("Arial", 24), text_color="#000")
        self.title.pack(side='top', anchor='w', padx=10)

        self.author = tk.CTkLabel(self.book_details, text=f"Author: {book_info['author']}", font=("Arial", 14), text_color="#000")
        self.author.pack(side='top', anchor='w', padx=10)

        self.category = tk.CTkLabel(self.book_details, text=f"Category: {book_info['category']}", font=("Arial", 14), text_color="#000")
        self.category.pack(side='top', anchor='w', padx=10, pady=5)

        self.delete_button = tk.CTkButton(self.book_details, text="Delete Book", command=lambda: self.delete_book(book_info['title']))
        self.delete_button.pack(pady=10, padx=20)


        self.borrowable_toggle = tk.CTkSwitch(self.book_details,font=('Arial',15), text="Borrowable",fg_color="black" ,text_color="black",command=lambda: self.change_state("borrow",book_info["title"]))
        self.borrowable_toggle.select() if book_info['borrowed'] else self.borrowable_toggle.deselect()
        self.borrowable_toggle.pack(side="left",pady=10, padx=20)
        self.purchasable_toggle = tk.CTkSwitch(self.book_details, text="Purchasable",fg_color="black",text_color="black",command=lambda: self.change_state("buy",book_info["title"]))
        self.purchasable_toggle.select() if book_info['Bought'] else self.purchasable_toggle.deselect()
        self.purchasable_toggle.pack(side='left',pady=10, padx=20)
    def delete_book(self,book_title):
      for book in book_info:
        if book["title"]==book_title:
          book_info.remove(book)
          break
      self.app.list_books(book_info)
    def change_state(self, state, name):
        for book in book_info:
            if book['title'] == name:
                if state == 'buy':
                    book["Bought"] = not book["Bought"]
                elif state == "borrow":
                    book['borrowed'] = not book['borrowed']
                break
        book_states[name]={
          'borrowed':book['borrowed'],
          'Bought':book["Bought"]
        }
        print(book_states)


class LibrarianMain(MainApp):
  def __init__(self):
    super().__init__()
    self.books_per_row=3
    self.book_info=book_info
    self.orders=orders
    self.create_header()
    self.create_content()

  def create_header(self):
    self.header_frame=tk.CTkFrame(self,corner_radius=10)
    self.header_frame.pack(fill="x",pady=20,padx=20)

    self.add=tk.CTkButton(self.header_frame,width=100,text="Add books",command=self.add_book)


    self.greeting_label=tk.CTkLabel(self.header_frame,text="Hello Librarian",font=('Arial',16))
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
      self.book_info=book_info
      self.list_books(self.book_info)
    else:
      for book in self.book_info:
          if search_term.lower() in book['title'].lower():
            filtered_books.append(book)
      self.book_info=filtered_books
      self.list_books(filtered_books)

  def search_orders(self,search_term):
    filtered_orders=[]
    if search_term=="":
      self.treeview.destroy()
      self.orders=orders
      self.list_of_orders(self.orders)
    else:
      for order in orders:
          if search_term.lower() == str(order["order_id"]):
            filtered_orders.append(order)
      self.book_info=filtered_orders
      self.treeview.destroy()
      self.list_of_orders(filtered_orders)

  def create_content(self):
    self.scroll_frame = tk.CTkScrollableFrame(self)
    self.scroll_frame.pack(fill='both', expand=True)
    self.list_of_orders(orders)

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
    self.treeview=ttk.Treeview(self.scroll_frame,columns=("Order ID", "Customer Name", "Book Title", "Order Date", "Due Date", "Status"),show="headings",style="Treeview")

    self.treeview.column("#1", width=50)  

    self.treeview.heading("#1", text="ID")
    self.treeview.heading("#2", text="Customer Name")
    self.treeview.heading("#3", text="Book Title")
    self.treeview.heading("#4", text="Order Date")
    self.treeview.heading("#5", text="Due Date")
    self.treeview.heading("#6", text="Status")
    self.treeview.pack(fill="y",expand=True)
    for order in orders:
      self.treeview.insert('','end',values=(order["order_id"], order["customer_name"], order["book_title"], order["order_date"], order["due_date"], order["status"]))

  def add_book(self):
    self.popup=tk.CTkToplevel(self)
    self.popup.geometry('300x300')
    self.popup.transient(self)
    self.popup.grab_set()
    self.popup.title('Add Book')

    self.book_title_entry = tk.CTkEntry(self.popup, placeholder_text="Book Title")
    self.book_author_entry = tk.CTkEntry(self.popup, placeholder_text="Author")
    self.book_cat_entry = tk.CTkEntry(self.popup, placeholder_text="Category")
    self.book_img_entry = tk.CTkEntry(self.popup, placeholder_text="Image Path (optional)")

    add_button = tk.CTkButton(self.popup, text="Add Book", command=lambda: self.add_book_to_list(self.book_title_entry.get(), self.book_author_entry.get(), self.book_cat_entry.get(),self.book_img_entry.get()))

    self.book_title_entry.pack(pady=10, padx=20)
    self.book_author_entry.pack(pady=10, padx=20)
    self.book_cat_entry.pack(pady=10, padx=20)
    self.book_img_entry.pack(pady=10, padx=20)
    add_button.pack(pady=10, padx=20)

  def add_book_to_list(self,title, author, cat,img):
      if img=="":
        self.book_info.append({"title": title, "author": author, "category": cat,"image_path":'UI/Assets/Images/books/unavailable.png',"borrowed": True, "Bought": True})
      self.book_info.append({"title": title, "author": author, "category": cat,"image_path":img,"borrowed": True, "Bought": True})
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

hi=LibrarianMain()
hi.mainloop()