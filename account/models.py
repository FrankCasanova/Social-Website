from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    """
    That class extend the User funtionalities
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True,
                                     null=True)
    photo = models.ImageField(upload_to='users/%y/%m/%d',
                              blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'
