import urllib2
import json
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.db import IntegrityError
from django.conf import settings
from events.models import Event, Guest
from events.forms import GuestForm
from base.models import Person
from base.forms import PersonForm


class EventList(ListView):
    """
    """
    queryset = Event.objects.filter(is_active=True)
    template_name = 'event_list.html'


def home(request):
    """
    """
    event = Event.objects.all()[0]

    return HttpResponseRedirect(reverse_lazy(
        event_detail,
        kwargs={
            'slug': event.slug,
        },
        current_app='events')
    )


def event_detail(request, slug=None, data=None):
    """
    """
    event = get_object_or_404(Event, slug=slug)

    if request.method == 'POST':
        data = request.POST

    if data is not None or request.method == 'POST':
        person_form = PersonForm(data=data, prefix="person")
        guest_form = GuestForm(data=data, prefix="guest")

        print person_form.errors

        if person_form.is_valid():
            # save person
            person = person_form.save(commit=False)
            person_data = person_form.cleaned_data

            person = Person.objects.filter(email=person_data['email'])

            if person.exists():
                person = person[0]

                # keep this object in case something goes wrong
                # when saving the registration
                original_person = person

                # update student data from form
                person.name = person_data['name']
            else:
                person = Person(**person_data)

            person.save()

            if guest_form.is_valid():

                # save guest
                guest_data = guest_form.cleaned_data

                guest = Guest(
                    person=person,
                    event=event,
                    proposal=guest_data['proposal'],
                    affiliation=guest_data['affiliation']
                )

                # try saving the guest.
                # this may fail because of the unique_together db constraint
                # an IntegrityError will occur
                try:
                    guest.save()
                    return HttpResponse(
                        serializers.serialize('json', [person, ]))

                # in case saving the guest failed
                # (see proposal above the try block),
                # add an error to the guest form
                except IntegrityError:

                    # restore data
                    person.name = original_person.name
                    person.save()

                    # display error
                    guest_form._errors['errors'] = \
                        guest_form.error_class(
                            ["Looks like you've already confirmed your attendance to this event", ])

                    return HttpResponse(json.dumps(
                        guest_form.errors))

    else:
        guest_form = GuestForm(prefix="guest")
        person_form = PersonForm(prefix="person")

    proposals = event.guest_set.filter(proposal__gt=0)

    facebook_url = 'https://graph.facebook.com/v2.1/%s/attending?access_token=%s' % (event.facebook_id, settings.FACEBOOK_ACCESS_TOKEN)
    facebook_event = urllib2.urlopen(facebook_url)
    attendees_list = facebook_event.read()
    facebook_attendees = json.loads(attendees_list)

    title_guest_names = []
    guest_names = event.guest_set.all().values_list('person__name', flat=True)
    for name in guest_names:
        title_guest_names.append(name.title())

    return render_to_response('event_detail.html', {
        'event': event,
        'proposals': proposals,
        'guest_names': title_guest_names,
        'facebook_attendees': facebook_attendees['data'],
        'person_form': person_form,
        'guest_form': guest_form,
    }, context_instance=RequestContext(request))
