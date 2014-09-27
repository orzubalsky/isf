from django.db.models import *
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from base.models import Base, Person


class Event(Base):
    """
    """
    class Meta:
        ordering = ['-created', ]

    title = CharField(max_length=255)
    slug = SlugField(max_length=160)
    description = HTMLField()
    start_date = DateTimeField()
    end_date = DateTimeField()
    hosted_by = CharField(max_length=255, blank=True, null=True)
    street_address = CharField(max_length=255, blank=True, null=True)
    city = CharField(max_length=64, blank=True, null=True)
    state = CharField(max_length=64, blank=True, null=True)
    zip_code = CharField(max_length=10, blank=True, null=True)
    telephone = CharField(max_length=20, blank=True, null=True)
    latitude = FloatField(blank=True, null=True)
    longitude = FloatField(blank=True, null=True)
    guests = ManyToManyField(
        Person,
        through="Guest",
        blank=True,
        null=True
    )
    related_letters = ManyToManyField("letters.Letter", blank=True, null=True)
    related_events = ManyToManyField("self", blank=True, null=True)
    color = CharField(max_length=22, default='#000000')
    do_color_inverse = BooleanField(default=True)
    do_get_guests = BooleanField(default=False)
    do_show_guests = BooleanField(default=False)
    do_show_proposals = BooleanField(default=False)
    facebook_id = CharField(max_length=100, blank=True, null=True)
    tags = TaggableManager(blank=True)

    def tag_list(self):
        return " ".join(["%s" % (t.name) for t in self.tags.all()])

    def __unicode__(self):
        return u"%s" % self.title


class Guest(Base):
    """
    """
    class Meta:
        unique_together = ('person', 'event')

    ATTENDING_CHOICES = (
        ('yes', 'Yes'),
        ('no', 'No'),
        ('maybe', 'Maybe'),
        ('no_rsvp', 'Hasn\'t RSVPed yet')
    )

    person = ForeignKey(Person)
    affiliation = CharField(
        max_length=160,
        blank=True,
        null=True,
        verbose_name="Group or organization",
        help_text="Are you in a group or organization "
        "that you think will interest others? (optional)"
    )
    event = ForeignKey(Event)
    proposal = TextField(
        blank=True,
        null=True,
        help_text="What would you like to talk about "
        "or work on in this event? (optional)"
    )
    comment = TextField(blank=True, null=True)
    is_public = BooleanField(default=False)
    attending_status = CharField(
        max_length=32,
        choices=ATTENDING_CHOICES,
        default='no_rsvp'
    )

    def __unicode__(self):
        return u"%s" % self.person.name
