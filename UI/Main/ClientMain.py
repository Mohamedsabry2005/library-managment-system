import customtkinter as tk
from PIL import Image, ImageTk
from UI.Main.MainAbstractClass import MainApp
from Resources.data.Data import read_books,borrow_book,buy_book,binary_search_all_books_by_price,sorted_books,sorted_books_desc,recommend_books
book_info=read_books()
class BookCard(tk.CTkFrame):
    def __init__(self, parent, book_info,app, width=250, height=250, corner_radius=10, fg_color="#fff"):
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

        self.price = tk.CTkLabel(self.book_details, text=f"{book_info.get_Book_price()} $", font=("Arial", 14), text_color="#000",width=int(width / 13), wraplength=int(width * 0.8))
        self.price.pack(side='top', anchor='w', padx=10, pady=5)

        self.borrow_button = tk.CTkButton(self.book_details, text="Borrow Now",width=int(width / 2) - 10, height=20,command=self.borrow)
        self.borrow_button.pack(side="left", expand=True, anchor='w', padx=10)

        self.buy_button = tk.CTkButton(self.book_details, text="Buy Now",width=int(width / 2) - 10, height=20,command=self.buy)
        self.buy_button.pack(side="right", expand=True, padx=10)

        self.borrow_button.configure(state="disabled" if book_info.borrowable else "normal")
        self.buy_button.configure(state="disabled" if book_info.buyable else "normal")
        for order in self.app.client.reading_history:
          if order.get_book_id()==book_info.get_Book_id():
            if order.get_order_type()=="borrow":
              self.borrow_button.configure(state="disabled")
            else:
              self.buy_button.configure(state="disabled")

    def borrow(self):
      toaster= Toaster(self, "Book borrowed successfully!")
      toaster.show()
      borrow_book(self.app.client,self.book_info.get_Book_id())
      self.borrow_button.configure(state="disabled")
    def buy(self):
      toaster= Toaster(self, "Book bought successfully!")
      toaster.show()
      buy_book(self.app.client,self.book_info.get_Book_id())
      self.buy_button.configure(state="disabled")


