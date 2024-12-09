import customtkinter as tk
from PIL import Image
from abc import ABC, abstractmethod
class Auth(tk.CTk,ABC):
  def __init__(self):
    super().__init__()
    self.title('Library App')
    self.geometry('1000x600')
    self.resizable(False, False)
    self.screen_stack = ['main']
    self.PrevIcon=tk.CTkImage(Image.open("UI/Assets/Icons/prev.png"), size=(20, 20))
    self.create_left_frame()
    self.create_right_frame()

  @abstractmethod
  def create_left_frame(self):
    self.left_frame = tk.CTkFrame(master=self, width=500)
    self.left_frame.pack(side='left', fill='both')

    self.hero_image = tk.CTkImage(Image.open("UI/Assets/Images/heroImg.jpg"), size=(500, 600))
    self.image_label = tk.CTkLabel(master=self.left_frame, image=self.hero_image, text='')
    self.image_label.pack(pady=20, padx=20)

  @abstractmethod
  def create_right_frame(self):
    self.right_frame = tk.CTkFrame(master=self, width=500)
    self.right_frame.pack(side="right", fill='both', expand=True)

  @abstractmethod
  def clear_right_frame(self):
    for widget in self.right_frame.winfo_children():
      widget.destroy()

  @abstractmethod
  def button_click(self, button_text):
      if button_text == "Sign In":
          from UI.Auth.Login import LoginScreen
          LoginScreen.show_sign_in_screen(self)
      elif button_text == "Sign Up":
          from UI.Auth.Register import SignUpScreen
          SignUpScreen.show_sign_up_screen(self)
      else:
          from UI.Auth.Forget import ForgetScreen
          ForgetScreen.show_forget_id_screen(self)

  @abstractmethod
  def show_previous_screen(self):
    if len(self.screen_stack) > 1:
        self.screen_stack.pop()
        if self.screen_stack[-1] == "main":
            self.show_main_screen()
        elif self.screen_stack[-1] == "sign_in":
            self.show_sign_in_screen()
        elif self.screen_stack[-1] == "sign_up":
            self.show_sign_up_screen()
        elif self.screen_stack[-1] == "forget_id":
            self.show_forget_id_screen()

