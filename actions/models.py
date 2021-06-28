from django.db import models
from django.contrib.contenttypes.models import ContentType  # 201
from django.contrib.contenttypes.fields import GenericForeignKey  # 201

# Create your models here.


class Action(models.Model):

    user = models.ForeignKey('auth.User',
                             related_name='actions',
                             db_index=True,
                             on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType,
                                  blank=True,
                                  null=True,
                                  related_name='target_obj',
                                  on_delete=models.CASCADE)
    target_id = models.PositiveBigIntegerField(null=True,
                                               blank=True,
                                               db_index=True)
    target = GenericForeignKey('target_ct', 'target_id')
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    class Meta:
        ordering = ('-created',)
