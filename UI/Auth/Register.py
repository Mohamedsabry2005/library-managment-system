import customtkinter as tk
from PIL import Image
from UI.Auth.AuthAbstractClass import Auth
from Resources.data.Data import client_sign_up,librarian_sign_up
class SignUpScreen(Auth):
  def __init__(self):
    super().__init__()
    self.show_sign_up_screen()

  def create_left_frame(self):
    return super().create_left_frame()
  def create_right_frame(self):
    return super().create_right_frame()
  def clear_right_frame(self):
    return super().clear_right_frame()
  def show_previous_screen(self):
    return super().show_previous_screen()

  def show_sign_up_screen(self):
    def show_error_message(message):
      error_message = tk.CTkLabel(master=self.right_frame, text=message, font=('Arial', 14), text_color="red")
      error_message.pack(pady=10)
      self.after(3000, error_message.destroy) 
    def submit_sign_up():
      selected_tab=self.tabview.get()
      print(selected_tab)
      if selected_tab == "Client":
        client_name = self.client_name.get()
        client_age = self.client_age.get()
        client_phone_number = self.client_phone_number.get()
        client_identification_number = self.client_identification_number.get()
        client_address = self.client_address.get()

        if not client_name or not client_name.isalpha():
            show_error_message("Client Name cannot be empty.")
            return
        if not client_age.isdigit() or int(client_age) <= 0:
            show_error_message("Client Age must be a positive integer.")
            return
        if not client_phone_number or not client_phone_number.isdigit():
            show_error_message("Client Phone Number cannot be empty and only digits.")
            return
        if not client_identification_number or not client_identification_number.isdigit():
            show_error_message("Client Identification Number cannot be empty and only digits.")
            return
        if not client_address:
            show_error_message("Client Address cannot be empty.")
            return
        client=client_sign_up(client_phone_number,client_name,client_age,client_identification_number,client_address)
        message=tk.CTkLabel(master=self.right_frame, text=client.get_id(), font=('Arial', 14), text_color="white")
        message.pack(pady=10)
      else:
        librarian_name = self.librarian_name.get()
        librarian_age = self.librarian_age.get()
        librarian_identification_number = self.librarian_identification_number.get()
        librarian_address = self.librarian_address.get()
        librarian_phone_number = self.librarian_phone_number.get()
        librarian_employment_type = self.librarian_employment_type.get()

        if not librarian_name or not librarian_name.isalpha():
            show_error_message("Librarian Name must be characters.")
            return
        if not librarian_age.isdigit() or int(librarian_age) <= 0:
            show_error_message("Librarian Age must be a positive integer.")
            return
        if not librarian_phone_number or not librarian_phone_number.isdigit():
            show_error_message("Librarian Phone Number must be numbers.")
            return
        if not librarian_identification_number:
            show_error_message("Librarian Identification Number cannot be empty.")
            return
        if not librarian_address:
            show_error_message("Librarian Address cannot be empty.")
            return
        if not librarian_employment_type:
            show_error_message("Librarian Employment Type cannot be empty.")
            return
        Librarian=librarian_sign_up(librarian_name,librarian_age,librarian_identification_number,librarian_address,librarian_phone_number,librarian_employment_type)
        message=tk.CTkLabel(master=self.right_frame, text=Librarian.get_id(), font=('Arial', 14), text_color="white")
        message.pack(pady=10)

    self.screen_stack.append('sign_up')
    self.clear_right_frame()
    self.previous_button = tk.CTkButton(master=self.right_frame, text="",image=self.PrevIcon,width=30,height=30, command=self.show_previous_screen)
    self.previous_button.pack(side="top", anchor="nw", pady=20, padx=20)
    self.heading_label=tk.CTkLabel(master=self.right_frame,text="Sign Up",font=('Arial',32),anchor='nw',width=500,height=60)
    self.heading_label.pack(padx=30)

    self.scroll=tk.CTkScrollableFrame(self.right_frame)
    self.scroll.pack(expand=True,fill="both",padx=20,pady=20)
    self.tabview = tk.CTkTabview(master=self.scroll)
    self.tabview.pack(expand=True, fill="both")

    # Create individual tabs
    self.tabview.add("Client")
    self.tabview.add("Librarian")

    # Get the frames of the tabs
    tab1_frame = self.tabview.tab("Client")
    tab2_frame = self.tabview.tab("Librarian")

    #fields for client
    self.client_name = tk.CTkEntry(master=tab1_frame, placeholder_text="Enter Name", width=300, height=50, font=('Arial', 18))
    self.client_name.pack(pady=10, padx=20)
    self.client_age = tk.CTkEntry(master=tab1_frame, placeholder_text="Enter Age", width=300, height=50, font=('Arial', 18))
    self.client_age.pack(pady=10, padx=20)
    self.client_phone_number = tk.CTkEntry(master=tab1_frame, placeholder_text="Enter Phone Number", width=300, height=50, font=('Arial', 18))
    self.client_phone_number.pack(pady=10, padx=20)
    self.client_identification_number = tk.CTkEntry(master=tab1_frame, placeholder_text="Enter Identification Number", width=300, height=50, font=('Arial', 18))
    self.client_identification_number.pack(pady=10, padx=20)
    self.client_address = tk.CTkEntry(master=tab1_frame, placeholder_text="Enter Address", width=300, height=50, font=('Arial', 18))
    self.client_address.pack(pady=10, padx=20)

    #fields for librarian
    self.librarian_name = tk.CTkEntry(master=tab2_frame, placeholder_text="Enter Name", width=300, height=50, font=('Arial', 18))
    self.librarian_name.pack(pady=10, padx=20)
    self.librarian_age = tk.CTkEntry(master=tab2_frame, placeholder_text="Enter Age", width=300, height=50, font=('Arial', 18))
    self.librarian_age.pack(pady=10, padx=20)
    self.librarian_identification_number = tk.CTkEntry(master=tab2_frame, placeholder_text="Enter Identification Number", width=300, height=50, font=('Arial', 18))
    self.librarian_identification_number.pack(pady=10, padx=20)
    self.librarian_address = tk.CTkEntry(master=tab2_frame, placeholder_text="Enter Address", width=300, height=50, font=('Arial', 18))
    self.librarian_address.pack(pady=10, padx=20)
    self.librarian_phone_number = tk.CTkEntry(master=tab2_frame, placeholder_text="Enter Phone Number", width=300, height=50, font=('Arial', 18))
    self.librarian_phone_number.pack(pady=10, padx=20)
    self.librarian_employment_type = tk.CTkEntry(master=tab2_frame, placeholder_text="Enter Employment Type", width=300, height=50, font=('Arial', 18))
    self.librarian_employment_type.pack(pady=10, padx=20)

    
    self.Submit = tk.CTkButton(master=self.right_frame, text="Submit",width=180,height=40,font=("Arial",18),command=submit_sign_up)
    self.Submit.pack(pady=40,padx=30)
