from django import forms


class studentform(forms.Form):
    firstname = forms.CharField(label="ENTER FIRST NAME", max_length=50)
    lastname = forms.CharField(label="ENTER LAST NAME", max_length=50)
    email = forms.CharField(label="enter the email", max_length=30)
    phonenumber = forms.CharField(label= "contact" ,max_length=12)
