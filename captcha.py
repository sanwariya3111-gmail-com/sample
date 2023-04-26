from captcha.image import ImageCaptcha
import random

# Generate a random string of given length
def generate_random_string(length):
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Generate a CAPTCHA image and return the image data and the answer string
def generate_captcha():
    captcha_string = generate_random_string(6)  # Change the length of the CAPTCHA string here
    image = ImageCaptcha()
    captcha_image = image.generate(captcha_string)
    captcha_image_data = image.generate_image(captcha_string)
    return captcha_image, captcha_string

# Example usage
captcha_image, captcha_string = generate_captcha()
captcha_image.save('captcha.png')  # Save the captcha image to a file
print("Captcha string:", captcha_string)

