from django import forms

# References
# https://docs.djangoproject.com/en/2.2/ref/forms/fields/#widget
# https://docs.djangoproject.com/en/2.2/ref/forms/fields/#built-in-field-classes


class Login(forms.Form):
    user_name = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class Registration(forms.Form):
    gender_choices = (('M', 'Male'), ('F', 'Female'))
    course_choices = (('P', 'Python'), ('D', 'Django'),
                      ('ML', 'Machine Learning'))
    country_choices = (('', '--Select--'), ('IND', 'India'),
                       ('AUS', 'Australia'), ('USA', 'United States of America'))
    years = [x for x in range(1950, 2019)]

    name = forms.CharField(help_text='(enter full name)')
    mobile = forms.CharField(required=False, disabled=True)
    password = forms.CharField(widget=forms.PasswordInput)

    email = forms.EmailField()

    experience = forms.IntegerField()

    dob = forms.DateField(label='Date of Birth', widget=forms.SelectDateWidget(
        years=years), initial="1990-06-21")

    graduate = forms.BooleanField(required=False)

    gender = forms.ChoiceField(
        choices=gender_choices, widget=forms.RadioSelect)

    courses = forms.MultipleChoiceField(
        required=False, widget=forms.CheckboxSelectMultiple, choices=course_choices)
    country = forms.ChoiceField(required=False, choices=country_choices)

    comment = forms.CharField(widget=forms.Textarea)

    image = forms.URLField(label="Image URL", required=False)

    def __str__(self):
        return self.name + ' ' + self.email
