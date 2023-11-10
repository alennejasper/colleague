from django.db import models

# Create your models here.
class Gender(models.Model):
    is_male = models.BooleanField(default = False, help_text = "Designates that the classmate has male gender.", verbose_name = "Male")
    is_female = models.BooleanField(default = False, help_text = "Designates that the classmate has female gender.", verbose_name = "Female")
    is_other = models.BooleanField(default = False, help_text = "Designates that the classmate has other gender.", verbose_name = "Other")

    class Meta:
        verbose_name = "Gender"
        verbose_name_plural = "Genders"

    def __str__(self):
        if self.is_male == True:
            return "Male"
        
        elif self.is_female == True:
            return "Female"

        elif self.is_other == True:
            return "Other"

class Classmate(models.Model):
    first_name = models.CharField(max_length = 65, null = True, blank = True, help_text = "Designates the first name of the classmate.", verbose_name = "First Name")
    last_name = models.CharField(max_length = 65, null = True, blank = True, help_text = "Designates the last name of the classmate.", verbose_name = "Last Name")
    gender = models.ForeignKey(Gender, on_delete = models.SET_NULL, blank = True, null = True, help_text = "Designates the foreign field of the Gender model.", verbose_name = "Gender")
    age = models.IntegerField(null = True, help_text = "Designates the age of the classmate.", verbose_name = "Age")
    email = models.EmailField(max_length = 65, null = True, help_text = "Designates the email of the classmate.", verbose_name = "Email")
    phone_number = models.CharField(max_length = 10, null = True, blank = True, help_text = "Designates the phone number of the classmate.", verbose_name = "Phone Number")
    address = models.CharField(max_length = 65, null = True, blank = True, help_text = "Designates the address of the classmate.", verbose_name = "Address")
    profile_photo = models.ImageField(null = True, blank = True, upload_to = "profiles", help_text = "Designates the profile photo of the classmate.", verbose_name = "Profile Photo")
    date_joined = models.DateTimeField(auto_now_add = True, help_text = "Designates the date and time of the date joined by the classmate.", verbose_name = "Date Joined")
    
    class Meta:
        verbose_name = "Classmate"
        verbose_name_plural = "Classmates"
    
    @property
    def photo_url(self):
        if self.profile_photo and hasattr(self.profile_photo, "url"):
            return self.profile_photo.url
    
    def __str__(self):
        return str(self.last_name) + ", " + str(self.first_name)
