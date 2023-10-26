#Importing framework |Remember to install in console: "pip install Pillow" (Importando FrameWork|Lembre - se de instalar o console: "pip install Pillow")
from PIL import Image
#------------------------------------------------------------------------------------------------
#Image way|Remember to change the way to your machine (Caminho da Imagem|Lembrar de mudar o caminho dentro da sua máquina)
way = "C:\Users\BeaKalbF\way.jpg"
img = Image.open(way)
#------------------------------------------------------------------------------------------------
#Image data (Dados da Imagem)
matrix = img.getdata()
#------------------------------------------------------------------------------------------------
#Image size (Tamanho da Imagem)
width, height = img.size
#------------------------------------------------------------------------------------------------
#New image based on the original (Criação de uma nova Imagem utlizando os dados da Imagem anterior)
average_img = Image.new('L', (width, height)) 
#------------------------------------------------------------------------------------------------
#Analyzing image pixels (Análise dos pixels da Imagem)
for h in range(height):
    for w in range(width):
        
        # Average image pixels
        # Média de pixels da Imagem
        r, g, b = img.getpixel((w, h))
        average_pixel = (r + g + b) // 3
        average_img.putpixel((w, h), average_pixel)
#------------------------------------------------------------------------------------------------
#Image saved (Salva a Imagem em Tons de Cinza)
average_img.save("gray_img.jpg")

#Show image (Mostrando Imagem)
average_img.show()