import customtkinter as tk
from PIL import Image, ImageTk
from MainAbstractClass import MainApp
from data import book_info

class BookCard(tk.CTkFrame):
    def __init__(self, parent, book_info, width=200, height=250, corner_radius=10, fg_color="#fff"):
        super().__init__(parent, width=width, height=height, corner_radius=corner_radius, fg_color=fg_color)

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

        self.borrow_button = tk.CTkButton(self.book_details, text="Borrow Now", width=80, height=20)
        self.borrow_button.pack(side="left", expand=True, anchor='w', padx=10)

        self.buy_button = tk.CTkButton(self.book_details, text="Buy Now", width=80, height=20)
        self.buy_button.pack(side="right", expand=True, padx=10)



class ClientMain(MainApp):
  def __init__(self):
    super().__init__()
    self.books_per_row=4
    self.book_info=book_info
    self.create_header()
    self.create_content()

  def create_header(self):
    self.header_frame=tk.CTkFrame(self,corner_radius=10)
    self.header_frame.pack(fill="x",pady=20,padx=20)

    self.greeting_label=tk.CTkLabel(self.header_frame,text="Hello Mr User",font=('Arial',16))
    self.greeting_label.pack(side="left",padx=10)
    self.search_frame=tk.CTkFrame(self.header_frame)
    self.search_frame.pack(side="left",expand=True)
    self.search_entry=tk.CTkEntry(self.search_frame,placeholder_text='Enter book name',width=300,border_color="#000",text_color='#fff',border_width=3)
    self.search_entry.pack(side="left",padx=10,pady=10)
    self.iconImg=tk.CTkImage(Image.open("UI/Assets/Icons/searchIcon.png"),size=(20,20))
    self.search_button=tk.CTkButton(self.search_frame,width=30,height=30,image=self.iconImg,text='',fg_color="#fff",hover_color="#fff",command=lambda:self.handle_search(self.search_entry.get()))
    self.search_button.pack(side="right",padx=10)

    self.main_button=tk.CTkButton(self.header_frame,width=100,text="Orders",command=self.show_orders)
    self.main_button.pack(side='right',padx=10)

  def show_orders(self):
    for widget in self.book_cards_frame.winfo_children():
      widget.destroy()
    self.order_label=tk.CTkLabel(self.book_cards_frame,text="Order History",font=("Arial",32),text_color='#fff')
    self.order_label.pack(side="top",fill='x',padx=10,pady=10,anchor="w")
    self.main_button.configure(text="Main",command=lambda: self.list_books(self.book_info))

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
      self.book_info=book_info
      self.list_books(self.book_info)
    else:
      for book in book_info:
          if search_term.lower() in book['title'].lower():
            filtered_books.append(book)
      self.book_info=filtered_books
      for widget in self.book_cards_frame.winfo_children():
        widget.destroy()
      self.list_books(filtered_books)

  def list_books(self, book_info):
    for widget in self.book_cards_frame.winfo_children():
      widget.destroy()
    row_counter=0
    current_row = tk.CTkFrame(self.book_cards_frame)
    current_row.pack(side="top", fill="x", padx=0, pady=10)


    self.main_button.configure(text="Orders",command=self.show_orders)
    for book in book_info:
      self.book_card=BookCard(current_row,book)
      self.book_card.pack(side="left",padx=10,pady=10)
      row_counter+=1

      if row_counter % self.books_per_row == 0 and row_counter < len(book_info):
        current_row = tk.CTkFrame(self.book_cards_frame)
        current_row.pack(side="top", fill="x", padx=0, pady=10)

hi=ClientMain()
hi.mainloop()