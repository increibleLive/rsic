from django.db import models
from operations.utils import validateImage,validate_image_dimensions

# Create your models here.
class ImageSlider(models.Model):
    image=models.ImageField(upload_to="sliderImage/",
                            max_length=250,null=True,default=None,
                            validators=[validateImage,validate_image_dimensions])
                           
        