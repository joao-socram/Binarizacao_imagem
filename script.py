# Código binariza imagem em preto e branco e tons de cinza

import cv2

def binarizar_imagem_niveis_de_cinza(imagem_path, limiar):
    # Carregar a imagem em escala de cinza
    imagem = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)

    # Aplicar a binarização com base no limiar
    _, imagem_binarizada = cv2.threshold(imagem, limiar, 255, cv2.THRESH_BINARY)

    # Exibir a imagem original e a binarizada
    cv2.imshow('Imagem Original', imagem)
    cv2.imshow('Imagem Binarizada', imagem_binarizada)

    # Aguardar o usuário pressionar uma tecla e fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Substitua 'caminho/para/sua/imagem.jpg' pelo caminho real da sua imagem
caminho_da_imagem = r'C:\Users\F0453\Downloads\lulu.jpg'

# Defina o limiar de binarização (um valor entre 0 e 255)
limiar_de_binarizacao = 127

# Chame a função para binarizar a imagem em níveis de cinza
binarizar_imagem_niveis_de_cinza(caminho_da_imagem, limiar_de_binarizacao)
