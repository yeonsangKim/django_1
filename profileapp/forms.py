from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm) :

    class Meta :            #이미지를 표현하기 위한 외부적인 정보들

        model=Profile
        fields=['image','nickname','message']




