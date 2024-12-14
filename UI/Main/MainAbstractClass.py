import customtkinter as tk
from abc import ABC, abstractmethod


class MainApp(tk.CTk,ABC):
  def __init__(self):
    super().__init__()
    self._set_appearance_mode("dark")
    self.title('Book Library')
    self.geometry('1250x600')
    self.resizable(False, False)

  @abstractmethod
  def create_header(self):
    pass

  @abstractmethod
  def create_content(self):
    pass

  @abstractmethod
  def list_books(self,book_info):
    pass
