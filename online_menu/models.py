from django.db import models

class Dish (models.Model):
    CATEGORY_CHOICES = [
        ('appetizer', 'Закуска'),
        ('main_course', 'Основное блюдо'),
        ('dessert', 'Десерт'),
        ('drink', 'Напиток'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Название блюда")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Категория")
    image_url = models.ImageField()
    
    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    sender_name = models.CharField(max_length=100, verbose_name="Имя отправителя")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Сообщение")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    def __str__(self):
        return f"Сообщение от {self.sender_name} ({self.email})"
    
    
class Order (models.Model):
    name = models.CharField(max_length=50)
    des = models.CharField (max_length=200)
    created_add = models.DateTimeField (auto_now=True)
    adres = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    
    

    

