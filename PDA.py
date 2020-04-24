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
layout = [  [sg.Text('Welcome To Personal Digital Assistant Built By Olawale Micheal Juwon')],
            [sg.Text('Ask me anything?'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Personal Digital Assistant', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    try:
        try:
            res = client.query(values[0])
            sg.Popup("Intelligence 1:", next(res.results).text, "Click OK to run another check")
        except (StopIteration, AttributeError):
            sg.Popup("Intelligence 1:", "Ops! I found No Result, Click the button below and wait while i run another intelligence check ......")
        try:
            sg.Popup(wikipedia.summary(values[0], sentences=2))
        except wikipedia.exceptions.PageError:
            sg.Popup("Intelligence 2:", "Oh lads! I couldn't find anything, am still a learner.Kindly report to my master by sending a mail to olawalejuwon@gmail.com", "Thank You")
        except wikipedia.exceptions.DisambiguationError:
            sg.Popup("Intelligence :", "I found similar meaning related to", values[0], "Please simplify it and try again")    
    except:
        sg.PopupNonBlocking("check your connection")
        engine.say("Please Check Your Internet Connection")
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
