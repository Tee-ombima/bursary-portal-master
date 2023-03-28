from django.db import models
from datetime import datetime,date

from django.core.exceptions import ValidationError
from django.utils import timezone




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
SCHOOL_CHOICES = [
        ('primary', 'Primary School'),
        ('highschool', 'High School'),
        ('college', 'College'),
        ('university', 'University'),
    ]
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
def file_size(value): # add this to some file where you can import it from
    limit =  1024*1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 1 MB.')

    if not value.path.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise ValidationError('File format is not correct , only png, jpg, or jpeg allowed')

def file_size2(value): # add this to some file where you can import it from
    limit =  1024*1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 1 MB.')

    if not value.path.lower().endswith('.pdf'):
        raise ValidationError('File format is not correct, Only pdf allowed ')



class scholarship(models.Model):
    title=models.CharField(max_length=30)
    short_description= models.CharField(max_length=100)
    long_description=models.TextField()
    img=models.ImageField(upload_to='pics/scholarship_pics',default='pics/scholarship_pics/default.png',validators=[file_size])
    both = models.IntegerField(blank=True,null=True,default=0)
    boy=models.IntegerField(blank=True,null=True,default=-1)
    girl = models.IntegerField(blank=True,null=True,default=-1)
    active = models.BooleanField(default=True)
    document = models.FileField(upload_to='documents/scholarship_broucher/',validators=[file_size2])
    scholarship_form = models.FileField(upload_to='documents/scholarship_form/',default='documents/scholarship_form/default_scholarship_form.pdf',validators=[file_size2])
    fromdate=models.DateField(null=True)
    toomdate = models.DateField(null=True)




class application_table(models.Model):
    scholarship_id=models.IntegerField(default=0)
    user_id=models.IntegerField(default=0)
    status = models.IntegerField(default=2,blank=True,null=True)


    your_name = models.CharField(max_length=20,default='myname',null=True, blank=True)
    your_num = models.IntegerField(default= 0o722000000)
    your_id_num = models.IntegerField(default=00000000)

    date_of_birth=models.DateField(default=timezone.now)
    gender=models.CharField(max_length=20,default='')
    school_type = models.CharField(max_length=20, choices=SCHOOL_CHOICES, default='primary')
    school_name=models.CharField(max_length=20,default='n/a',blank=False)
    addmission_number=models.CharField(max_length=25,blank=True,null=True)
    campus_branch=models.CharField(max_length=25, default='muranga')
    faculty=models.CharField(max_length=20,default='')
    course_of_study=models.CharField(max_length=20,default='')
    mode_of_study=models.CharField(max_length=30,default='')
    year_of_study=models.CharField(max_length=20,default='')
    academic_year=models.CharField(max_length=10,default=0)
    course_duration=models.IntegerField(default=0)
    year_of_completion=models.IntegerField(default=0)
    physical_address=models.CharField(max_length=20,default='')
    location=models.CharField(max_length=20,default='')
    sub_location=models.CharField(max_length=20,default='')
    ward=models.CharField(max_length=20,default='')
    institutions_postal_address=models.CharField(max_length=20,default='')
    institutions_tel_no=models.CharField(max_length=20,default='')
    amnt_applied_for=models.CharField(max_length=20,default='')
    family_background=models.CharField(max_length=30, default='')
    num_of_siblings=models.IntegerField(default=0)
    sibling_name=models.CharField(max_length=20,default='')
    sibling_institution=models.CharField(max_length=30,default='college')
    sibling_fee=models.IntegerField(default='0')
    est_family_income=models.IntegerField(default=10000)
    est_family_expenses=models.IntegerField(default=10000)
    school_in_kenya=models.CharField(max_length=30,default='none')
    allocated_amnt=models.CharField(max_length=20,default='',null=True)


    father_name=models.CharField(max_length=30,default='',blank=True,null=True)
    father_address=models.CharField(max_length=20,default='')
    father_num=models.CharField(max_length=20,default='')
    father_occupation=models.CharField(max_length=20,default='')
    father_employment=models.CharField(max_length=50, default='')
    father_main_income=models.CharField(max_length=20,default='')

    mother_name=models.CharField(max_length=30,default='',blank=True,null=True)
    mother_address=models.CharField(max_length=20,default='')
    mother_num=models.CharField(max_length=20,default='')
    mother_occupation=models.CharField(max_length=20,default='')
    mother_employment=models.CharField(max_length=50, default='')
    mother_main_income=models.CharField(max_length=20,default='')

    guardian_name=models.CharField(max_length=30,default='',blank=True,null=True)
    guardian_address=models.CharField(max_length=20,default='')
    guardian_num=models.CharField(max_length=20,default='')
    guardian_occupation=models.CharField(max_length=20,default='')
    guardian_employment=models.CharField(max_length=50, default='')
    guardian_main_income=models.CharField(max_length=20,default='')

    applied_student_id = models.FileField(upload_to='applications/student_id',blank=True,null=True)
    applied_father_id = models.FileField(upload_to='applications/father_id',blank=True,null=True)
    applied_document_last_sem = models.FileField(upload_to='applications/document_last_sem',blank=True,null=True)
    applied_document12 = models.FileField(upload_to='applications/document12',blank=True,null=True)
    applied_document10 = models.FileField(upload_to='applications/document10',blank=True,null=True)
    applied_extra1 = models.FileField(upload_to='applications/extra1',blank=True,null=True,validators=[file_size])
    applied_extra2 = models.FileField(upload_to='applications/extra2',blank=True,null=True,validators=[file_size])
    applied_scholarship_form = models.FileField(upload_to='applications/applied_scholarship_form',blank=True,null=True,validators=[file_size2])

    def get_my_integer_field_display(self):
        if self.status == 1:
            return "Success"
        elif self.status == 2:
            return "Pending"
        elif self.status == 3:
            return "Reject"
        else:
            return str(self.my_integer_field)



class session_table(models.Model):
    user_id = models.IntegerField(default=0)
    scholarship_id = models.IntegerField(default=0)
    session = models.IntegerField(default=0)
