from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify

# pip install Pillow : imagefield için
# editable=False : id'ninn değiştirilme özellliğini kapatır.İd değiştirilemez. 

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Kullanıcı')
    isim = models.CharField(max_length=100)
    resim = models.ImageField(upload_to = 'profiller/')
    olusturulma_tarihi = models.DateField(auto_now_add=True, null=True)
    slug = models.SlugField(null=True, editable=False)

    def __str__(self):
        return self.isim
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)

class Hesap(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resim = models.ImageField(upload_to='hesap/')
    telefon = models.IntegerField()
    sifre = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.user.username