import time
import sys

def countimer() :
  no_of_second = int(input("Enter The Timer :"))
  while no_of_second :
   if 0 <= no_of_second <= 3600:
     hrs = no_of_second // 3600
     min = no_of_second // 60
     sec = no_of_second % 60
     timer = '%02d:%02d:%02d' %(hrs , min , sec)
     print(timer , end='\r')
     time.sleep(1)
     no_of_second -= 1
 print("Time Up !!!")   
    
countimer()