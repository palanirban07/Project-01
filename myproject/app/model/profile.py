from django.db import models
from app.model.base import Base
from django.contrib.auth.models import User

class Profile(Base):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20, null= True)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=16, null= True)
    
    