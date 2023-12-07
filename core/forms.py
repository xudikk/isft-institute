from django.forms import ModelForm
from core.models import Test


class QuizForm(ModelForm):
    class Meta:
        model = Test
        fields = ["a", "b", "c", "d", "true"]