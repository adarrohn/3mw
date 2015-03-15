from django.db import models


class Site(models.Model):
    """
    Model representation for a Site
    """
    name = models.CharField(max_length=50)
    date = models.DateField()
    val_a = models.DecimalField()
    val_b = models.DecimalField()

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'
        ordering = ['-Name']

    def __str__(self):
        return 'Site {}'.format(self.name)