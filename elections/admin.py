
from django.contrib import admin
from elections.models import Election, Candidate, PersonalData
from popolo.models import Organization, Membership, ContactDetail, OtherName, Post, Area
from django.contrib.contenttypes.admin import GenericTabularInline
# from django.contrib.flatpages.admin import FlatPageAdmin
# from django.contrib.flatpages.models import FlatPage
## OOPS this is a custom widget that works for initializing
## tinymce instances on stacked and tabular inlines
## for flatpages, just use the tinymce packaged one.
#from content.widgets import TinyMCE
# from tinymce.widgets import TinyMCE


class ElectionAdmin(admin.ModelAdmin):
    search_fields = ['name', 'tags']


admin.site.register(Election, ElectionAdmin)


class OrgnizationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Organization, OrgnizationAdmin)


class ContactDetailInline(GenericTabularInline):
    model = ContactDetail
    fields = ('label', 'contact_type', 'value')


class MembershipInline(admin.TabularInline):
    model = Membership
    fields = ('label', 'role', 'organization', 'on_behalf_of', 'post', 'start_date', 'end_date', 'area')


class OtherNameInline(GenericTabularInline):
    model = OtherName


class PersonalDataInline(admin.TabularInline):
    model = PersonalData


class CandidateAdmin(admin.ModelAdmin):
    inlines = [
        ContactDetailInline,
        MembershipInline,
        OtherNameInline,
        PersonalDataInline,
    ]
admin.site.register(Candidate, CandidateAdmin)


class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)


class AreaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Area, AreaAdmin)
# class PageForm(FlatpageForm):
#     class Meta:
#         model = FlatPage
#         widgets = {
#             'content': TinyMCE(),
#         }


# class PageAdmin(FlatPageAdmin):
#     """
#     Page Admin
#     """
#     form = PageForm

# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, PageAdmin)
