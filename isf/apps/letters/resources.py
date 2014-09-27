from import_export import resources, fields
from letters.models import Signature


class SignatureResource(resources.ModelResource):

    person = fields.Field()

    class Meta:
        model = Signature
        fields = ('id', 'letter', 'comment')

    def dehydrate_letter(self, signature):
        print self

    def dehydrate_person(self, signature):
        print self
