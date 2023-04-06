import math
import numpy as np
import pygame
import time

from PyQt5.QtWidgets import QApplication, QDial, QWidget, QVBoxLayout
from PyQt5.QtGui import QColor
from PyQt5 import QtGui
from PyQt5.QtCore import Qt



# Manejador de eventos para el desplazamiento de la rueda del mouse
def wheelEvent(event):
    global freq, angle_per_sample
    delta = event.angleDelta().y()
    freq += delta / 8  # Dividimos por 8 para disminuir la sensibilidad del dial
    freq = max(dial.minimum(), min(dial.maximum(), freq))
    dial.setValue(freq)
    angle_per_sample = 2.0 * math.pi * freq / sample_rate

# Configuración de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Frecuencia y duración del tono
freq = 2
duration = 5

# Número de muestras por segundo
sample_rate = 44100

# Calcula el número de muestras
num_samples = int(duration * sample_rate)

# Calcula la amplitud máxima
max_amplitude = 2 ** 15 - 1

# Calcula el ángulo por muestra
angle_per_sample = 2.0 * math.pi * freq / sample_rate

# Inicializa el array de datos de audio
data = []
for i in range(num_samples):
    # Calcula el valor de la muestra
    sample = int(max_amplitude * math.sin(i * angle_per_sample))

    # Agrega el valor de la muestra al array de datos de audio
    data.append(sample)

# Inicializa Pygame
pygame.init()

# Crea una superficie para dibujar la huella cimática
surface = pygame.Surface((width, height))

# Crea la ventana de la interfaz gráfica de usuario
app = QApplication([])
app.setStyle("Fusion")
palette = app.palette()
app.setStyleSheet("QWidget { background-color: %s }" % palette.color(palette.Background))
palette.setColor(palette.Base, QColor(53, 53, 53))
app.setPalette(palette)
palette.setColor(QtGui.QPalette.Base, QtGui.QColor(53, 53, 53))
app.setPalette(palette)
palettewidget = QWidget()
palettewidget.wheelEvent = wheelEvent

# Crea la perilla para ajustar la frecuencia
dial = QDial(palettewidget)
dial.setRange(50, 1000)
dial.setValue(freq)
dial.setFixedSize(200, 200)

# Conecta la señal de cambio de valor de la perilla a la función de actualización de la frecuencia
def update_freq(value):
    global freq, angle_per_sample
    freq = value
    angle_per_sample = 2.0 * math.pi * freq / sample_rate

dial.valueChanged.connect(update_freq)

# Agrega la perilla al diseño vertical de la ventana
layout = QVBoxLayout()
layout.addWidget(dial)
palettewidget.setLayout(layout)

# Muestra la ventana de la interfaz gráfica de usuario
palettewidget.show()

# Espera a que el usuario cierre la ventana
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Rueda del mouse hacia arriba
                freq += 10  # Aumenta la frecuencia
                freq = max(dial.minimum(), min(dial.maximum(), freq))
                dial.setValue(freq)
                angle_per_sample = 2.0 * math.pi * freq / sample_rate
            elif event.button == 5:  # Rueda del mouse hacia abajo
                freq -= 10  # Disminuye la frecuencia
                freq = max(dial.minimum(), min(dial.maximum(), freq))
                dial.setValue(freq)
                angle_per_sample = 2.0 * math.pi * freq / sample_rate

    # Genera el tono de audio
    pygame.mixer.init(frequency=sample_rate, devicename='hw:0,0')


    # sound = pygame.sndarray.make_sound(np.array(data))

    # # Reproduce el tono de audio
    # sound.play()

    # Dibuja la huella cimática
    t = time.time()
    x = width / 2
    y = height / 2
    for i in range(num_samples):
        dx = math.cos(i * angle_per_sample) * max_amplitude / 2
        dy = math.sin(i * angle_per_sample) * max_amplitude / 2
        pygame.draw.line(surface, (255, 255, 255), (x, y), (x + dx, y + dy))
        x += dx
        y += dy
    screen.blit(surface, (0, 0))

    # Actualiza la pantalla
    pygame.display.flip()

    # Espera hasta que sea el momento de generar la siguiente muestra
    while time.time() - t < 1.0 / sample_rate:
        pass

# Sale de Pygame
pygame.quit()
