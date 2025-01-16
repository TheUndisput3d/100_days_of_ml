import json
from tkinter import messagebox
class Database:

  def add_user(self, name, email, password):

    with open('resources/db.json', 'r') as rf:
      data = json.load(rf)

    if email not in data:
      data[email] = [name, password]
      with open('resources/db.json', 'w') as wf:
        json.dump(data, wf)
      return 1
    
    else:
      return 0
    
  def authenticate(self, email, password):

    with open('resources/db.json', 'r') as f:
      data = json.load(f)
    
    if email in data:
      if password == data[email][1]:
        return 1
        
      else:
        return 'wrong password'
    else:
      return 0
