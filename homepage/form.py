

from django.forms import ModelForm
from .models import  scholarship,application_table
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

RANK_COHICES = (
    ('Lance Naik','Lance Naik'),
    ('Naik','Naik'),
    ('Hawaldar','Hawaldar'),
    ('Nb Subedar','Nb Subedar'),
    ('Subedar','Subedar'),
    ('Subeder Maj','Subeder Maj'),
    ('Officer','Officer'),
)
present_year = (
    ('FE','FE'),
    ('SE','SE'),
    ('TE','TE'),
    ('BE','BE'),

)

sibling_school = (
    ('secondary','Secondary'),
    ('college','College'),
    ('university','University'),


)

study_mode = (
    ('REGULAR','regular'),
    ('PARALLEL','parallel'),
    ('BOARDING','boarding'),
    ('DAY','day'),

)
guardian_mode = (
    ('PERMANENT','permanent'),
    ('CONTRACTUAL','contractual'),
    ('CASUAL','casual'),
    ('RETIRED','retired'),
    ('SELF_EMPLOYED','self_employed'),
    ('NONE','none'),

)

mother_mode = (
    ('PERMANENT','permanent'),
    ('CONTRACTUAL','contractual'),
    ('CASUAL','casual'),
    ('RETIRED','retired'),
    ('SELF_EMPLOYED','self_employed'),
    ('NONE','none'),

)
father_mode = (
    ('PERMANENT','permanent'),
    ('CONTRACTUAL','contractual'),
    ('CASUAL','casual'),
    ('RETIRED','retired'),
    ('SELF_EMPLOYED','self_employed'),
    ('NONE','none'),

)
family_mode = (
    ('TOTAL_ORPHAN','total_orphan'),
    ('PARTIAL_ORPHAN','partial_orphan'),
    ('SINGLE_PARENT','single_parent'),
    ('BOTH_PARENTS_ALIVE','both_parents_alive'),
    ('OTHER_STATE','other_state'),
    ('NUM_OF_SIBLINGS','num_of_siblings'),
    ('EST_FAMILY_INCOME','est_family_income'),
    ('EST_FAMILY_EXPENSES','est_family_expenses'),

)

class DateInput(forms.DateInput):
    input_type = 'date'

class add_scholarship_form(forms.ModelForm):
    class Meta:
        model = scholarship
        fields = ['title','short_description','long_description','img','both','boy','girl','active','document','scholarship_form','fromdate','toomdate']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'special'}),
            'fromdate': DateInput(),
            'toomdate': DateInput(),
        }

        labels = {
            'title': 'Title',
            'short_description': 'Short_description',
            'img': 'Picture',
            'both': ' Total(boys and girls)per branch',
            'boy':'Boys per branch( if distributed in boys and girls else leave -1)',
            'girl':'Girls per branch( if distributed in boys and girls else leave -1)',
            'document':'Scholarship SOP',
            'fromdate': 'Starting date (Make sure it is less then or equal to today"s date)',
            'toomdate': 'End date',
        }

class extra_documents_form(forms.ModelForm):
    class Meta:
        model = application_table
        fields = ['your_name','gender','date_of_birth','your_id_num','your_num','school_type','school_name','addmission_number','campus_branch','status','amnt_applied_for','allocated_amnt']
        labels = {
            'applied_scholarship_form':'Application form(Only in pdf)',
            'applied_extra1': 'Other Document 1',
            'applied_extra2': 'Other Document 2',
            'your_name': 'Your Full Names',
            'gender': 'Your Gender',
            'date_of_birth':'Date of Birth',
            'your_id_num':'Your ID Number if applicable',
            'your_num':'Contact Phone Number',
            'school_type':'Your Institution type',
            'school_name': 'Name of school/college/University',
            'addmission_number':'Your School Admission Number',
            'campus_branch': 'Campus Branch only for college/University',
        }
        widgets = {
            'your_name':forms.NumberInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth':forms.DateInput(attrs={'class': 'datepicker'}),
            'your_id_num':forms.NumberInput(attrs={'class':'form-control'}),
            'your_num':forms.NumberInput(attrs={'class':'form-control'}),
            'school_type': forms.Select(attrs={'class': 'form-control'}),
            'school_name': forms.TextInput(attrs={'class': 'form-control'}),
            'addmission_number': forms.Select(attrs={'class': 'form-control'}),
            'campus_branch': forms.TextInput(attrs={'class': 'form-control'}),








            'amnt_applied_for':forms.NumberInput(attrs={'class':'form-control'}),
            'allocated_amnt':forms.NumberInput(attrs={'readonly':False,'class':'form-control'}),


        }
# class extra_documents_form_in_details(forms.ModelForm):
#     class Meta:
#         model = application_table
#         fields = ['status','school_name','amnt_applied_for','allocated_amnt']
#         labels = {
#             'school_name': 'School Name',
#             'allocated_amnt':'Allocated Amount',
#             'amnt_applied_for':'Amnt Applied',
#             'date_of_birth': 'Date of Birth',
#             'status': 'Status',
class UpdateFieldWithCustomValueForm(forms.Form):

    custom_input = forms.CharField(max_length=20)
