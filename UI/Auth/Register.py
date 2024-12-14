import customtkinter as tk
from PIL import Image
from UI.Auth.AuthAbstractClass import Auth

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


    self.Submit = tk.CTkButton(master=self.right_frame, text="Submit",width=180,height=40,font=("Arial",18))
    self.Submit.pack(pady=40,padx=30)