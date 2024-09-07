import matplotlib.pyplot as plt

# Função para plotar uma imagem
def plot_image(image):
    # Cria uma figura com tamanho especificado
    plt.figure(figsize=(12, 4))
    
    # Exibe a imagem em escala de cinza
    plt.imshow(image, cmap='gray')
    
    # Remove os eixos
    plt.axis('off')
    
    # Mostra a imagem plotada
    plt.show()

# Função para plotar múltiplas imagens lado a lado
def plot_result(*args):
    # Obtém o número de imagens a serem plotadas
    number_images = len(args)
    
    # Cria uma figura com subplots em uma única linha
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12, 4))
    
    # Cria uma lista de nomes para as imagens
    names_lst = ['Image {}'.format(i) for i in range(1, number_images)]
    names_lst.append('Result')
    
    # Itera sobre os eixos, nomes e imagens para plotar cada uma
    for ax, name, image in zip(axis, names_lst, args):
        ax.set_title(name)  # Define o título do subplot
        ax.imshow(image, cmap='gray')  # Exibe a imagem em escala de cinza
        ax.axis('off')  # Remove os eixos
    
    # Ajusta o layout da figura para evitar sobreposição
    fig.tight_layout()
    
    # Mostra a figura plotada
    plt.show()

# Função para plotar histogramas de uma imagem
def plot_histogram(image):
    # Cria uma figura com 3 subplots compartilhando eixos x e y
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    
    # Lista de cores para os canais de cor
    color_lst = ['red', 'green', 'blue']
    
    # Itera sobre os eixos, índices e cores para plotar cada histograma
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title('{} histogram'.format(color.title()))  # Define o título do subplot
        ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)  # Plota o histograma do canal de cor
    
    # Ajusta o layout da figura para evitar sobreposição
    fig.tight_layout()
    
    # Mostra a figura plotada
    plt.show()
