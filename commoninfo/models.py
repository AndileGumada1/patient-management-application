from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserInfo(AbstractUser):
	    user_name 		= models.CharField(max_length=130)
	    email 	  		= models.EmailField(blank=True)
	    password  		= models.CharField(max_length=130)
	    re_type			= models.CharField(max_length=130)
	    first_name		= models.CharField(max_length=130)
	    last_login		= models.CharField(max_length=130)
	    uniqueID		= models.IntegerField(null=True)
	    dateOfbirth		= models.DateField(auto_now_add=True)
	 


