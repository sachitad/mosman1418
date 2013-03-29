from django.db import models

from app.generic.models import Place, StandardMetadata

# Create your models here.


class Place(Place):
    place_name = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    geonames_id = models.URLField(blank=True)


class Address(StandardMetadata):
    building_name = models.CharField(max_length=250, blank=True)
    street_name = models.CharField(max_length=250, blank=True)
    street_number = models.CharField(max_length=250, blank=True)
    mosman_street = models.ForeignKey('places.MosmanStreet', null=True, blank=True)
    place = models.ForeignKey('places.Place', null=True, blank=True)

    def __unicode__(self):
        if self.mosman_street:
            street = self.mosman_street
        elif self.street_name:
            street = self.street_name
        else:
            street = None
        return '{building}{number}{street}, {place}'.format(
                            building='{}, '.format(self.building_name) if self.building_name else '',
                            number='{} '.format(self.street_number) if self.street_number else '',
                            street='{} '.format(street) if street else '',
                            place=self.place
                        )


class MosmanStreet(StandardMetadata):
    street_name = models.CharField(max_length=250, blank=True)
    bounding_box = models.CharField(max_length=250, blank=True)

    def __unicode__(self):
        return self.street_name
