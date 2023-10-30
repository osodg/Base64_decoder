#!/bin/python3

import base64
import os

def clear():
  os.system('clear')
  print('\n')

def reverse_encoding():
  ''' Decodes base64 and prints output
  .decode("utf-8") strips out everthing leaving clean output '''
  with open(f"{path}/{users_file}", "r") as file:
    for line in file:
      line = line.strip()
      decoded_file = base64.b64decode(line).decode('utf-8') 
      data = f"{decoded_file} is {line}"
      with open(f"{path}/output_text.txt", "a") as file:
        file.write(data)
        file.write('\n')
  print(f"\nYour file is in '{path}/output_text.txt'.\n")
  
      
clear()
users_file = input("Input path/file to be decoded:\n\t>>> ")
path = "/home/kali/Tools/Base64_decoder" #Change This

if __name__ == ("__main__"):
  reverse_encoding()