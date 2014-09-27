from django.db.models import *
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from base.models import Base, Person


class Letter(Base):
    """
    """
    class Meta:
        ordering = ['-created', ]

    title = CharField(max_length=255)
    slug = SlugField(max_length=160)
    body = HTMLField()
    date_published = DateTimeField()
    signatures = ManyToManyField(
        Person,
        through="Signature",
        blank=True,
        null=True
    )
    related_letters = ManyToManyField("self", blank=True, null=True)
    related_events = ManyToManyField("events.Event", blank=True, null=True)    
    color = CharField(max_length=22, default='#000000')
    do_color_inverse = BooleanField(default=True)
    do_get_signatures = BooleanField(default=False)
    do_show_signatures = BooleanField(default=False)
    tags = TaggableManager(blank=True)

    def tag_list(self):
        return " ".join(["%s" % (t.name) for t in self.tags.all()])

    def __unicode__(self):
        return u"%s" % self.title


class Signature(Base):
    """
    """
    class Meta:
        unique_together = ('person', 'letter')

    person = ForeignKey(Person)
    letter = ForeignKey(Letter)
    comment = TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.person.name
