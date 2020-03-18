from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .forms import InspectionForm


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


def inspectionf(request):
    form = InspectionForm(request.POST or request.FILES or None)
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        title = form.cleaned_data['title']
        inspection_tag = form.cleaned_data['inspection_tag']
        author = form.cleaned_data['author']
        content = form.cleaned_data['content']
        status = form.cleaned_data['status']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        # envoi = True

    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'inspection.html', locals())
