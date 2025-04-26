
from django.core.exceptions import ValidationError
from PIL import Image

def validateImage(value):
    """
    Validate that the uploaded image is a JPEG.
    """
    # Check the file's content type
    # if not value.file.content_type in ['image/jpeg', 'image/jpg']:
    #     raise ValidationError('Only JPEG images are allowed.')

    # Optionally, you can also check the file extension if needed
    file_extension = value.name.split('.')[-1].lower()
    if file_extension not in ['jpg', 'jpeg','png']:
        raise ValidationError('Only JPEG or PNG images are allowed.')
    

def validate_image_dimensions(value):
    """
    Validate that the uploaded image has dimensions 1920x500.
    """
    # Open the image using PIL (Python Imaging Library)
    img = Image.open(value)
    
    # Get the dimensions of the image
    width, height = img.size
    
    # Check if the dimensions are not as required
    if width != 1920 or height != 500:
        raise ValidationError('Image dimensions must be 1920x500 pixels.')
    

def validate_Square_image(value):
    
    img = Image.open(value)
    
    # Get the dimensions of the image
    width, height = img.size
    
    # Check if the dimensions are not as required
    if width != height:
        raise ValidationError('Please upload a square image.')

