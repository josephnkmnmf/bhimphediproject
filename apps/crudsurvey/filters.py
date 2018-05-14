import django_filters
from apps.crudsurvey.models import Surve


class SurveFilter(django_filters.FilterSet):
    class Meta:
        model = Surve
        fields = ['ref_no', 'house_owner', 'phone_no', ]
