from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import TBModel
from .serializers import TBModelSerializer
# Create your views here.


class TBList(APIView):
    """
    List all tb_cases, or create a new case.
    """
    def get(self, request, format=None):
        tb_cases = TBModel.objects.all()
        serializer = TBModelSerializer(tb_cases, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TBModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




