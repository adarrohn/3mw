from django.db import models


class Site(models.Model):
    """
    Model representation for a Site
    """
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'
        ordering = ['-name']

    def __str__(self):
        return 'Site {}'.format(self.name)


class Entry(models.Model):
    """
    Model representation for a single Site Entry
    """
    site = models.ForeignKey(Site)
    date = models.DateField()
    val_a = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='Value A')
    val_b = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='Value B')

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'
        ordering = ['-date']

    def __str__(self):
        return 'Entry {}'.format(self.pk)