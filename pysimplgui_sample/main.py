import PySimpleGUI as sg

# Layouts
layout = [
    [
        sg.Button('Push', size=(30, 3), key='BUTTON_1'),
    ],
    [
        sg.Button('Push', size=(30, 3), key='BUTTON_2'),
    ],
]

window = sg.Window(title="Window title", layout=layout)
window.finalize()

while True:
    event, values = window.read(timeout=None)
    # 変更部分
    print('Event: ', event)
    print('Values: ', values)
    # 変更部分終わり
    if event is None:
        break
window.close()
