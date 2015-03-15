from django.views.generic import ListView, DetailView
from .models import Site

class SitesList(ListView):
    """

    """
    model = Site


class SitesDetail(DetailView):
    """

    """
    model = Site


class SummaryList(ListView):
    """

    """
    model = Site


class SummaryListAverage(ListView):
    """

    """
    model = Site
