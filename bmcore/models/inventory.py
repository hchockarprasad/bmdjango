from django.db import models

from django.contrib.auth.models import User

from bmcore import utils

from bmcore.models import (
    Manufacturer,
    Composition,
    Section,
    Tax,
    Therapy,
    Rack,
)


# Inventory Manager
class InventoryManager(models.Manager):

    def create(self, name, manufacturer, composition, section, tax, rack, created_by, **kwargs):

        instance = self.model()

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.alias_name = kwargs.get('alias_name', None)

        instance.manufacturer = manufacturer

        instance.composition = composition

        instance.section = section

        instance.tax = tax

        instance.rack = rack

        instance.schedule_h = kwargs.get('schedule_h', None)

        instance.schedule_h1 = kwargs.get('schedule_h1', None)

        instance.narcotic = kwargs.get('narcotic', None)

        instance.for_order = kwargs.get('for_order', None)

        instance.prohibited = kwargs.get('prohibited', None)

        instance.hide = kwargs.get('hide', None)

        instance.s_disc = kwargs.get('s_disc', None)

        instance.created_by = created_by

        instance.save()

        therapies = kwargs.get('therapy', None)

        for item in therapies:

            instance.therapy.add(item)

        return instance

    @staticmethod
    def update(inst, name, manufacturer, composition, section, tax, rack, created_by, **kwargs):

        instance = inst

        instance.name = name.upper()

        instance.val_name = utils.gen_val_str(instance.name)

        instance.alias_name = kwargs.get('alias_name', None)

        instance.manufacturer = manufacturer

        instance.composition = composition

        instance.section = section

        instance.tax = tax

        instance.rack = rack

        instance.schedule_h = kwargs.get('schedule_h', None)

        instance.schedule_h1 = kwargs.get('schedule_h1', None)

        instance.narcotic = kwargs.get('narcotic', None)

        instance.for_order = kwargs.get('for_order', None)

        instance.prohibited = kwargs.get('prohibited', None)

        instance.hide = kwargs.get('hide', None)

        instance.s_disc = kwargs.get('s_disc', None)

        instance.s_disc = kwargs.get('s_disc', None)

        instance.created_by = created_by

        instance.save()

        instance.therapy.clear()

        therapies = kwargs.get('therapy', None)

        for item in therapies:

            instance.therapy.add(item)

        return instance


# Inventory
class Inventory(models.Model):

    name = models.CharField(max_length=100)

    val_name = models.CharField(max_length=100, blank=True, null=True)

    alias_name = models.CharField(max_length=100, blank=True, null=True)

    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True)

    composition = models.ForeignKey(Composition, blank=True, null=True)

    bwd = models.BooleanField(default=True)

    section = models.ForeignKey(Section, blank=True, null=True)

    therapy = models.ManyToManyField(Therapy, blank=True)

    tax = models.ForeignKey(Tax, blank=True, null=True)

    rack = models.ForeignKey(Rack, blank=True, null=True)

    schedule_h = models.BooleanField(default=False)

    schedule_h1 = models.BooleanField(default=False)

    narcotic = models.BooleanField(default=False)

    for_order = models.BooleanField(default=True)

    prohibited = models.BooleanField(default=False)

    hide = models.BooleanField(default=False)

    min_order_lvl = models.IntegerField(default=0)

    max_order_lvl = models.IntegerField(default=0)

    re_order_lvl = models.IntegerField(default=0)

    range_order_lvl = models.IntegerField(default=0)

    s_disc = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    migration_id = models.IntegerField(blank=True, null=True)

    migration_name = models.CharField(max_length=100, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    created_by = models.ForeignKey(User, default=1)

    objects = InventoryManager()

    class Meta:
        db_table = 'tbl_inventory'
        ordering = ["-timestamp", "-updated"]

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
