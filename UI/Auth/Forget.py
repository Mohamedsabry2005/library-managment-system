import customtkinter as tk
from PIL import Image
from UI.Auth.AuthAbstractClass import Auth

class ForgetScreen(Auth):
  def __init__(self):
    super().__init__()
    self.show_forget_id_screen()

  def create_left_frame(self):
    return super().create_left_frame()
  def create_right_frame(self):
    return super().create_right_frame()
  def clear_right_frame(self):
    return super().clear_right_frame()
  def show_previous_screen(self):
    return super().show_previous_screen()

  def show_forget_id_screen(self):
    self.screen_stack.append('forget_id')
    self.clear_right_frame()
    self.previous_button = tk.CTkButton(master=self.right_frame, text="",image=self.PrevIcon,width=30,height=30, command=self.show_previous_screen)
    self.previous_button.pack(side="top", anchor="nw", pady=20, padx=20)
    self.heading_label=tk.CTkLabel(master=self.right_frame,text="Forget ID",font=('Arial',32),anchor='nw',width=500,height=100)
    self.heading_label.pack(pady=40,padx=30)
    self.Identification_number = tk.CTkEntry(master=self.right_frame, placeholder_text="Enter Identification Number",width=300,height=50,font=('Arial',18))
    self.Identification_number.pack(pady=10, padx=20)
    self.Submit_ID = tk.CTkButton(master=self.right_frame, text="Submit",width=180,height=40,font=("Arial",18))
    self.Submit_ID.pack(pady=40,padx=30)


