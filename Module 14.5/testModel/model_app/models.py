from django.db import models
from django.utils import timezone

class Student(models.Model):
#       auto_field = models.AutoField(primary_key=True)
#       big_auto_field = models.BigAutoField(primary_key=True)
        roll = models.IntegerField(primary_key= True)
        name = models.TextField()# null = True or blank = True for keeping empty fields

        binary_field = models.BinaryField(default=b'')
        boolean_field = models.BooleanField(default=True) # use BooleanField(null=True, blank=True) instead of NullBooleanField
        char_field = models.CharField(max_length=255, default='')
        time_field = models.TimeField(auto_now_add=True, null = True)
        date_field = models.DateField(auto_now_add=True, null = True)
        date_time_field = models.DateTimeField(auto_now_add=True, null = True)
        decimal_field = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
        duration_field = models.DurationField(default=timezone.timedelta(seconds=0))
        email_field = models.EmailField(default="test@gmail.com")
        file_field = models.FileField(upload_to='files/', default='default_file.txt')
        file_path_field = models.FilePathField(path='/path/to/files/', default='/path/to/files/default_file.txt')
        float_field = models.FloatField(default=0.0)
        generic_ip_address_field = models.GenericIPAddressField(default='127.0.0.1')
        image_field = models.ImageField(upload_to='images/', default='')
        json_field = models.JSONField(default=dict)
        positive_big_integer_field = models.PositiveBigIntegerField(default=2500999999999)
        positive_integer_field = models.PositiveIntegerField(default=29999999990)
        positive_small_integer_field = models.PositiveSmallIntegerField(default=10)
        slug_field = models.SlugField(default='default-slug')
        small_integer_field = models.SmallIntegerField(default=5)
        url_field = models.URLField(default='https://google.com')

"""
import uuid
uuid_field = models.UUIDField(default=uuid.uuid5, editable=False, unique=True)
one_to_one_field = models.OneToOneField(OtherModel, on_delete=models.CASCADE)

many_to_many_field = models.ManyToManyField(OtherModel)

foreign_key = models.ForeignKey(OtherModel, on_delete=models.CASCADE)

comma_separated_field = models.CharField(
        validators=[comma_separated_validator],
        max_length=255
    ) # it is depreciated in Django 3.1
"""