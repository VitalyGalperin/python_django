from django import forms


class ChoiceForm(forms.Form):
    region = forms.ChoiceField(choices=(
        (1, 'Нижегородская область'), (2, 'Московская область'), (3, 'Вологодская область'), (4, 'Негев и Арава')))
    category = forms.ChoiceField(choices=((1, 'Услуги'), (2, 'Дома на продажу'), (3, 'Велосипеды и запчасти')))
    topic = forms.CharField()


class AdvertisementForm(forms.Form):
    counter = forms.IntegerField(disabled=True, initial=0)
