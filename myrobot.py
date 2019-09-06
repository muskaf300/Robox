from time import gmtime, strftime   
import random
from datetime import date
import time
from selenium import webdriver
import sys
import math
import os

#this program was desinged to see how many elifs, if and else statement im gonna use to design a bot like this and using one class
#never the less there are different ways we can write this program
#program was designed by novice programmer
#lines of code 143 with only one class and loops, no functions and constructors

class Robot:

	today = date.today()
	while 1:
		create= input("Hello What Happened You Ran Me Today ")
		emotional_expression=[' Wow you have a nice name', ' Beautiful you have the name of a Prophet', ' You are fantastic']
		greet=['Hey ', 'Hello', 'Hi', 'Asslamualaikum ']
		prayer=['May Allah Reward You Brother ','May Allah Grant You Entrance into Paradise ', 
		' May Allah Forgive You For All Your Sins ', ]
		help_section=("""
this is a manual for this software
version = for version of software
save a file = for creating new file eg .txt .html .php .py etc..
time= for time
date= for current date
automate = for internet automation
count to 100= to count from 1 to 100
count to 500= to count from 1 to 500
count to 1000= to count from 1 to 1000
count to 10000= to count from 1 to 10000
count to 5000= to count from 1 to 5000
shutdown -h = to hibernate
shutdown -s = to shutdown
terminal = to open power shell
command = to open cmd
squareroot = for square root

	""")
		name_of_robot="Robox"
		
		if create == "date":
			print("Todays date is ",today)
		if create == "time":
			print(strftime("%H:%M:%S", gmtime())) 
		elif create == "admin":
			print("iam the admin of my self")
		elif create == "version":
			print("V.1.3 ")
		elif create =="whats my name":
			print("your name? that i dont know but you can tell me")
			time.sleep(3)
			name=input("Whats your name? ")
			print("Hello " + name + random.choice(emotional_expression))
		elif create =="Assalamualaikum".lower():
			print("Waalaikumussalam")
			time.sleep(2)
			muslim=input("Whats your name my muslim brother? ")
			print(random.choice(prayer)+muslim.upper()+"\nGood bye"+muslim.upper())
		elif create == "count to 1000":
			for i in range(1,1000):
				print(i)
		elif create == "Who are you".lower():
			print("Thinking...")
			time.sleep(3)
			print("You can call me " + name_of_robot)
		#elif create =="Change name".lower():
			#new_name=input("Enter new name:")
			#print("Name changed to " + new_name)
		elif create =="Terminal".lower():
			print("opening Terminal")
			time.sleep(2)
			os.system("powershell")
		elif create =="Command".lower():
			print("opening Command Line")
			time.sleep(2)
			os.system("cmd")
		elif create == "count to 100":
			for i in range(1,100):
				print(i)
		elif create == "count to 50":
			for i in range(1,50):
				print(i)
		elif create == "count to 500":
			for i in range(1,500):
				print(i)
		elif create == "count to 5000":
			for i in range(1,5000):
				print(i)
		elif create == "count to 10000":
			for i in range(1,10000):
				print(i)
		elif create == "convert to dollar".lower():
			num1=int(input("enter amount in naira: "))
			print("the amount in dollar is: ", num1/360)
		elif create == "convert to naira".lower():
			num1=int(input("enter amount in dollar: "))
			print("the amount in naira is: ", num1*360)
		elif create == "Hibernate".lower():
			os.system("shutdown -h")
		elif create == "Shutdown".lower():
			os.system("shutdown -s -t01")

		elif create == "squareroot".lower():
			num=int(input("enter number: "))
			print(math.sqrt(num))
		elif create == 'automate'.lower():
			print("loading.....")
			time.sleep(2)
			driver=webdriver.Chrome('chromedriver.exe')
			driver.get("")
			driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/a[2]').click()
			time.sleep(2)
			driver.find_element_by_xpath('//*[@id="registration_name"]').send_keys('')
			time.sleep(2)
			driver.find_element_by_xpath('//*[@id="registration_email"]').send_keys('')
			time.sleep(2)
			driver.find_element_by_xpath('//*[@id="registration_password"]').send_keys('')
			time.sleep(2)
			driver.find_element_by_xpath('//*[@id="registration_password_confirmation"]').send_keys('')
			time.sleep(2)
			driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[5]/button').click()
			time.sleep(15)
			driver.find_element_by_xpath('//*[@id="session_email"]').send_keys('')
			driver.find_element_by_xpath('//*[@id="session_password"]').send_keys('')
			driver.find_element_by_xpath('/html/body/div[2]/div/div/form/div[3]/button').click()
			"""driver.get("https://www.gmail.com")
												time.sleep(2)
												driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('Abdulmalik573@gmail.com')
												time.sleep(3)
												driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
												time.sleep(5)
												driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('tal')
												time.sleep(2)
												driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()"""
		elif create == "save a file".lower():
			filename=input('filename: ')
			writefile=input('write inside filename: ')
			extension=input('Enter extension e.g .txt, .pdf, .html etc: ')
			file=open(filename+'.'+extension,'w')
			file.write(writefile)
			file.close()

		elif create == 'help'.lower():
			print(help_section)
		elif create == 'exit'.lower():
			sure=input("are you sure you wanna exit?")
			if sure == "yes".lower():
				sys.exit()
	 # this is a reminder you use a while loop to continously run programm 

	
			










robot=Robot()
