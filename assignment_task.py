#!/usr/bin/python3

from itertools import permutations
import re


while True:
	try:
                T = int(input("Enter number of test cases between 1-100:"))
                break
	except:
		print("Please enter only nubers")

list=['null']*T              
if  0 < T < 101:
        for i in range(0,T):
                t=0
                print('\nTest case:{}'.format(i+1))
                ptrn = input("Enter first line (Pattern):")
                l1=len(ptrn)
                if 0 < l1 < 1001:
                    txt = input("Enter second line (text line):")
                    l2=len(txt)
                    if 0 < l2 < 100001:
                        perms1 = [''.join(p) for p in permutations(ptrn)]

                        for j in perms1:
                    
                           if re.search(j, txt):
                             t=1
                             list[i]="YES"
                             break
                    else:
                         print("Text string length must be between 1-100000")
 
                else:
                      print("Pattern length must be between 1-1000")
  
                if t==0:
                   list[i]="NO"
         
        print("\nTest result:")
        for opt in list:
               print(opt)
              
                                           
else:
	print("Please enter a number between 1-100 only")


