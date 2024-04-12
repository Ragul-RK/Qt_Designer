from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class CircularProgress(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # CUSTOM PROPERTIES
        self.value = 25
        self.max_value = 75
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = True
        self.progress_color = 0x498BD1
        self.font_family = "Segoe UI"
        self.font_size = 12
        self.suffix = "%"
        self.text_color = 0x498BD1
        self.enable_shadow = True
        
        # SET DEFAULT SIZE WITHOUT LAYOUT
        self.resize(self.width, self.height)
        
    # ADD DROPSHADOW
    def add_shadow(self, enable):
        if enable:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(1)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 80))
            self.setGraphicsEffect(self.shadow)
        
    # SET VALUE
    def set_value(self, value):
        self.value = value
        self.repaint()# Render progress bar after change value
    
    
    #PAINT EVENT (DESIGN YOUR CIRCULAR PROGRESS HERE)
    def paintEvent(self, event):
        # SET PROGRESS PARAMETTERS
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value
        
        #PAINTER
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing) # remove pixelated edges
        paint.setFont(QFont(self.font_family, self.font_size))
        
        # CREATE RECTANGLE
        rect = QRect(0, 0, self.width, self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)
        
        # PEN
        pen = QPen()
        pen.setColor(QColor(self.progress_color))
        pen.setWidth(self.progress_width)
        #Set Round Cap
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)
            
        #CREATA ARC / CIRCULAR PROGRESS
        paint.setPen(pen)
        paint.drawArc(margin, margin, width, height, -90 *16, -value * 16)#(x, y, w, h, a, alen) [(a) ark 360 is equal to 360*16 in the Qt, or 5760/16]
        
        #CREATE TEXT
        pen.setColor(QColor(self.text_color))
        paint.setPen(pen)
        paint.drawText(rect, Qt.AlignCenter, f"{self.value} {self.suffix} PIPE2.0") #   center text content
        
        
        # END
        paint.end()