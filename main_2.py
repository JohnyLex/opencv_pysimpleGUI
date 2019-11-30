import cv2, PySimpleGUI as sg
cv_integration =[
    [sg.Button(button_text='Capture'),sg.Button(button_text='Cancel'),sg.Text('Give name of capturing foto'),sg.Input(size=(20,1))]
]
window = sg.Window(' OpenCV Integration-Foto by Soft', [[sg.Image(filename='', key='image')],], location=(800,400)).layout(cv_integration)
cap = cv2.VideoCapture(0)   
check, frame = cap.read()    
while True:                     
    event, values = window.Read(timeout=20, timeout_key='timeout')      
    if event is None:  break                                            
    window.FindElement('image').Update(data=cv2.imencode('.png', cap.read()[1])[1].tobytes())
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
            img_resized = cv2.imwrite(filename=f'{foto_name}', img=img_)
            print("Image saved!") 
            break
    if event in (None,'Cancel'):
            print("Turning off camera.")
            cap.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
    window.FindElement('image').Update(data=cv2.imencode('.png', cap.read()[1])[1].tobytes())

if buttons in (None, 'Cance'):
    exit() 
