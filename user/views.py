from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    전체 유저 불러오기
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserDetailView(APIView):

    def get(self,request,id):
        model = User.objects.get(id=id)
        if model:
            serializer = UserSerializer(instance=model)
            return Response(serializer.data)
        else:
            return Response({"ErrorMessage": "해당 유저가 존재하지 않습니다"}, status=404)

    def delete(self,request,id):
        model = User.objects.get(id=id)
        if model:
            model.delete()
            return Response({"message":"정상적으로 삭제되었습니다"})
        else:
            return Response({"ErrorMessage": "해당 유저가 존재하지 않습니다"}, status=404)


