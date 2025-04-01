from PIL import Image


image_path = 'path_to_your_image.jpg'  
image = Image.open(image_path)


width, height = image.size


aspect_ratio = width / height


print(f"Width: {width}")
print(f"Height: {height}")
print(f"Aspect Ratio: {aspect_ratio}")
