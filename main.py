from rembg import remove
from PIL import Image

input_path = 'СВЕТЛАНА.jpg'
output_path = 'out_СВЕТЛАНА.png'

open_image = Image.open(input_path)
output = remove(open_image)

output.save(output_path)
