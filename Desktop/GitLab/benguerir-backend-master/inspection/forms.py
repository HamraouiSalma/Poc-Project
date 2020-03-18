#cleaned_data dictionnaire
from django import forms

class InspectionForm(forms.Form):
    title = forms.CharField(max_length=100,label="Objet d'inspection : ")
    inspection_tag = forms.SlugField(max_length=150)
    author = forms.CharField(widget=forms.Textarea, label="Auteur d'inspection : ")
    #content  = forms.EmailField(label="Votre adresse e-mail")
    #renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)content,status
    content = forms.Textarea()
    status = forms.CheckboxInput()
    img = forms.ImageField()

