from django.forms import ModelForm
from core.models import Test


class QuizForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'