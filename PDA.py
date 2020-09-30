#Ensure you checked the readme file before auditing the code
#welcome to the PDA, the unused code here, helps the reader to understand how some module works here
import os
import PySimpleGUI as sg #the GUI
import pyttsx3  #the speaking module
import wikipedia #intelligence 2

#the code below explain how multiple validation works
# if "play" or "tea" in "play":
#     print("mic")
import wolframalpha #intelligence 1

client = wolframalpha.Client("THXGAJ-WHX823RHKG") #The Application Interface (API)

#the code below give a glimpse of Intelligence 1 model
# try:
#     res = client.query('Barack Obama')
#     print(next(res.results).text)
# except StopIteration:
#     print("No result")

# try:
#     print(wikipedia.summary("micheal", sentences=1))
# except wikipedia.exceptions.PageError:
#     print("No Result")
 

engine = pyttsx3.init() #initializing the speaking engine

sg.theme('LightBlue')	# Adding a touch of color 
# All the stuff inside the window are here.

layout = [  [sg.Text('Welcome To Personal Digital Assistant Developed By Olawale Micheal Juwon')],
            [sg.Text('Enter A Prompt'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Creating the Window
window = sg.Window('Personal Digital Assistant', layout)
# Event Loop to process "events" and get the "values" of the inputs

#Introduction

sg.PopupNonBlocking("How It Works",
"This Personal Digital Assistant, has two intelligence model.Intelligence 1 will try to respond to your prompt directly, while intelligence 2 can also handle your request or convert it to something similar.", 
"Intelligence 1 is modelled for answering mostly calculations, statistics, weather forecast etc. Intelligence 2 can help with History,Documentations, Personalities.", 
"Instead of asking who is Barack Obama, simply type 'Barack Obama'.The zen of this application is 'Simple Is Better Than Complex'. So make it simple", 
"-Open: Any prompt starting with open will open a file present in this program directory. e.g open PDA.py  (Don't Forget The Extension)", 
"-Play: Any prompt starting with play will play a media file in the application directory e.g play testing.mp4 (Don't Forget The Extension) ")
engine.say("Welcome To Your Personal Digital Assistant")
engine.runAndWait() #stoping engine loop
#The engine speaks

while True: # The GUI looping
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break

    #The following explains how the intelligence models works
    # try:
    #     res = client.query(values[0])
    #     sg.Popup("Intelligence 1:", values[0], next(res.results).text, "Click OK to run another check")
    # except (StopIteration, AttributeError):
    #     engine.say("Ops! I found No Result for ", values[0],  " Click the OK button below and wait while i run another intelligence check.")
    #     sg.PopupNonBlocking("Intelligence 1:", "Ops! I found No Result for ", values[0],  " Click the button below and wait while i run another intelligence check ......")
    # except Exception:
    #     sg.PopupNonBlocking("Please Enter A Prompt")
    #     engine.say("Please Enter A Prompt")
         
            
    # try:
    #     sg.PopupNonBlocking(wikipedia.summary(values[0], sentences=2))
    # except wikipedia.exceptions.PageError:
    #     sg.PopupNonBlocking("Intelligence 2:", "Oh lads! I couldn't find anything relating to ", values[0],  "am still a learner.Kindly report to my master by sending a mail to olawalejuwon@gmail.com", "Thank You")
    # except wikipedia.exceptions.DisambiguationError:
    #     sg.PopupNonBlocking("Intelligence 2:", "I found similar meaning related to", values[0], "Please simplify it and try again")
    # except wikipedia.exceptions.WikipediaException:
    #     engine.say("I can't assist without your command")
          
    # if "open"  in values[0][0:4]:
    #     file_nameo = values[0][5:]
    #     sg.PopupNonBlocking("open", file_nameo)
    # elif "play" in values[0][0:4]:
    #     file_namep = values[0][5:]
    #     sg.PopupNonBlocking("play", file_namep)
    # else:
    #    sg.PopupNonBlocking(" It is not present ") 

    testo = values[0][0:4].lower() #testing open
    testp = values[0][0:4].lower() #testing play
    o_yes = 0                      #value for loop
    for prompt in values[0]:
        if prompt.isspace():
            o_yes += 1
    o_true = o_yes >= 1 and len(values[0]) > 5

    #opening of files and playing media   
    if "open"  == values[0][0:4].lower() and o_true == True: #checks for offline tasks
        file_name = values[0][5:]
        file_nameo = file_name.lower()
        if os.system(file_nameo) == 0:
            engine.say("File Opened")
            engine.runAndWait()
        else:
            sg.PopupNonBlocking(file_nameo, "Can't Be Found. Ensure That You Are In The Right Directory, And You Used The Right Extension. ")
            engine.say("Can't Open Your File")
            engine.runAndWait()
            
            #checking for play command

    elif "play" == values[0][0:4].lower() and o_true == True: 
        file_namea = values[0][5:]
        file_namep = file_namea.lower()
        if os.system(file_namep) == 0:
            engine.say("Media Played")
            engine.runAndWait()
        else:
            sg.PopupNonBlocking(file_namea, "Can't Be Found. Ensure That You Are In The Right Directory, And You Used The Right Extension. ")
            engine.say("Can't Open Your Media")
            engine.runAndWait()
            
    
    #Handling Online Tasks
      
    else:
        try: #catch internet connection error
            try:# Working with intelligence model 1
                res = client.query(values[0])
                intel_one = next(res.results).text
                sg.PopupNonBlocking("Intelligence 1:", values[0], intel_one, "Click OK to run another check")
                engine.say(intel_one)
                engine.runAndWait()
            
            except (StopIteration, AttributeError):
                sg.PopupNonBlocking("Intelligence 1:", "Ops! I found No Result for ", values[0],  " Click the button below and wait while i run another intelligence check ......")
                engine.say("Dear user, i couldn't get that, i'll try to run another check.")
                engine.runAndWait()
            except Exception:
                pass

            #intelligence model 2 

            try:
                intel_two = wikipedia.summary(values[0], sentences=1)
                sg.PopupNonBlocking(intel_two)
                engine.say(intel_two)
                engine.runAndWait()
            except wikipedia.exceptions.PageError:
                sg.PopupNonBlocking("Intelligence 2:", "Oh lads! I couldn't find anything relating to ", values[0],  "Am still a learner.Kindly report to my master by sending a mail to olawalejuwon@gmail.com", "Thank You")
                engine.say("Ops! I don't get that, am still learning.Kindly report to my master, by sending a mail to, olawalejuwon@gmail.com")
                engine.runAndWait()
            except wikipedia.exceptions.DisambiguationError:
                sg.PopupNonBlocking("Intelligence 2:", "I found many similar meaning related to", values[0], "Please make it simple and try again")
                engine.say("That's too complex for me,kindly simplify it and re-try.")
            except wikipedia.exceptions.WikipediaException:
                sg.PopupNonBlocking("Please Enter A Prompt")
                engine.say("I can't assist without your command")  

        except:
            sg.PopupNonBlocking("check your connection")
            engine.say("Please Check Your Internet Connection")
            engine.runAndWait()
        engine.runAndWait()


        
        
        #This explain the whole intelligence model


    # wiki_res = wikipedia.search(values[0])
    # res = client.query(values[0])
    # wolfrem_res = next(res.results).text
    # wiki_res = wikipedia.summary(values[0], sentences=1)
    # wiki_res = wikipedia.page(values[0])
    # print(next(res.results).text)
    # print(values[0])
    # sg.Popup("Intelligence 1: ", wolfrem_res, "Intelligence 2: ", wiki_res)


window.close()