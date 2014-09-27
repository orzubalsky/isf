from import_export import resources
from base.models import Person


class PersonResource(resources.ModelResource):

    class Meta:
        model = Person
        fields = ('id', 'name', 'email')
