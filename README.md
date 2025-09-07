# 🖼️ Conversão de Imagens: RGB → Tons de Cinza → Binarização

Este projeto em Python demonstra como converter imagens coloridas para tons de cinza (0 a 255) e aplicar binarização (0 e 255 - preto e branco) usando a biblioteca OpenCV.

Ideal para estudantes, entusiastas de visão computacional e machine learning que desejam entender o pré-processamento de imagens.


# 🎯 Objetivo

Transformar imagens RGB em grayscale

Aplicar binarização simples com limiar fixo

(Opcional) Aplicar binarização com Otsu

Salvar e visualizar os resultados


# 🧰 Tecnologias utilizadas

Python 3.x

OpenCV (cv2)

# 📷 Exemplo de código

Converter para tons de cinza : 

imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

Aplicar binarização com limiar 127 

_, imagem_binarizada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)
