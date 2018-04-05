from django.db import models
from django.utils.safestring import mark_safe 

# Create your models here.
class Query(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)
  query_content = models.CharField(max_length=100000, null=False, blank=False)

  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
      # ecocase ID has to be unique (should probably make it a primary key)
    self.query_content = mark_safe(self.query_content)
    super(Query, self).save(*args, **kwargs)