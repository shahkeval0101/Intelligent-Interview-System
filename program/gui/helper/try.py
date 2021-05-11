
import tkinter
import cv2
import PIL.Image, PIL.ImageTk


stopb = None

class App():
    def __init__(self, window, window_title):
        self.window = window
        self.window.title = window_title
        # Create a canvas that can fit the above video source size
        self.set_camera() #this needs to be set every time you open the camera

        self.canvas = tkinter.Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        self.opencamera = tkinter.Button(window, text="open camera", command=self.open_camera)
        self.opencamera.pack()
        self.closecamera = tkinter.Button(window, text="close camera", command=self.close_camera)
        self.closecamera.pack()
        self.delay = 10
        self.save_and_show()

        # After it is called once, the save_and_show method will be automatically called every delay milliseconds
        self.window.mainloop()

    def set_camera(self):
        self.ok = True
        self.video = cv2.VideoCapture(0)
        self.width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        #create videowriter
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('output.avi',self.fourcc,10,(640,480))
        
        

    def save_and_show(self):
        ret, frame = self.video.read()
        print("in save_and_show")
        if self.ok :
            # print("saving frame")
            self.out.write(frame)
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

            self.window.after(self.delay, self.save_and_show)

    def open_camera(self):
        # self.ok = True
        self.set_camera()
        print("camera opened")
        print(self.ok)


    def close_camera(self):
        print("camera closed")
        self.ok = False
        self.video.release()
        self.out.release()

    def __del__(self):
        if self.video.isOpened():
            self.video.release()
            self.out.release()


App(tkinter.Tk(), "mywindow")