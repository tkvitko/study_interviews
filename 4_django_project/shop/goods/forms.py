from django.forms import ModelForm

from .models import Good


class GoodForm(ModelForm):
    class Meta:
        model = Good
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GoodForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
