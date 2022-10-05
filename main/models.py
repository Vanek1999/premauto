from django.db import models


class Oil(models.Model):
	product_title = models.CharField('Название продукта', max_length = 200)
	product_description = models.TextField('Описание')
	product_price = models.CharField('Цена', max_length = 200, null=True)
	photo = models.ImageField(upload_to='main/static/img/product/', null=True, blank=True)

	def __str__(self):
		return self.product_title

	class Meta:
		verbose_name = 'Масло'
		verbose_name_plural = 'Масла'

class Spares(models.Model):
	product_title = models.CharField('Название продукта', max_length = 200)
	product_description = models.TextField('Описание')
	product_price = models.CharField('Цена', max_length = 200, null=True)
	photo = models.ImageField(upload_to='main/static/img/product/', null=True, blank=True)

	def __str__(self):
		return self.product_title

	class Meta:
		verbose_name = 'Запчасти'
		verbose_name_plural = 'Запчасти'

class Autochemistry(models.Model):
	product_title = models.CharField('Название продукта', max_length = 200)
	product_description = models.TextField('Описание')
	product_price = models.CharField('Цена', max_length = 200, null=True)
	photo = models.ImageField(upload_to='main/static/img/product/', null=True, blank=True)

	def __str__(self):
		return self.product_title

	class Meta:
		verbose_name = 'Автохимия'
		verbose_name_plural = 'Автохимия'

class Users(models.Model):
	password = models.CharField(max_length = 30)
	number = models.CharField(max_length = 15)
	name = models.CharField(max_length = 10)
	ip = models.CharField(max_length = 20, null = True)
	cart = models.CharField(max_length = 200, null = True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Клиенты'
		verbose_name_plural = 'Клиенты'

