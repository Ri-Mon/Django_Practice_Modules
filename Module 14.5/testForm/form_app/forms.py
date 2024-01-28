from django import forms
from datetime import datetime

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
GEEKS_CHOICES = ( 
    (1, "A"), 
    (2, "B"), 
    (3, "C"), 
    (4, "D"), 
    (5, "E"), 
)

class TestForm(forms.Form):
    name = forms.CharField(label="Enter your Name", initial="Your Name")
    email = forms.EmailField(label = "User Email", initial='mail@gmail.com',error_messages = { 
                 'required':"Please Enter your mail"
                 })
    roll_number = forms.IntegerField(  
                     help_text = "Enter 6 digit roll number"
                     )  
    password = forms.CharField(widget = forms.PasswordInput()) 
    comment = forms.CharField(widget=forms.Textarea, label = "Enter Your Comments")
    ShortComment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), required=False)
    Agree = forms.BooleanField()
    agree = forms.BooleanField(initial=True)
    date = forms.DateField()
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget())
    value = forms.DecimalField()
    message = forms.CharField(
	max_length = 10,
    )
    day = forms.DateField(initial=datetime.now())
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color_button = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    multiple_favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)

    favorite_colors_checkbox = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)
    
    TypedchoiceField = forms.TypedChoiceField( 
                   choices = GEEKS_CHOICES, 
                   coerce = str
                  )
    Duration_field = forms.DurationField( )
    file_field = forms.FileField()
    filePath_field = forms.FilePathField(path = "E:/") 
    UUID_field = forms.UUIDField( ) 
    URL_field = forms.URLField( )
    Time_field = forms.TimeField( )
    Regex_field = forms.RegexField(regex = "G.*s")
    nullBoolean_field = forms.NullBooleanField( )

    ip_field = forms.GenericIPAddressField( )
    img_field = forms.ImageField()
    float_field = forms.FloatField( )




    


"""
model_choice = forms.ModelChoiceField(
        queryset = MyModel.objects.all(),
        initial = 0
        )
model_choices = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple,
        queryset = MyModel.objects.all(),
        initial = 0
        )
slug_field = models.SlugField(max_length = 200)

"""






