import cv2 
import PySimpleGUI as sg
import string
key = cv2. waitKey(1)

opencv='opencv'
values = {'val': opencv}
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
    cap = cv2.VideoCapture(0)
    check, frame = cap.read()
    
    
    while True:
        event, values = windo.Read(timeout=20, timeout_key='timeout') 
        foto_name=[values[0]]
        if event in (None,'Capture'):
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            cap.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray,(28,28))
            print("Resized...")
            img_resized = cv2.imwrite(filename='sd.jpg', img=img_)
            print("Image saved!") 
            break
        if event in (None,'Cancel'):
            print("Turning off camera.")
            cap.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
        windo.FindElement('image').Update(data=cv2.imencode('.png', cap.read()[1])[1].tobytes())

if buttons in (None, 'Cance'):
    exit()














