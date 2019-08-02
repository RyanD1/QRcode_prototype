from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser
)

class User(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True)
    first_name  = models.CharField(max_length=255)
    last_name  = models.CharField(max_length=255)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = [first_name, last_name]

    def __str__(self):
        return
    
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def get_short_name(self):
        return self.email
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin