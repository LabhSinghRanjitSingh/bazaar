from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
Image_Folder="bazaar/"

class Book(models.Model):
    # TODO: Define fields here
    name = models.CharField(blank=True, max_length=100)
    brand = models.ManyToManyField('Brand')
    cover = models.ImageField(upload_to=Image_Folder)
    description = models.CharField(blank=True, max_length=500)
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def image_tag(self):
        #--hkcheck--flag .. "" use var
        return mark_safe('<img src="/images/%s" width="100px" height="100px"/>' % self.cover)

    def __unicode__(self):
        pass

    def __str__(self):
        return self.name


class Brand(models.Model):
    # TODO: Define fields here
    name = models.CharField(blank=True, max_length=100)
    logo = models.ImageField(upload_to=Image_Folder)
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __unicode__(self):
        pass

    def __str__(self):
        return self.name

class Piece(models.Model):
    # TODO: Define fields here
    name = models.CharField(blank=True, max_length=100)
    clothType = models.ForeignKey('ClothType', on_delete=models.CASCADE)
    description = models.CharField(blank=True, max_length=500)
    book = models.ForeignKey('Book',on_delete=models.CASCADE,related_name='pieces')
    cover = models.ImageField(upload_to=Image_Folder) 
    class Meta:
        verbose_name = 'Piece'
        verbose_name_plural = 'Pieces'

    def __unicode__(self):
        pass

    def __str__(self):
        return self.name


class PieceImage(models.Model):
    # TODO: Define fields here
    image = models.ImageField(upload_to=Image_Folder)
    piece = models.ForeignKey('Piece', on_delete=models.CASCADE,related_name='images')
    class Meta:
        verbose_name = 'PieceImage'
        verbose_name_plural = 'PieceImages'

    def __unicode__(self):
        pass

    def image_tag(self):
        #--hkcheck--flag .. "" use var
        return mark_safe('<img src="/images/%s" width="100px" height="100px"/>' % self.image)


class ClothType(models.Model):
    # TODO: Define fields here
    name = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=True, max_length=500)
    class Meta:
        verbose_name = 'ClothType'
        verbose_name_plural = 'ClothTypes'

    def __unicode__(self):
        pass

    def __str__(self):
        return self.name
