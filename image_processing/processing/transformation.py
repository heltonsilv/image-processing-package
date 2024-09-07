from skimage.transform import resize

# Função para redimensionar uma imagem com base em uma proporção
def resize_image(image, proportion):
    # Verifica se a proporção está entre 0 e 1
    assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1."
    
    # Calcula a nova altura e largura da imagem com base na proporção fornecida
    height = round(image.shape[0] * proportion)
    width = round(image.shape[1] * proportion)
    
    # Redimensiona a imagem usando a função resize do skimage, com anti-aliasing para melhorar a qualidade
    image_resized = resize(image, (height, width), anti_aliasing=True)
    
    # Retorna a imagem redimensionada
    return image_resized
