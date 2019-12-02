import cv2 
import PySimpleGUI as sg
import string
import tensorflow.keras
from PIL import Image
import numpy as np
key = cv2. waitKey(1)
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
opencv='opencv'
values = {'val': opencv}
cap = cv2.VideoCapture(0)
t = string.Template("""
----------------Bine ati venit-----------------
Acest program a fost creat in scopuri educative
pentru a arata posibilitatile inteligentei 
artificiale.Au fost folosite librariile tensorflow
pysimplegui ${val} si altele pentru ca acest mini 
program sa fie implementat.
Programul este destinat studentilor , profesorilor
si persoanelor interesate de procesarea foto/video
si utilizarea ulteriora a acestor in probleme de cla-
sificare si automatizare a diferitor procese de zi cu
zi.
-------------------------------------------------
Daca doriti sa continuati utilizarea acestui produs 
apasati butonul 'START' pentru esire apasati'EXIT'
-------------------------------------------------
Va dorim o experienta placuta in procesul utilizarii
softului. Suntem deschisi la idei de imbunatarie si 
dezvoltare a produsului.
""")
sg.change_look_and_feel('Topanga')
first_form=[[sg.Text(t.substitute(values),text_color='Orange',justification='center',auto_size_text=True)],
            [sg.Button(button_text='START'),sg.Button(button_text='EXIT')]

]
wind =sg.Window('Valute_Detector',size=(400,400),auto_size_text=True).layout(first_form)
butt , output =wind.read()

if butt in (None,'START'):
    wind.close()
    lay = [[sg.Text('Name    '),sg.Input(size=(20,1))],
       [sg.Text('Forname'),sg.Input(size=(20,1))],
       [sg.Text('Age       '),sg.Input(size=(20,1))],
       [sg.Text('Make Foto from CAM'),sg.Radio('With Soft Keys', "RADIO1", default=False),sg.Radio('With breadbord buttons', "RADIO2", default=False)],
       [sg.Button(button_text='Registration'),sg.Button(button_text='Cancel')]
       ]
    windows =sg.Window('Registration Form ').layout(lay)
    buttons , values =windows.read()
if butt in (None,'EXIT'):
    sg.popup(title='GoodBy',custom_text='GoodBy')
    exit()
if buttons in (None,'Registration'):
    age = int(values[2])
    name = values[0]
    fname = values[1]
    values ={'Forname':fname,'name':name,'age':age}
    t = string.Template("""
    Name    : $name
    Vorname : $Forname
    Age     : $age
    """)
    print('Client information:',t.substitute(values))
    cv_integration =[
    [sg.Button(button_text='Capture'),sg.Button(button_text='Cancel'),sg.Text('Give name of capturing foto'),sg.Input(size=(20,1))]
    ]
    windo = sg.Window(' OpenCV Integration-Foto by Soft', [[sg.Image(filename='', key='image')],], location=(800,400)).layout(cv_integration)
    
    
    
    while True:
        check, frame = cap.read()
        event, values = windo.Read(timeout=20, timeout_key='timeout') 
        foto_name=[values[0]]
        
        
        if event in (None,'Capture'):
            cv2.imwrite(filename=f'{foto_name}.jpg', img=frame)
            cap.release()
            image = Image.open(f'{foto_name}.jpg')
            # Make sure to resize all images to 224, 224 otherwise they won't fit in the array
            image = image.resize((224, 224))
            image_array = np.asarray(image)
            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            # Load the image into the array
            data[0] = normalized_image_array
            # run the inference
            prediction = model.predict(data)
            print(prediction) 
            break
        if event in (None,'Cancel'):
            print("Turning off camera.")
            cap.release()
            cv.destroyAllWindows()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
        windo.FindElement('image').Update(data=cv2.imencode('.png', cap.read()[1])[1].tobytes())

if buttons in (None, 'Cance'):
    exit()
cap.release()
cv2.destroyAllWindows()













