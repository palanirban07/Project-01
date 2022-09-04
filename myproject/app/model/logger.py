from django.db import models
from app.model.base import Base
from django.contrib.auth.models import User

class Logger(Base):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)