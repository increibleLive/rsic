from django.db import models
from categories.models import CategoryInfo
from operations.utils import validateImage,validate_Square_image
# Create your models here.
class ProductInfo(models.Model):
    category=models.ForeignKey(CategoryInfo, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    photo= models.ImageField(upload_to="productImage/",
                            max_length=250,null=True,default=None,
                            validators=[validateImage,validate_Square_image])
    
    