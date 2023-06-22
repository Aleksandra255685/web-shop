from django.db import models
from django.urls import reverse


class Product(models.Model):
    CAKE = 'cake'
    PASTRY = 'pastry'
    CANDY_BAR = 'candy-bar'
    CHOICE_GROUP = {
        (CAKE, 'cake'),
        (PASTRY, 'pastry'),
        (CANDY_BAR, 'candy-bar'),
    }

    objects = None
    name = models.CharField('Название', max_length=100)
    filling = models.CharField('Начинка', max_length=100)
    composition = models.TextField('Состав')
    cost = models.DecimalField('Цена', max_digits=20, decimal_places=2, blank=True, null=True)
    category = models.CharField('Категория', max_length=20, choices=CHOICE_GROUP, default=CAKE)
    image = models.ImageField('Изображение', upload_to='cakes/', default='default.jpg')
    url = models.SlugField(max_length=130, unique=True)

    def get_absolute_url(self):
        return reverse('product_view', kwargs={"slug": self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
