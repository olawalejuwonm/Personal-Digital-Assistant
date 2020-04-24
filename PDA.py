import wolframalpha
client = wolframalpha.Client("THXGAJ-WHX823RHKG")
# try:
#     res = client.query('Barack Obama')
#     print(next(res.results).text)
# except StopIteration:
#     print("No result")

import wikipedia
# try:
#     print(wikipedia.summary("micheal", sentences=1))
# except wikipedia.exceptions.PageError:
#     print("No Result")
 

import pyttsx3
engine = pyttsx3.init()

import PySimpleGUI as sg




sg.theme('LightBlue')	# Add a touch of color
# All the stuff inside the window are here.
layout = [  [sg.Text('Welcome To Personal Digital Assistant Developed By Olawale Micheal Juwon')],
            [sg.Text('Enter A Prompt'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Personal Digital Assistant', layout)
# Event Loop to process "events" and get the "values" of the inputs
sg.PopupNonBlocking("How It Works","This Personal Digital Assistant, has two intelligence model.Intelligence 1 will try to respond to your prompt directly, while intelligence 2 can also handle your request or convert it to something similar.Intelligence 1 is modelled for answering mostly calculations, statistics, weather forecast etc. Intelligence 2 can help with History,Documentations, Personalities. Instead of asking who is Barack Obama, simply type 'Barack Obama'.The zen of this application is 'Simple Is Better Than Complex'. So make it simple")
engine.say("Welcome To Your Personal Digital Assistant")
engine.runAndWait()






while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
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
           


    try:
        try:
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
            sg.PopupNonBlocking("Please Enter A Prompt")
            engine.say("Please Enter A Prompt")

            
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
            engine.say("I can't assist without your command")  

    except:
        sg.PopupNonBlocking("check your connection")
        engine.say("Please Check Your Internet Connection")
        engine.runAndWait()
    engine.runAndWait()


            


    # wiki_res = wikipedia.search(values[0])
    # res = client.query(values[0])
    # wolfrem_res = next(res.results).text
    # # wiki_res = wikipedia.summary(values[0], sentences=1)
    # # wiki_res = wikipedia.page(values[0])
    # # print(next(res.results).text)
    # # print(values[0])
    # sg.Popup("Intelligence 1: ", wolfrem_res, "Intelligence 2: ", wiki_res)


window.close()
