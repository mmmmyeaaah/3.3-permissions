import django_filters
from django_filters import rest_framework as filters

from adv.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']