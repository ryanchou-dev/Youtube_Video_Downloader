from pytube import YouTube

import PySimpleGUI as sg
# Download dependencies with pip
error_message1 = ""
sg.change_look_and_feel('bluemono')

layout=[
    [sg.Text("What video do you want to download? (paste the link)")],
    [sg.InputText(key='link')],
    [sg.Text(error_message1)],
    [sg.Button('Submit'), sg.Button('Cancel')]
]

window = sg.Window("Youtube Video Downloader", layout, resizable=True, element_justification="c").Finalize()
window.Maximize()

while True:
    event, value = window.Read()
    if event in (None, 'Cancel'):
        break
    if event == 'Submit':
        try:
            link = value['link']
            yt = YouTube(link)
            ys = yt.streams.get_by_itag('18')
            ys.download('Downloads')
            window.Close()
            error_message1 = "Completed. Check your Downloads Folder."
            layout=[
                [sg.Text("What video do you want to download? (paste the link)")],
                [sg.InputText(key='link')],
                [sg.Text(error_message1)],
                [sg.Button('Submit'), sg.Button('Cancel')]
            ]

            window = sg.Window("Youtube Video Downloader", layout, resizable=True, element_justification="c").Finalize()
            window.Maximize()
            event, value = window.Read()
        except:
            error_message1 = "Couldn't read that, try again."
            window.Close()
            layout=[
                [sg.Text("What video do you want to download? (paste the link)")],
                [sg.InputText(key='link')],
                [sg.Text(error_message1)],
                [sg.Button('Submit'), sg.Button('Cancel')]
            ]

            window = sg.Window("Youtube Video Downloader", layout, resizable=True, element_justification="c").Finalize()
            window.Maximize()
            event, value = window.Read()


