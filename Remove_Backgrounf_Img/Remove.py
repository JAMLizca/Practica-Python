from rembg import remove
from PIL import Image
input_path = 'leo.jpg'
output_path = 'leo.png'
input_image = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Img.open("leo.png")

#no funciona :Vpython3 -m venv myenv
