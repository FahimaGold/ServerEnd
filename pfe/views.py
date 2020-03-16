import json

from bokeh.command.subcommands.json import JSON
from django.http import JsonResponse, HttpResponse, HttpResponseServerError
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
import urllib.request
from .classification import ClassificationDiab
import numpy as np

#Lists all infos or create a new one
#infos/



vecteur = []



class InfoReception(APIView):


      permission_classes = (permissions.AllowAny,)
      def post(self, request):
          global vecteur
          #request.session.set_expiry(300)
          if request.method == 'POST':
             result = request.POST
             if result:
                vecteur = result
                print(vecteur)
                #patient = [BMI,ponds,taille, tension systolique, tension dyastolique, age, sexe, diabÃ©tique ou pas]


             else:
                 print("errroor!")


             return JsonResponse(result,safe=False)
          else:
             return Response({'key': 'value'}, status=status.HTTP_200_OK)


          #return  JsonResponse(data,safe=False)



      def get(self, request):

          classif = ClassificationDiab.get_classification_result(vecteur)
          s = str(classif)
          data = {"Res": s}
          print("welcome to city")
          print(vecteur)

          return  JsonResponse(data)
