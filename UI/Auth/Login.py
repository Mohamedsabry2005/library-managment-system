import customtkinter as tk
from PIL import Image
from UI.Auth.AuthAbstractClass import Auth
from Resources.data.Data import user_sign_in
from UI.Main.ClientMain import *
from UI.Main.LibrarianMain import *
class LoginScreen(Auth):
  def __init__(self):
    super().__init__()
    self.show_sign_in_screen()

  def create_left_frame(self):
    return super().create_left_frame()
  def create_right_frame(self):
    return super().create_right_frame()
  def clear_right_frame(self):
    return super().clear_right_frame()
  def show_previous_screen(self):
    return super().show_previous_screen()

  def show_sign_in_screen(self):
    def submit_id():
        ID= self.ID.get()
        if not ID or not ID.isdigit():
          error_message = tk.CTkLabel(master=self.right_frame, text="ID must be Numbers", font=('Arial', 14), text_color="red")
          error_message.pack(pady=10)
          self.after(3000,error_message.destroy)
        else:
          human=user_sign_in(ID)
          id=human.get_id()
          if id.startswith("1")==1:
            self.destroy()
            x=ClientMain(human)
            x.mainloop()
          else:
            self.destroy()
            x=LibrarianMain(human)
            x.mainloop()


    self.screen_stack.append('sign_in')
    self.clear_right_frame()
    self.previous_button = tk.CTkButton(master=self.right_frame, text="",image=self.PrevIcon,width=30,height=30, command=self.show_previous_screen)
    self.previous_button.pack(side="top", anchor="nw", pady=20, padx=20)
    self.heading_label=tk.CTkLabel(master=self.right_frame,text="Sign In",font=('Arial',32),anchor='nw',width=500,height=100)
    self.heading_label.pack(pady=40,padx=30)
    self.ID = tk.CTkEntry(master=self.right_frame, placeholder_text="Enter ID",width=300,height=50,font=('Arial',18))
    self.ID.pack(pady=10, padx=20)
    self.Submit_ID = tk.CTkButton(master=self.right_frame, text="Submit",width=180,height=40,font=("Arial",18),command=submit_id)
    self.Submit_ID.pack(pady=40,padx=30)

