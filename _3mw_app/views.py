from django.views.generic import ListView, DetailView
from .models import Site, Entry


class SiteMixin(object):
    """
    Mixin for all Site Model Views
    """
    model = Site
    context_object_name = 'sites'


class SitesList(SiteMixin, ListView):
    """
    Shows All Sites as a List View
    """
    template_name = 'sites_list.html'


class SitesDetail(ListView):
    """
    Shows a Single Site in a List View Containing Foreign Entries
    """
    template_name = 'sites_detail.html'
    context_object_name = 'entries'

    def get_queryset(self):
        return Entry.objects.filter(site=self.kwargs['id'])


class SummaryListSum(SiteMixin, ListView):
    """

    """
    template_name = 'summary_list.html'


class SummaryListAverage(SiteMixin, ListView):
    """

    """
    template_name = 'summary_avg_list.html'
