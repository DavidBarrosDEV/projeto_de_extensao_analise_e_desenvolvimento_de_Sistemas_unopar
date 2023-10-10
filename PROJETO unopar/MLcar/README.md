# Projeto de Extensão: Detecção de Velocidade de Carros

## Introdução
Este projeto de extensão tem como objetivo desenvolver uma aplicação para a detecção de velocidade de carros em vídeos gravados ou em tempo real usando uma webcam. A aplicação utiliza a biblioteca OpenCV para processamento de vídeo, detecção de carros e cálculo da velocidade, além de incorporar funcionalidades de interface gráfica usando o módulo tkinter e alertas sonoros usando o módulo pygame. O projeto também depende de um arquivo de classificação em cascata (haarcascade) para a detecção de carros.

## Funcionalidades
O projeto oferece as seguintes funcionalidades:

1. **Carregamento de Vídeo:** Os usuários podem selecionar um arquivo de vídeo para análise. O projeto suporta vídeos gravados previamente.

2. **Definição da Velocidade Máxima:** Os usuários podem inserir a velocidade máxima permitida na estrada para fins de comparação.

3. **Detecção de Velocidade em Vídeo Gravado:** Os usuários podem iniciar a detecção de velocidade em vídeos gravados, com a aplicação exibindo as velocidades dos carros detectados e alertando quando a velocidade excede o limite definido.

4. **Detecção de Velocidade em Tempo Real:** Os usuários também têm a opção de iniciar a detecção de velocidade em tempo real usando uma webcam. A aplicação funciona de maneira semelhante à detecção em vídeo gravado, mas com entrada de vídeo ao vivo da câmera.

## Requisitos do Sistema
Para executar este projeto, é necessário ter os seguintes requisitos:

- Python 3.x
- OpenCV
- pygame
- tkinter (já incluído na maioria das instalações Python)
- Um arquivo de classificação em cascata para detecção de carros (haarcascade_car.xml)

## Uso da Aplicação
1. **Carregando um Vídeo:** Clique no botão "Abrir Vídeo" para selecionar um arquivo de vídeo. O caminho do arquivo será exibido na interface.

2. **Definindo a Velocidade Máxima:** Insira a velocidade máxima permitida na estrada em km/h no campo "Velocidade Máxima (km/h)".

3. **Iniciando a Detecção em Vídeo:** Clique no botão "Iniciar Detecção em Vídeo" para começar a análise do vídeo carregado. Os carros detectados serão exibidos com suas velocidades, e alertas sonoros serão reproduzidos quando a velocidade exceder o limite definido.

4. **Iniciando a Detecção em Tempo Real:** Clique no botão "Iniciar Detecção em Tempo Real" para começar a análise de vídeo em tempo real da webcam. O processo é semelhante ao da detecção em vídeo gravado.

5. **Finalizando a Detecção:** Para encerrar a detecção em qualquer momento, pressione a tecla "q" na janela de exibição do vídeo.

## Considerações Finais
Este projeto de extensão fornece uma solução simples para a detecção de velocidade de carros em vídeos gravados ou em tempo real. Ele pode ser útil para fins educacionais, de monitoramento de tráfego e de conscientização sobre velocidades permitidas. Certifique-se de ter os requisitos do sistema instalados e o arquivo de classificação em cascata (haarcascade_car.xml) disponível para usar a aplicação corretamente.

