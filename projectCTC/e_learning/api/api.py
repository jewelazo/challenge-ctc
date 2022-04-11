from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from e_learning.models import Padre, Estudiante
from e_learning.api.serializers import PadreSerializer, EstudianteSerializer


class PadreAPIView(GenericAPIView):

    serializer_class = PadreSerializer
    queryset = ''

    def get(self, request):
        padres = Padre.objects.all()
        padres_serializer = PadreSerializer(padres, many=True)
        return Response(padres_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        padre_serializer = PadreSerializer(data=request.data)
        if padre_serializer.is_valid():
            padre_serializer.save()
            return Response(padre_serializer.data, status=status.HTTP_201_CREATED)
        return Response(padre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PadreDetailAPIView(GenericAPIView):

    serializer_class = PadreSerializer
    queryset = ''

    def get(self, request, pk=None):
        padre = Padre.objects.filter(pk=pk).first()
        if padre:
            padre_serializer = PadreSerializer(padre)
            return Response(padre_serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No existe ese id"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        padre = Padre.objects.filter(pk=pk).first()
        if padre:
            padre_serializer = PadreSerializer(padre, data=request.data)
            if padre_serializer.is_valid():
                padre_serializer.save()
                return Response(padre_serializer.data, status=status.HTTP_200_OK)
            return Response(padre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "No existe ese id"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        padre = Padre.objects.filter(pk=pk).first()
        if padre:
            padre.delete()
            return Response({"message": "eliminado exitosamente"}, status=status.HTTP_200_OK)
        return Response({"message": "No existe ese id"}, status=status.HTTP_400_BAD_REQUEST)


class EstudianteAPIView(GenericAPIView):

    serializer_class = EstudianteSerializer
    queryset = ''

    def get(self, request):
        estudiantes = Estudiante.objects.all()
        estudiantes_serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(estudiantes_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        estudiante_serializer = EstudianteSerializer(data=request.data)
        if estudiante_serializer.is_valid():
            estudiante_serializer.save()
            return Response(estudiante_serializer.data, status=status.HTTP_201_CREATED)
        return Response(estudiante_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EstudianteDetailAPIView(GenericAPIView):

    serializer_class = EstudianteSerializer
    queryset = ''

    def get(self, request, pk=None):
        estudiante = Estudiante.objects.filter(pk=pk).first()
        if estudiante:
            estudiante_serializer = EstudianteSerializer(estudiante)
            return Response(estudiante_serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "No existe ese id"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        estudiante = Estudiante.objects.filter(pk=pk).first()
        if estudiante:
            estudiante_serializer = PadreSerializer(estudiante, data=request.data)
            if estudiante_serializer.is_valid():
                estudiante_serializer.save()
                return Response(estudiante_serializer.data, status=status.HTTP_200_OK)
            return Response(estudiante_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "No existe ese id"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        estudiante = Estudiante.objects.filter(pk=pk).first()
        if estudiante:
            estudiante.delete()
            return Response({"message": "eliminado exitosamente"}, status=status.HTTP_200_OK)
        return Response({"message": "No existe ese id"}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET','POST'])
# def padre_api_view(request):

#     # list
#     if request.method=="GET":
#         padres=Padre.objects.all()
#         padres_serializer=PadreSerializer(padres,many=True)

#         return Response(padres_serializer.data,status=status.HTTP_200_OK)

#     # create
#     elif request.method=="POST":
#         padre_serializer=PadreSerializer(data=request.data)
#         if padre_serializer.is_valid():
#             padre_serializer.save()
#             return Response(padre_serializer.data,status=status.HTTP_201_CREATED)
#         return Response(padre_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET","PUT","DELETE"])
# def padre_detail_api_view(request,pk=None):
#     # queryset
#     padre=Padre.objects.filter(id=pk).first()

#     #validation
#     if padre:

#         # retrieve
#         if request.method=="GET":
#             padre_serializer=PadreSerializer(padre)
#             return Response(padre_serializer.data,status=status.HTTP_200_OK)

#         # update
#         elif request.method=="PUT":
#             padre=Padre.objects.filter(id=pk).first()
#             padre_serializer=PadreSerializer(padre,data=request.data)
#             if padre_serializer.is_valid():
#                 padre_serializer.save()
#                 return Response(padre_serializer.data,status=status.HTTP_200_OK)
#             return Response(padre_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#         # delete
#         elif request.method=="DELETE":
#             padre=Padre.objects.filter(id=pk).first()
#             padre.delete()
#             return Response({"message":"eliminado exitosamente"},status=status.HTTP_200_OK)


#     return Response({"message":"No existe ese id"},status=status.HTTP_400_BAD_REQUEST)
