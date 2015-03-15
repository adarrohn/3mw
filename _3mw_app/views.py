from django.views.generic import ListView, DetailView
from .models import Site


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

    def get_queryset(self):
        return Site.objects.order_by('name').all()


class SitesDetail(SiteMixin, DetailView):
    """
    Shows a Single Site in a Detail View
    """
    template_name = 'sites_detail.html'
    context_object_name = 'site'


class SummaryListSum(SiteMixin, ListView):
    """

    """
    template_name = 'summary_list.html'


class SummaryListAverage(SiteMixin, ListView):
    """

    """
    template_name = 'summary_avg_list.html'