class ClientMain(MainApp):
  def __init__(self,client):
    super().__init__()
    self.client=client
    self.books_per_row=4
    self.book_info=recommend_books(self.client)
    self.create_header()
    self.create_content()

  def create_header(self):
    self.header_frame=tk.CTkFrame(self,corner_radius=10)
    self.header_frame.pack(fill="x",pady=20,padx=20)

    self.greeting_label=tk.CTkLabel(self.header_frame,text=f"Hello Mr {self.client.name}",font=('Arial',16))
    self.greeting_label.pack(side="left",padx=10)
    self.search_frame=tk.CTkFrame(self.header_frame)
    self.search_frame.pack(side="left",expand=True)
    self.search_entry=tk.CTkEntry(self.search_frame,placeholder_text='Enter book name',width=300,border_color="#000",text_color='#fff',border_width=3)
    self.search_entry.pack(side="left",padx=10,pady=10)
    self.iconImg=tk.CTkImage(Image.open("UI/Assets/Icons/searchIcon.png"),size=(20,20))
    self.search_button=tk.CTkButton(self.search_frame,width=30,height=30,image=self.iconImg,text='',fg_color="#fff",hover_color="#fff",command=lambda:self.handle_search(self.search_entry.get()))
    self.search_button.pack(side="right",padx=10)
    self.priceImg=tk.CTkImage(Image.open("UI/Assets/Icons/dollar.png"),size=(20,20))
    self.price_button=tk.CTkButton(self.search_frame,width=30,height=30,image=self.priceImg,text='',fg_color="#fff",hover_color="#fff",command=lambda:self.handle_search_price(self.search_entry.get()))
    self.price_button.pack(side="right",padx=10)

    self.main_button=tk.CTkButton(self.header_frame,width=100,text="Orders",command=self.show_orders)
    self.main_button.pack(side='right',padx=10)

    self.priceupImg=tk.CTkImage(Image.open("UI\Assets\Icons\sortup.png"),size=(20,20))
    self.price_button=tk.CTkButton(self.search_frame,width=30,height=30,image=self.priceupImg,text='',fg_color="#fff",hover_color="#fff",command=lambda:self.handle_sort("high"))
    self.price_button.pack(side="right",padx=10)

    self.priceDownImg=tk.CTkImage(Image.open("UI/Assets/Icons/sortdown.png"),size=(20,20))
    self.price_button=tk.CTkButton(self.search_frame,width=30,height=30,image=self.priceDownImg,text='',fg_color="#fff",hover_color="#fff",command=lambda:self.handle_sort("low"))
    self.price_button.pack(side="right",padx=10)

  def handle_sort(self,option):
    if option=="high":
      books=sorted_books()
      self.list_books(books)
    else:
      books=sorted_books_desc()
      self.list_books(books)

  def show_orders(self):
    for widget in self.book_cards_frame.winfo_children():
      widget.destroy()
    self.order_label=tk.CTkLabel(self.book_cards_frame,text="Order History",font=("Arial",32),text_color='#fff')
    self.order_label.pack(side="top",fill='x',padx=10,pady=10,anchor="w")
    self.main_button.configure(text="Main",command=lambda: self.list_books(self.book_info))
    for order in self.client.reading_history:  
      order_frame = tk.CTkFrame(self.book_cards_frame, corner_radius=8)
      order_frame.pack(side="top", fill="x", padx=10, pady=5)

      order_id_label = tk.CTkLabel(order_frame, text=f"Order ID: {order.get_id()}", font=("Arial", 12))
      order_id_label.pack(side="left", padx=5)

      date_label = tk.CTkLabel(order_frame, text=f"Date: {order.get_date()}", font=("Arial", 12))
      date_label.pack(side="left", padx=5)

      status_label = tk.CTkLabel(order_frame, text=f"Status: {order.get_status()}", font=("Arial", 12))
      status_label.pack(side="left", padx=5)

      order_type_label = tk.CTkLabel(order_frame, text=f"Type: {order.get_order_type()}", font=("Arial", 12))
      order_type_label.pack(side="left", padx=5)

      if order.get_price(): 
        price_label = tk.CTkLabel(order_frame, text=f"Price: ${order.get_price():.2f}", font=("Arial", 12))
        price_label.pack(side="right", padx=5)

  def create_content(self):
    self.scroll_frame = tk.CTkScrollableFrame(self)
    self.scroll_frame.pack(fill='both', expand=True)
    self.book_cards_frame = tk.CTkFrame(self.scroll_frame)
    self.book_cards_frame.pack(fill="both", expand=True, padx=30, pady=30)
    self.list_books(self.book_info)

  def handle_search(self, search_term):
    filtered_books=[]
    if search_term=="":
      for widget in self.book_cards_frame.winfo_children():
        widget.destroy()
      self.list_books(book_info)
    else:
      for book in self.book_info:
          if search_term.lower() in book.title.lower() :
            filtered_books.append(book)
          else:
            toaster= Toaster(self, "There is not a book with this price.")
            toaster.show()
      self.book_info=filtered_books
      self.list_books(filtered_books)

  def handle_search_price(self,search_term):
    if search_term=="":
      for widget in self.book_cards_frame.winfo_children():
        widget.destroy()
      self.list_books(book_info)
    else:
        try:
          price=float(search_term)
          books=binary_search_all_books_by_price(price)
          if books:
            self.list_books(books)
          else:
            toaster= Toaster(self, "There is not a book with this price.")
            toaster.show()
        except ValueError:
          pass


  def list_books(self, book_info):
    for widget in self.book_cards_frame.winfo_children():
      widget.destroy()
    row_counter=0
    current_row = tk.CTkFrame(self.book_cards_frame)
    current_row.pack(side="top", fill="x", padx=0, pady=10)


    self.main_button.configure(text="Orders",command=self.show_orders)
    for book in book_info:
      self.book_card=BookCard(current_row,book,self)
      self.book_card.pack(side="left",padx=10,pady=10)
      row_counter+=1

      if row_counter % self.books_per_row == 0 and row_counter < len(book_info):
        current_row = tk.CTkFrame(self.book_cards_frame)
        current_row.pack(side="top", fill="x", padx=0, pady=10)




class Toaster:
    def __init__(self, master, msg, duration=3000):
        self.master = master
        self.msg = msg
        self.duration = duration
        self.toaster_frame = None

    def show(self):
        self.toaster_frame = tk.CTkFrame(master=self.master, width=300, height=50, corner_radius=10, fg_color="gray20")
        self.toaster_frame.place(relx=0.5, rely=0.9, anchor="center")

        self.message_label = tk.CTkLabel(master=self.toaster_frame, text=self.msg, text_color="white", font=("Arial", 12))
        self.message_label.pack(padx=20, pady=10)

        self.master.after(self.duration, self.hide)

    def hide(self):
        self.toaster_frame.destroy()