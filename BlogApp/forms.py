from django import forms


class UserInfo(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    website = forms.CharField(required=False)
    # comment = forms.CharField() #??
#class UserComment(form.Form):


