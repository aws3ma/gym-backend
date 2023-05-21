from django.contrib.auth.models import User
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import BodyBuilderSerializer
from .models import BodyBuilder
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class BodyBuilderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data["user"] = request.user.id
        serializer = BodyBuilderSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        user_id = str(request.user.id)
        id = "0"
        if "id" in request.query_params.keys():
            id = request.query_params["id"]
        if id == "0":
            body_builders = BodyBuilder.objects.filter(user_id=user_id)
        if id != "0":
            body_builders = BodyBuilder.objects.filter(id=id)
        body_builders = BodyBuilderSerializer(body_builders, many=True)
        return Response(body_builders.data, status=status.HTTP_200_OK)
    def put(self,request):
        bodybuilder = BodyBuilder.objects.get(id=request.data["id"])
        ser = BodyBuilderSerializer(instance=bodybuilder,data=request.data,partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(status=status.HTTP_201_CREATED)