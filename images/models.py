from django.db import models
from django.urls import reverse  # 168
from django.conf import settings  # 5-2
from django.utils.text import slugify  # 5-3
# Create your models here.


class Image(models.Model):  # 5-2
    """
    image model
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200,
                            blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,  # 5-4 #makemigration migration
                                        related_name='images_liked',
                                        blank=True)
    total_likes = models.PositiveBigIntegerField(db_index=True,
                                                 default=0)

    def __str__(self):  # 5-3
        return self.title

    def save(self, *args, **kwargs):
        """
        overrie this method to automatically generate
        the slug field based on the value of the title field
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
