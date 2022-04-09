from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from e_learning.models import Padre
from e_learning.api.serializers import PadreSerializer

@api_view(['GET','POST'])
def padre_api_view(request):
    
    if request.method=="GET":
        padres=Padre.objects.all()
        padres_serializer=PadreSerializer(padres,many=True)
        return Response(padres_serializer.data)

    elif request.method=="POST":
        padre_serializer=PadreSerializer(data=request.data)
        if padre_serializer.is_valid():
            padre_serializer.save()
            return Response(padre_serializer.data)
        return Response(padre_serializer.errors)

