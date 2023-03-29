from django.db import models
from django.urls import reverse
from django.utils.text import slugify#імпортуємо slugify
# Create your models here.

# тут додав модель і поля до неї
class Movie(models.Model): 
	name = models.CharField(max_length=40)
	rating = models.IntegerField()
	year = models.IntegerField(null=True)
	budget = models.IntegerField(default=1000000)
	slug = models.SlugField(default='', null=False)

    # додав тип slug для зрозумілішого відображення данних з бд
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Movie, self).save(*args, **kwargs)

	def get_url(self):
		return reverse('movie-datail', args=[self.slug])
    
    # додав магічний метод __str__ для кращого відображення данних з бд
	def __str__(self):
		return f'Це {self.name} - {self.rating}%'
