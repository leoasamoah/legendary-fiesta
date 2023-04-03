import PySimpleGUI as sg
import pyttsx3

speaker = pyttsx3.init()

layout = [
    [sg.Text('Enter your text:'),],
    [sg.InputText(key='-INPUT-')],
    [sg.Text('Select a voice:')],
    [sg.Radio('Male', "RADIO1", default=True, key='male_voice'),
     sg.Radio('Female', "RADIO1", key='female_voice'),
     ],
    [sg.Text('VOLUME: '),
     sg.Slider(key='vol',range=(0,10), size=(18, 15), orientation='horizontal')],
    [sg.Button('Speak'), ], 
]

window = sg.Window('Speechify', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Speak':
        # Init the pyttsx3 engine
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        volume = engine.getProperty('volume')
        set_volume = values['vol']
        
        text = values['-INPUT-']

        voices = engine.getProperty('voices')

        # Set the type of Voice
        if values['male_voice']:
            engine.setProperty('voice', voices[0].id)
        elif values['female_voice']:
            engine.setProperty('voice', voices[1].id)
           
        engine.setProperty('volume', set_volume )
        engine.say(text)

        engine.runAndWait()


window.close()
