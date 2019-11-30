import cv2, PySimpleGUI as sg
cv_integration =[
    [sg.Button(button_text='Capture'),sg.Button(button_text='Cancel'),sg.Text('Give name of capturing foto'),sg.Input(size=(20,1))]
]
window = sg.Window(' OpenCV Integration-Foto by Soft', [[sg.Image(filename='', key='image')],], location=(800,400)).layout(cv_integration)
cap = cv2.VideoCapture(0)       
while True:                     
    event, values = window.Read(timeout=20, timeout_key='timeout')      
    if event is None:  break                                            
    window.FindElement('image').Update(data=cv2.imencode('.png', cap.read()[1])[1].tobytes()) 
