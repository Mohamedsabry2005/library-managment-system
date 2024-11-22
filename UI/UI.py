import customtkinter as tk
from PIL import Image

class LibrarayApp(tk.CTk):
  def __init__(self):
    super().__init__()
    self.title('Library App')
    self.geometry('1000x600')
    self.resizable(False, False)
    self.screen_stack = ['main']
    self.PrevIcon=tk.CTkImage(Image.open("UI/Images/prev.png"), size=(20, 20))
    self.create_left_frame()
    self.create_right_frame()

    self.show_main_screen()

  def create_left_frame(self):
    self.left_frame = tk.CTkFrame(master=self, width=500)
    self.left_frame.pack(side='left', fill='both')

    self.hero_image = tk.CTkImage(Image.open("UI/Images/heroImg.jpg"), size=(500, 600))
    self.image_label = tk.CTkLabel(master=self.left_frame, image=self.hero_image, text='')
    self.image_label.pack(pady=20, padx=20)

  def create_right_frame(self):
    self.right_frame = tk.CTkFrame(master=self, width=500)
    self.right_frame.pack(side="right", fill='both', expand=True)

  def clear_right_frame(self):
    for widget in self.right_frame.winfo_children():
      widget.destroy()

  def button_click(self, button_text):
      # self.clear_right_frame()
      if button_text == "Sign In":
          self.show_sign_in_screen()
      elif button_text == "Sign Up":
          self.show_sign_up_screen()
      else:
          self.show_forget_id_screen()

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

  def show_sign_in_screen(self):
    self.screen_stack.append('sign_in')
    self.clear_right_frame()
    self.previous_button = tk.CTkButton(master=self.right_frame, text="",image=self.PrevIcon,width=30,height=30, command=self.show_previous_screen)
    self.previous_button.pack(side="top", anchor="nw", pady=20, padx=20)
    self.heading_label=tk.CTkLabel(master=self.right_frame,text="Sign In",font=('Arial',32),anchor='nw',width=500,height=100)
    self.heading_label.pack(pady=40,padx=30)
    self.ID = tk.CTkEntry(master=self.right_frame, placeholder_text="Enter ID",width=300,height=50,font=('Arial',18))
    self.ID.pack(pady=10, padx=20)
    self.Submit_ID = tk.CTkButton(master=self.right_frame, text="Submit",width=180,height=40,font=("Arial",18))
    self.Submit_ID.pack(pady=40,padx=30)

  def show_sign_up_screen(self):
    self.screen_stack.append('sign_up')
    self.clear_right_frame()
    self.previous_button = tk.CTkButton(master=self.right_frame, text="",image=self.PrevIcon,width=30,height=30, command=self.show_previous_screen)
    self.previous_button.pack(side="top", anchor="nw", pady=20, padx=20)
    self.heading_label=tk.CTkLabel(master=self.right_frame,text="Sign Up",font=('Arial',32),anchor='nw',width=500,height=100)
    self.heading_label.pack(pady=40,padx=30)
    self.name = tk.CTkEntry(master=self.right_frame, placeholder_text="Enter Name",width=300,height=50,font=('Arial',18))
    self.name.pack(pady=10, padx=20)
    self.age = tk.CTkEntry(master=self.right_frame, placeholder_text="Enter age",width=300,height=50,font=('Arial',18))
    self.age.pack(pady=10, padx=20)
    self.Identification_number = tk.CTkEntry(master=self.right_frame, placeholder_text="Enter Identification Number",width=300,height=50,font=('Arial',18))
    self.Identification_number.pack(pady=10, padx=20)
    self.Submit = tk.CTkButton(master=self.right_frame, text="Submit",width=180,height=40,font=("Arial",18))
    self.Submit.pack(pady=40,padx=30)

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


app=LibrarayApp()
app.mainloop()