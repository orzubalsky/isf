from django.db.models import *
from django.utils import timezone
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField


class Base(Model):
    """
    Base model for all of the models in the application.
    """
    class Meta:
        abstract = True

    created = DateTimeField(editable=False)
    updated = DateTimeField(editable=False)
    is_active = BooleanField(default=True)

    def save(self, *args, **kwargs):
        """
        Save timezone-aware values for created and updated fields.
        """

        self.created = timezone.now()
        self.updated = timezone.now()
        super(Base, self).save(*args, **kwargs)

    def __unicode__(self):
        if hasattr(self, "name") and self.name:
            return self.name
        else:
            return "%s" % (type(self))


class Person(Base):
    """
    """
    class Meta:
        verbose_name_plural = "People"
        ordering = ['name', ]

    name = CharField(max_length=140)
    email = EmailField()


class Image(Base):
    name = CharField(max_length=140, null=True, blank=True)
    media = FileBrowseField("Image", max_length=200, directory="images/")


class Document(Base):
    name = CharField(max_length=140, null=True, blank=True)
    media = FileBrowseField("PDF", max_length=200, directory="documents/")


class Sound(Base):
    name = CharField(max_length=140, null=True, blank=True)
    media = FileBrowseField("Audio", max_length=200, directory="sounds/")


class Video(Base):
    name = CharField(max_length=140, null=True, blank=True)
    media = FileBrowseField("Video", max_length=200, directory="video/")


class Vimeo(Base):
    name = CharField(max_length=140, null=True, blank=True)
    media = TextField()


class ContentManager(Manager):
    def get_queryset(self):
        return super(ContentManager, self).get_queryset().prefetch_related(
            'images',
            'sounds',
            'videos',
            'vimeos',
            'documents'
        )


class Content(Base):
    """
    """
    class Meta:
        abstract = True

    name = CharField(max_length=140)
    content = HTMLField(null=True, blank=True)
    slug = SlugField(max_length=160)
    images = ManyToManyField(Image, blank=True, null=True)
    sounds = ManyToManyField(Sound, blank=True, null=True)
    videos = ManyToManyField(Video, blank=True, null=True)
    vimeos = ManyToManyField(Vimeo, blank=True, null=True)
    documents = ManyToManyField(Document, blank=True, null=True)
    objects = ContentManager()

    def media():
        def fget(self):
            return {'images': self.images,
                    'sounds': self.sounds,
                    'videos': self.videos,
                    'vimeos': self.vimeos,
                    'documents': self.documents,
                    }
        return locals()

    media = property(**media())

    def gallery_items(self):
        items = []
        for item_dictionary in self.media.values():
            if item_dictionary.count() > 0:
                for item in item_dictionary.all():
                    items.append(item)
        return items

    def gallery_items_count(self):
        return len(self.gallery_items())
