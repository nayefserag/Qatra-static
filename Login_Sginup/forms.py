from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone


CHOICES1 = (('ذكر','ذكر'),
            ('انثى','انثى'))
CHOICES2 = (('A+','A+'),
            ('O+','O+'),
            ('B+','B+'),
            ('AB+','AB+'),
            ('A-','A-'),
            ('O-','O'),
            ('A-','A-'),
            ('B-','B-'),
            ('AB-','AB-'))
CHOICES3 = (('نعم','نعم'),
            ('لا','لا'))
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=101,label='الاسم بالكامل')
    email = forms.EmailField(label='البريد الالكتروني')
    phone = forms.CharField(max_length=101,label='رقم الهاتف')
    identity = forms.CharField(max_length=101,label='رقم الهويه')
    gender = forms.ChoiceField(choices=CHOICES1, required=True,label='النوع')
    age = forms.IntegerField( required=True,label='العمر')
    blood_type=forms.ChoiceField(choices=CHOICES2,label='فصيلة الدم')
    The_last_donate=forms.CharField(initial=timezone.now,label='تاريخ اخر تبرع')
    issuse=forms.ChoiceField(choices=CHOICES3,label='هل تعاني من أي امراض مزمنه؟')

    class Meta:
        model = User
        fields = [ 'username','email','phone', 'password1', 'password2','identity','gender','age' ,'blood_type','The_last_donate','issuse']
        labels = {
            'password1' : 'كلمة المرور',
            'password2' : 'تأكيد كلمة المرور',
        }
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k, v in self.Meta.labels.items():
            self[k].label = v
