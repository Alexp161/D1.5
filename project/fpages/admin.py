from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as OriginalFlatPageAdmin
from django.utils.translation import gettext_lazy as _


class CustomFlatPageAdmin(OriginalFlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Additional Options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)
