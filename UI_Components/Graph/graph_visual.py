from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QDrag
from PyQt5.QtCore import Qt, QPoint, QMimeData
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QStackedLayout,
    QScrollArea,
    QLayout,
    QWidget,
    QTabWidget
)

# ============================================================
# what we have in here is all widgets needed to create a 
# visual of all components of a graph.
# these are VISUALS ALONE, and have no functionality.
# ============================================================



class VertexWidget(QWidget): # Qlabel can hold the canvas

  _canvas_container = None
  _vertex_text = None
  _vertex_size = 100 # px x px
  _vertex_width = 3 # px width of the drawn circle
  _background_color = QColor(255, 255, 255) # white by default
  _vertex_color = QColor(0, 0, 0) # black by default

  def __init__(self, parent, text = None): 
    super().__init__(parent) # call to QWidget window super with parent widget
    self.setStyleSheet("max-width: 100px; max-height: 100px;")
    self._draw_vertex(text)

  # draw the vertex within this widget. we will use a canvas for more flexibility.
  # very basic for now though.
  def _draw_vertex(self, text):
    self._canvas_container = QLabel(parent = self)
    canvas = QPixmap(self._vertex_size, self._vertex_size)
    canvas.fill(self._background_color)
    self._canvas_container.setPixmap(canvas)
    canvas = self._canvas_container.pixmap()

    painter = QPainter(canvas)
    pen = QPen()
    pen.setWidth(self._vertex_width)
    pen.setColor(self._vertex_color) 
    painter.setPen(pen)

    half_vertex_size = self._vertex_size // 2 # for center of canvas positioning
    circle_radius = half_vertex_size - self._vertex_width # for fitting within the canvas including pen size
    center = QPoint(self.pos().x() + half_vertex_size, self.pos().y() + half_vertex_size)
    painter.drawEllipse(center, circle_radius, circle_radius)
    
    painter.end()
    self._canvas_container.setPixmap(canvas)

    if text is not None:
      layout = QStackedLayout()
      self.setLayout(layout)
      self._vertex_text = QLabel(text, parent = self)
      # self._vertex_text.setStyleSheet("background-color: red;") # for seeing where actual label is
      self._vertex_text.setAlignment(Qt.AlignCenter)
      self._vertex_text.setWordWrap(True)
      self._vertex_text.setMargin(5)

      layout.addWidget(self._vertex_text)
      layout.addWidget(self._canvas_container)
      
      layout.setStackingMode(QStackedLayout.StackingMode.StackAll)      

      # pen.setWidth(1)
      # pen.setColor(QColor(105, 105, 105))
      # painter.setPen(pen)
      # painter.drawText(QPoint(self.pos().x() + self._vertex_width + 2, self.pos().y() + half_vertex_size), text)
    
  def mouseMoveEvent(self, e):
    if e.buttons() == Qt.MouseButton.LeftButton:
        print("alskdnashdkasm")
        drag = QDrag(self)
        mime = QMimeData()
        drag.setMimeData(mime)
        drag.exec_(Qt.MoveAction)

    

  # this may not work, but keeping for notes for edges to always be pointing to the center of a vertex:
  # property posᅟ: QPoint
  # This property holds the position of the widget within its parent widget.
  # If the widget is a window, the position is that of the widget on the desktop, including its frame.
  # When changing the position, the widget, if visible, receives a move event ( moveEvent() ) immediately. If the widget is not currently visible, it is guaranteed to receive an event before it is shown.
  # By default, this property contains a position that refers to the origin 
  def get_position(self):
    return self.pos()

