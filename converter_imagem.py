import cv2

# Caminho para a imagem
caminho_imagem = 'sua_imagem.jpg'  # Substitua pelo nome do arquivo da sua imagem

# 1. Carregar a imagem colorida
imagem_colorida = cv2.imread(caminho_imagem)

# 2. Converter para escala de cinza
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# 3. Binarizar a imagem (usando limiar 127)
# Tudo abaixo de 127 vira 0 (preto), acima vira 255 (branco)
_, imagem_binarizada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

# 4. Exibir as imagens (opcional)
cv2.imshow('Imagem Colorida', imagem_colorida)
cv2.imshow('Imagem em Tons de Cinza', imagem_cinza)
cv2.imshow('Imagem Binarizada (Preto e Branco)', imagem_binarizada)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. (Opcional) Salvar as imagens geradas
cv2.imwrite('imagem_cinza.jpg', imagem_cinza)
cv2.imwrite('imagem_binarizada.jpg', imagem_binarizada)
