from PIL import Image, ImageFilter, ImageEnhance

def open_image(filepath):
    """Open an image file."""
    return Image.open(filepath)

def apply_blur(image, radius=5):
    """Apply a Gaussian Blur filter to an image."""
    return image.filter(ImageFilter.GaussianBlur(radius))

def enhance_contrast(image, factor=1.5):
    """Enhance the contrast of an image."""
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def save_image(image, filepath):
    """Save an image to a file."""
    image.save(filepath)

def main():
    input_path = 'input_image.jpg'

  
    img = open_image(input_path)

    blurred_img = apply_blur(img, radius=10)

    
    enhanced_img = enhance_contrast(blurred_img, factor=1.8)


    output_path = 'output_image.jpg'
    save_image(enhanced_img, output_path)

    print(f"Processed image saved as: {output_path}")

if __name__ == '__main__':
    main()
