from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from club.models import Club, ClubType


class SignUpForm(UserCreationForm):
    club_name = forms.CharField(max_length=100, help_text='동아리 이름')
    club_type = forms.ModelChoiceField(queryset=ClubType.objects.all(), empty_label="Select Club Type", help_text='동아리 유형')

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('club_name', 'club_type',)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            club_name = self.cleaned_data.get('club_name')
            club_type = self.cleaned_data.get('club_type')
            Club.objects.create(name=club_name, club_type=club_type, owner=user)
        return user
