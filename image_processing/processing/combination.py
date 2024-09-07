import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

# Função para encontrar a diferença entre duas imagens
def find_difference(image1, image2):
    # Verifica se as duas imagens têm a mesma forma
    assert image1.shape == image2.shape, "Specify 2 images with the same shape."
    
    # Converte as imagens para escala de cinza
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    
    # Calcula a similaridade estrutural entre as duas imagens
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    print("Similarity of the images:", score)
    
    # Normaliza a imagem de diferença para o intervalo [0, 1]
    normalized_difference_image = (difference_image - np.min(difference_image)) / (np.max(difference_image) - np.min(difference_image))
    
    # Retorna a imagem de diferença normalizada
    return normalized_difference_image

# Função para transferir o histograma de uma imagem para outra
def transfer_histogram(image1, image2):
    # Ajusta o histograma da primeira imagem para combinar com o da segunda
    matched_image = match_histograms(image1, image2, multichannel=True)
    
    # Retorna a imagem com o histograma ajustado
    return matched_image
