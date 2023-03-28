from django.contrib import admin
from .models import scholarship,application_table,session_table
from import_export.admin import  ImportExportModelAdmin
from django.contrib.auth.models import  User
#from .models import application_table
from django import forms
from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils.translation import ngettext

# Register your models here.
admin.site.register(scholarship)
admin.site.register(application_table)
admin.site.register(session_table)


admin.site.unregister(User)
admin.site.unregister(application_table)

        #return render(request, 'admin/m

def approve_bursary(self,request,queryset):
    queryset.update(status=3)

#
# def change_field_value(modeladmin, request, queryset):
#     form = ChangeFieldValueForm(request.POST)
#     if form.is_valid():
#         new_value = form.cleaned_data['new_value']
#         queryset.update(application_table.amnt_applied_for==new_value)
# change_field_value.short_description = "Change field value"
#
#
# def custom_action(self, request, queryset):
#     #form = CustomActionForm(request.POST)
#     new_value = request.POST.get('new_value')
#     queryset.update(school_name=new_value)
#
#
#     #all_fields_retriever = application_table.objects.get(all)
#     # old_status = application_table.status
#
#     if form.is_valid():
#         new_value = form.cleaned_data['new_value']
#         queryset.update(status==new_value)
#         for new_value in new_value:
#             new_value.save()
#         #for obj in status:
#         #    obj.save()
#         self.message_user(request, f"{len(queryset)} objects updated.")
#     return render(request, 'admin/custom_action.html', {'form': form, 'queryset': queryset})
        # return HttpResponseRedirect(request.get_full_path())
    # else:
    #     messages.error(request,_('please fix error'))
    #     return render(request, 'admin/custom_action.html', {'form': form, 'queryset': queryset})


    # form = UpdateFieldWithCustomValueForm(request.POST)
    # if form.is_valid():
    #     custom_value = form.cleaned_data['custom_value']
    #     for obj in queryset:
    #         obj.school_name = custom_value
    #         obj.save()
    #         self.message_user(request, f"Updated school name with value {custom_value} for selected objects.")
    #     return render(request, 'admin/custom_action.html', {'form': form, 'queryset': queryset})
    #
    #
    #
    # else:
    #
    #     self.message_user(request, "Invalid custom value input.")

    # custom_input = request.POST.get('custom_input')  # Get the custom input value from the POST data
    #
    # # Update the field with the custom input value
    # obj = queryset.update(school_name=custom_input)
    #
    # # Display a success message to the user
    # message = ngettext(
    #     '%(count)d object was updated.',
    #     '%(count)d objects were updated.',
    #     obj,
    # ) % {'count': obj}
    # messages.success(request, message)

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('username','email','first_name','is_staff',)
    list_filter = ('first_name',)


@admin.register(application_table)
class ApplicationtableAdmin(ImportExportModelAdmin):

    list_display = ('scholarship_id','user_id','status','school_name','amnt_applied_for','allocated_amnt')
    list_filter = ('status',)
    def update_field_with_custom_input(modeladmin, request, queryset):
        if request.method == 'POST':
            form = UpdateFieldWithCustomValueForm(request.POST)
            if form.is_valid():
                custom_input = form.cleaned_data['custom_input']
                for obj in queryset:
                    obj.allocated_amnt = custom_input
                    obj.save()
                self.message_user(request, f"{len(queryset)} objects updated.")# Return None to indicate success

        else:
            form = UpdateFieldWithCustomValueForm()

        context = {
            'form': form,
            'queryset': queryset,
        }
        return render(request, 'admin/custom_action.html', context)

    # def update_field_with_custom_value(self, request, queryset):
    #
    #     if form.is_valid(request.method == 'POST'):
    #         custom_value = form.cleaned_data['custom_value']
    #         queryset = application_table.objects.get()
    #         for obj in queryset:
    #             obj.school_name = custom_value
    #             obj.save()
    #
    #     #self.message_user(request, f"Updated custom field with value {custom_value} for selected objects.")
    #     else:
    #         self.message_user(request, "Invalid custom value input.")
    #         context = {
    #             'queryset': queryset,
    #             'form': form
    #         }
    #     return render(request, 'admin/custom_action.html')



    actions = [approve_bursary, update_field_with_custom_input]

    #
    #
    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions
    #
    #
    #
    # def get_form(self, request, obj=None, **kwargs):
    #     if obj is not None:
    #         self.form = UpdateFieldWithCustomValueForm
    #     return super().get_form(request, obj, **kwargs)
    #




class UpdateFieldWithCustomValueForm(forms.Form):

    custom_input = forms.CharField(max_length=20)
    # class Meta:
    #     model = application_table
    #     fields = "__all__"
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['custom_input'] = forms.CharField()

    #status = forms.IntegerField(label="status")
