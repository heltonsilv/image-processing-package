from skimage.io import imread, imsave

# Função para ler uma imagem a partir de um caminho especificado
def read_image(path, is_gray=False):
    # Lê a imagem do caminho fornecido
    # Se is_gray for True, a imagem será convertida para escala de cinza
    image = imread(path, as_gray=is_gray)
    
    # Retorna a imagem lida
    return image

# Função para salvar uma imagem em um caminho especificado
def save_image(image, path):
    # Salva a imagem no caminho fornecido
    imsave(path, image)
