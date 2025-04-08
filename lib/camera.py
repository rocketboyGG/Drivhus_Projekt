from picamera2 import Picamera2, Preview

class Camera:
    def __init__(self):
        self.picam2 = Picamera2()
        config = self.picam2.create_preview_configuration(main={"size": (640, 480)})
        self.picam2.configure(config)
        self.picam2.start_preview(Preview.NULL)
    
    def capture_pic(self):
        self.picam2.start()
        self.picam2.start_and_capture_file("static/img/pic.jpg")
    
    def stop_camera():
        self.picam2.close()
