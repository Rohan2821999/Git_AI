# An Artificially Intelligent Virtual Assistant for tasks like Home Automation, Websearches and artifical learning algorithm
# Developer: Rohan Hundia

import urllib
import urllib2 
import json
import datetime
import time
import serial
import poplib
import webbrowser
import smtplib
import linecache
from collections import Counter
import pyttsx
import mp3play
import speech_recognition as sr 
from email import parser
variable=1
i=1
h=[]
file2=open("output.txt","a+") # Creating a txt file whereby all the new commands are stored which the system hasn't known previously
list=time.strftime("%H")
str1=raw_input("").lower()
engine = pyttsx.init()                  # Using Google Text to Speech API for voice Output                
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
c= urllib2.urlopen('http://api.wunderground.com/api/95a13755c3be7e1e/geolookup/conditions/q/IN/Ahmedabad.json') # Weather Data Logger from weather station at my House
json_string = c.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_c = parsed_json['current_observation']['temp_c']
precip_today_string = parsed_json['current_observation']['precip_today_string']
relative_humidity = parsed_json['current_observation']['relative_humidity']
c.close()
c= urllib2.urlopen('http://timesofindia.indiatimes.com/feeds/newsdefaultfeeds.cms?feedtype=sjson') # Times of India API for news and Parsing it in Java Script Object Notation
json_string = c.read()
parsed_news = json.loads(json_string)
news=parsed_news['NewsItem'][1]['HeadLine']
news1=parsed_news['NewsItem'][0]['Caption']
news4=parsed_news['NewsItem'][3]['HeadLine']
news4a=parsed_news['NewsItem'][3]['Caption']
news5=parsed_news['NewsItem'][4]['Caption']
news6=parsed_news['NewsItem'][5]['Caption']
news7=parsed_news['NewsItem'][6]['Caption']
news8=parsed_news['NewsItem'][7]['Caption']
news9=parsed_news['NewsItem'][9]['Caption']
news10=parsed_news['NewsItem'][10]['Caption']
news11=parsed_news['NewsItem'][11]['Caption']
news12=parsed_news['NewsItem'][12]['Caption']
news13=parsed_news['NewsItem'][14]['Caption']
news14=parsed_news['NewsItem'][15]['Caption']
news15=parsed_news['NewsItem'][16]['Caption']
today=datetime.date.today()
try:
    defserial = serial.Serial('com3', 9600) # Serial Port  Communication with Arduino Uno Microcontroller for controlling devices at my house wirelessly
except:
    pass
time.sleep(2)
r = sr.Recognizer()
while True:
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    my_str=raw_input("").lower()
    keywords=""
    for char in my_str:
        if char not in punctuations:
            keywords= keywords + char
    if str1=='hello jarvis' or "hey jarvis":
        if"light" in keywords:
            if"on" in keywords:
                try:
                    defserial.write('3')
                    print("I will switch on the light in your room. It is now on!")
                    engine.say('I will switch on the light in your room. It is now on!')
                    engine.runAndWait()
                    a=file2.write(list+"\n")
                except:
                    print('Your UART module is not connected to Port 3')
                    engine.say('Your UART module is not connected to Port 3')
                    engine.runAndWait()
                    pass
            if"off" in keywords:
                try:
                    defserial.write('6')
                    print("I will Switch off the Fan. It is now off!")
                    engine.say('I will switch off the Fan.It is now off!')
                    engine.runAndWait()
                except:
                    print("Your UART module is not connected to Port 13")
                    engine.say('Your UART module is not connected to Port 13')
                    engine.runAndWait()
        elif"weather" or "temperature"in keywords:
            print("Current temperature in %s is: %s Celsius and a relative humidity of: %s" % (location, temp_c,relative_humidity))
            engine.say('Current temperature in %s is: %s Celsius and a relative humidity of: %s' % (location, temp_c,relative_humidity))
            engine.runAndWait()
        elif"search" in keywords: # Search Query Code to search about anything unkown
            engine.say('Sir, What should I search about?')
            engine.runAndWait()
            SearchInput = raw_input( 'Sir, What should I search about?:')
            query2 = urllib.urlencode ( { 'q' : SearchInput } )
            response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query2 ).read()
            json = json.loads (response)
            results = json [ 'responseData' ] [ 'results' ]
            for result in results:
                title = result['title']
                url = result['url']
                webbrowser.open(result['url'])
            print("Here is the Information about"+SearchInput)
            engine.say('Here is the Information about'+SearchInput)
            engine.runAndWait()
        elif"send" in keywords: # Utilizing smtlib library to send messages via mail user
            engine.say("What message should I send?")
            engine.runAndWait()
            print("What message should I send")
            content=raw_input("")
            mail=smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login('rohanhundia@gmail.com','password_hidden')
            engine.say("Enter the Receiver's Email Address:")
            engine.runAndWait()
            rec = raw_input("Enter the Receiver's Email Address:")
            mail.sendmail('rohanhundia@gmail.com',rec,content)
            print("Your message has been sent")
            engine.say('your message has been sent')
        elif keywords in open('read.txt').read(): # Two .txt files are created named raed.txt (All the questions and queries are stored here) and read2.txt (all the answers to the questions of the previous file are stored here)
            file='read.txt'   # For every query stored in the read.txt file Jarvis seeks an answer to that query from read2.txt
            word=keywords
            with open(file, 'r') as text:
                for num,line in enumerate(text):
                    if word in line:
                        num
                        k=linecache.getline('read2.txt', num+1)
                        print(k)
                        engine.say(k)
                        engine.runAndWait()
        else:
             file3=open("read.txt","a+") #opening a notepad file for appending text (
             file4=open("read2.txt","a+") # opening another notepad file for appending text
             file3.write(keywords+("\n"))# append the input given by the user
             print("Can You Tell me the answer")
             engine.say('Can You Tell me the answer')
             engine.runAndWait()
             str2=raw_input() #user has to give the meaning of previous input
             file4.write(str2+("\n"))#appending the meaning of input in another file
             file3.close()
             file4.close()
        file3=open("output.txt","r") # Output. txt file stores the time period when the 'light on' command is deployed the most (mode of time periods). Jarvis learns from this and automatically switches on the light at that time
        b=sum(1 for _ in file3)
        for i in range (1,b):
            h.append(linecache.getline('output.txt',i))
        data = Counter(h)
        mode=data.most_common(1)
        for word in mode:
            modefinal=word[:1]
        stringofmode = ''.join(modefinal)
        timestore=time.strftime("%H")
        if  timestore in stringofmode:
            if variable==1:
                    print("I have learnt that this is the time when you generally switch on the light.So, I have switched on the light automatically for you")
                    engine.say("I have learnt that this is the time when you generally switch on the light So, I have switched on the light automatically for you")
                    engine.runAndWait()
                    variable=variable+1
                    try:
                        defserial.write('3')
                    except:
                        pass

            
