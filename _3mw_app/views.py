from django.views.generic import ListView, DetailView
from .models import Site

class SitesList(ListView):
    """

    """
    model = Site
    template_name = 'sites_list.html'

class SitesDetail(DetailView):
    """

    """
    model = Site
    template_name = 'sites_detail.html'


class SummaryList(ListView):
    """

    """
    model = Site
    template_name = 'summary_list.html'


class SummaryListAverage(ListView):
    """

    """
    model = Site
    template_name = 'summary_avg_list.html'
