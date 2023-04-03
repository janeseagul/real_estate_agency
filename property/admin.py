from django.contrib import admin

from .models import Flat, Complaint, Owner


class Flat_owned_by(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
    )
    list_editable = ['new_building']
    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony'
    )
    raw_id_fields = ('liked_by',)
    inlines = [Flat_owned_by]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)
    search_fields = ['flat_owner']
    inlines = [Flat_owned_by]

