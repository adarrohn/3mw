from django.db import models, connection


class SiteAverageManager(models.Manager):
    def with_averages_join(self):
        """
        Computes Averages via Raw SQL
        """
        cursor = connection.cursor()
        cursor.execute("""
            SELECT _3mw_app_site.id,
            _3mw_app_site.name,
            AVG(_3mw_app_entry.val_a) AS avg_val_a,
            AVG(_3mw_app_entry.val_b) AS avg_val_b
            FROM _3mw_app_site
            LEFT OUTER JOIN _3mw_app_entry
            ON ( _3mw_app_site.id = _3mw_app_entry.site_id )
            GROUP BY _3mw_app_site.id, _3mw_app_site.name
            ORDER BY _3mw_app_site.name ASC;
        """)

        results = []
        for row in cursor.fetchall():
            site = self.model(id=row[0], name=row[1])
            site.avg_val_a = row[2]
            site.avg_val_b = row[3]
            results.append(site)
        return results

    def with_averages_python(self):
        """
        Computer Averages via Simple Query and Python
        """
        cursor = connection.cursor()
        cursor.execute("""
            SELECT name, val_a, val_b
            FROM _3mw_app_entry, _3mw_app_site
            WHERE _3mw_app_entry.site_id = _3mw_app_site.id;
        """)

        results = {}
        for row in cursor.fetchall():
            try:
                results[row[0]]['a'].append(row[1])
                results[row[0]]['b'].append(row[2])

            except KeyError:
                results[row[0]] = {'a': [row[1]],
                                   'b': [row[2]]}

        return [(key,
                 sum(results[key]['a']) / len(results[key]['a']),
                 sum(results[key]['b']) / len(results[key]['b'])) for key in sorted(results.keys())]


class Site(models.Model):
    """
    Model representation for a Site
    """
    name = models.CharField(max_length=50)

    objects = models.Manager()
    average_objects = SiteAverageManager()

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'
        ordering = ['name']

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
        ordering = ['date']

    def __str__(self):
        return 'Entry {}'.format(self.pk)
