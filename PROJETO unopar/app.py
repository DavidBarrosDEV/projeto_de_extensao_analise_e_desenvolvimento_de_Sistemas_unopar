import cv2
import numpy as np
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Determine o diretório do script atual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Crie o caminho absoluto para o arquivo haarcascade_car.xml no mesmo diretório do script
cascade_file = os.path.join(script_dir, 'haarcascade_car.xml')

# Verifique se o arquivo existe antes de carregá-lo
if os.path.exists(cascade_file):
    car_cascade = cv2.CascadeClassifier(cascade_file)
else:
    raise FileNotFoundError(f"O arquivo 'haarcascade_car.xml' não foi encontrado em {cascade_file}")

# Inicialize o pygame para reproduzir alertas sonoros
pygame.mixer.init()

# Função para calcular a velocidade do carro
def calcular_velocidade(p1, p2, fps, largura_real):
    if p1 is None or p2 is None:
        return 0  # Retorna 0 km/h se a detecção de carro falhar
    distancia_pixeis = abs(p2 - p1)
    largura_real_metros = largura_real / 100  # Suponhamos que a largura real da estrada seja de 3.7 metros.
    distancia_metros = (distancia_pixeis / largura_real) * largura_real_metros
    velocidade_metros_segundo = distancia_metros * fps
    velocidade_km_hora = velocidade_metros_segundo * 3.6
    return velocidade_km_hora

# Função para abrir um vídeo
def abrir_video():
    global cap
    global video_path
    video_path = filedialog.askopenfilename()
    cap = cv2.VideoCapture(video_path)
    # Atualize o rótulo para mostrar o arquivo importado
    arquivo_importado_label.config(text=f"Arquivo Importado: {video_path}")

# Função para iniciar a detecção de velocidade
def iniciar_detecao():
    global cap
    global frame_count
    global max_speed_kmh

    # Verifique se o campo de velocidade máxima está preenchido
    if not velocidade_maxima_entry.get():
        messagebox.showerror("Erro", "Por favor, preencha o campo de velocidade máxima.")
        return

    largura_real_da_estrada = 370  # A largura real da estrada em centímetros
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0
    max_speed_kmh = float(velocidade_maxima_entry.get())

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            if frame_count % 5 == 0:
                velocidade = calcular_velocidade(x, x+w, fps, largura_real_da_estrada)
                if velocidade is not None:
                    if velocidade > max_speed_kmh:
                        cor_texto = (0, 0, 255)  # Vermelho para velocidade acima do limite
                        pygame.mixer.Sound('alerta.wav').play()  # Reproduzir um alerta sonoro se a velocidade for excedida
                    else:
                        cor_texto = (0, 255, 0)  # Verde para velocidade dentro do limite
            
                    # Exiba a velocidade em tempo real sobre o carro detectado com a cor apropriada
                    cv2.putText(frame, f"Velocidade: {int(velocidade)} km/h", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, cor_texto, 2)

        cv2.imshow('Detecção de Velocidade de Carros', frame)
        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Função para iniciar a detecção em tempo real
def iniciar_detecao_em_tempo_real():
    global cap
    global frame_count
    global max_speed_kmh

    # Verifique se o campo de velocidade máxima está preenchido
    if not velocidade_maxima_entry.get():
        messagebox.showerror("Erro", "Por favor, preencha o campo de velocidade máxima.")
        return

    largura_real_da_estrada = 370  # A largura real da estrada em centímetros
    fps = 30  # Taxa de quadros por segundo para a câmera em tempo real
    frame_count = 0
    max_speed_kmh = float(velocidade_maxima_entry.get())

    cap = cv2.VideoCapture(0)  # Usar a câmera em tempo real

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            if frame_count % 5 == 0:
                velocidade = calcular_velocidade(x, x+w, fps, largura_real_da_estrada)
                if velocidade is not None:
                    if velocidade > max_speed_kmh:
                        cor_texto = (0, 0, 255)  # Vermelho para velocidade acima do limite
                        pygame.mixer.Sound('alerta.wav').play()
                    else:
                        cor_texto = (0, 255, 0)  # Verde para velocidade dentro do limite
                
                    # Exiba a velocidade em tempo real sobre o carro detectado com a cor apropriada
                    cv2.putText(frame, f"Velocidade: {int(velocidade)} km/h", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, cor_texto, 2)

        cv2.imshow('Detecção de Velocidade de Carros em Tempo Real', frame)
        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Função para fechar a janela da câmera e liberar os recursos
def fechar_janela():
    global cap
    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()
    root.quit()

# Crie a janela da interface
root = tk.Tk()
root.title("Detecção de Velocidade de Carros")

# Defina o tamanho da janela como o de um celular
largura = 360
altura = 640
root.geometry(f"{largura}x{altura}")

# Personalize as cores da interface para preto e amarelo
root.configure(bg="black")
root.option_add("*Button.Background", "yellow")
root.option_add("*Button.Foreground", "black")
root.option_add("*Label.Background", "black")
root.option_add("*Label.Foreground", "yellow")
root.option_add("*Entry.Background", "white")
root.option_add("*Entry.Foreground", "black")

# Rótulo para mostrar o arquivo importado
arquivo_importado_label = tk.Label(root, text="", bg="black", fg="yellow")
arquivo_importado_label.pack()

# Botão para abrir um vídeo
abrir_video_button = tk.Button(root, text="Abrir Vídeo", command=abrir_video)
abrir_video_button.pack()

# Entrada para definir a velocidade máxima
velocidade_maxima_label = tk.Label(root, text="Velocidade Máxima (km/h):", bg="black", fg="yellow")
velocidade_maxima_label.pack()
velocidade_maxima_entry = tk.Entry(root)
velocidade_maxima_entry.pack()

# Botão para iniciar a detecção
iniciar_detecao_button = tk.Button(root, text="Iniciar Detecção em Vídeo", command=iniciar_detecao)
iniciar_detecao_button.pack()

# Botão para iniciar a detecção em tempo real
iniciar_detecao_tempo_real_button = tk.Button(root, text="Iniciar Detecção em Tempo Real", command=iniciar_detecao_em_tempo_real)
iniciar_detecao_tempo_real_button.pack()

# Botão para fechar a janela
fechar_janela_button = tk.Button(root, text="Fechar", command=fechar_janela)
fechar_janela_button.pack()

# Parâmetros para a detecção de carros
car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

# Manipulador de evento para fechar a janela
root.protocol("WM_DELETE_WINDOW", fechar_janela)

root.mainloop()
