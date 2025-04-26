from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class CategoryInfo(models.Model):
    categoryName= models.CharField(max_length=70)
    slug= AutoSlugField(populate_from='categoryName',unique=True,null=True,default=None)

    def __str__(self):
        return f'{self.categoryName}'
    
    