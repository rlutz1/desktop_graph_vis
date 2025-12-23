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
    QWidget,
)

class NavigationPane(QWidget): # generally a QWidget

  def init_pane(self):
    layout = QVBoxLayout() # for now, a vbox is easiest

    option_box = QComboBox()
    option_box.addItems(["Testing", "1", "2", "3"])

    widgets  = [
      option_box
    ]

    for w in widgets:
      layout.addWidget(w)

    self.setLayout(layout)


  def __init__(self):
    super().__init__() # super initialization

    # idea is to have a layout, list of widgets, add widgets
    # to the layout, set this widget layout to the layout wanted,
    # then add this widget to the window as desired.
    self.init_pane()


