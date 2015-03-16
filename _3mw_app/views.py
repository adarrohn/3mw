from django.views.generic import ListView
from django.db.models import Sum, Avg

from .models import Site, Entry


class SitesList(ListView):
    """
    Shows All Sites as a List View
    """
    model = Site
    context_object_name = 'sites'
    template_name = 'sites_list.html'


class SitesDetail(ListView):
    """
    Shows a Single Site in a List View Containing Foreign Entries
    """
    context_object_name = 'entries'
    template_name = 'sites_detail.html'

    def get_queryset(self):
        return Entry.objects.filter(site=self.kwargs['id'])


class SummaryListSum(ListView):
    """
    Shows an Aggregated Sum of A And B Values From Each Site
    """
    template_name = 'summary_sum_list.html'
    context_object_name = 'sites'

    def get_queryset(self):
        return Site.objects.all().annotate(sum_val_a=Sum('entry__val_a'),
                                           sum_val_b=Sum('entry__val_b'))


class SummaryListAverage(ListView):
    """
    Shows an Average of A and B Values From Each Site
    """
    template_name = 'summary_avg_list.html'
    context_object_name = 'sites'

    def get_queryset(self):
        return Site.average_objects.with_averages_join()
