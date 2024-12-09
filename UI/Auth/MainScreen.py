import customtkinter as tk
from PIL import Image
from UI.Auth.AuthAbstractClass import Auth

class MainScreen(Auth):
  def __init__(self):
    super().__init__()
    self.show_main_screen()

  def create_left_frame(self):
    return super().create_left_frame()
  def create_right_frame(self):
    return super().create_right_frame()
  def clear_right_frame(self):
    return super().clear_right_frame()
  def button_click(self, button_text):
    return super().button_click(button_text)
  def show_previous_screen(self):
    return super().show_previous_screen()


  def show_main_screen(self):
    self.clear_right_frame()

    self.heading_label = tk.CTkLabel(master=self.right_frame,text="Welcome to My Library",font=('Arial', 32), anchor='nw',width=500, height=100)
    self.heading_label.pack(pady=40, padx=20)

    self.sign_in_button = tk.CTkButton(master=self.right_frame, text="Sign In",width=180, height=40, font=("Arial", 18),command=lambda: self.button_click("Sign In"))
    self.sign_in_button.pack(pady=10, padx=20)

    self.sign_up_button = tk.CTkButton(master=self.right_frame, text="Sign Up",width=180, height=40, font=("Arial", 18),command=lambda: self.button_click("Sign Up"))
    self.sign_up_button.pack(pady=10, padx=20)

    self.forget_id_button = tk.CTkButton(master=self.right_frame, text="Forget ID",width=180, height=40, font=("Arial", 18),command=lambda: self.button_click("Forget ID"))
    self.forget_id_button.pack(pady=10, padx=20)
