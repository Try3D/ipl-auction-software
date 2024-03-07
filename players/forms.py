from .models import Player
from django.forms import ModelForm


class add(ModelForm):
    class Meta:
        model = Player
        fields = "__all__"
