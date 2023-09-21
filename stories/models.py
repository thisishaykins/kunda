from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

from auditlog.registry import auditlog

# Create your models here.
class Stories(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, related_name='stories_user', on_delete=models.CASCADE)
    request = models.CharField(validators=[RegexValidator(
                regex=r"^[a-zA-Z0-9-_., ]+$",
                message="Only numbers, letters, underscores, dots, dashes, comma, and spaces are allowed."
            )], blank=False, null=False, max_length=200, default=None)
    content = models.TextField(validators=[RegexValidator(
        regex=r"^[a-zA-Z0-9-_./ ]+$",
        message="Only numbers, letters, underscores, dots, dashes, forward-slash, and spaces are allowed."
    )], null=False, name="story content")
    ai_model = models.CharField(validators=[RegexValidator(
                regex=r"^[a-zA-Z0-9-_., ]+$",
                message="Only numbers, letters, underscores, dots, dashes, comma, and spaces are allowed."
            )], blank=True, null=True, max_length=50, default=None)
    ai_role = models.CharField(validators=[RegexValidator(
                regex=r"^[a-zA-Z0-9-_., ]+$",
                message="Only numbers, letters, underscores, dots, dashes, comma, and spaces are allowed."
            )], blank=True, null=True, max_length=50, default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class UserStories(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, related_name='user_stories', on_delete=models.CASCADE)
    story = models.ForeignKey(Stories, null=False, blank=False, related_name='user_stories_story', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


auditlog.register(Stories)
auditlog.register(UserStories)