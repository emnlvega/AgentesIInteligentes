from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ubicacion
from .serializers import UbicacionSerializer

@api_view(['GET', 'POST'])
def ubicaciones(request):
    if request.method == 'GET':
        ubicaciones = Ubicacion.objects.all().order_by('-timestamp')[:10]
        serializer = UbicacionSerializer(ubicaciones, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UbicacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)