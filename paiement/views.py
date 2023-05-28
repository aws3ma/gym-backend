from django.contrib.auth.models import User
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PaiementSerializer
from .models import Paiement
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class PaiementView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data["user"] = request.user.id
        serializer = PaiementSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data,status=status.HTTP_201_CREATED)

    def get(self, request):
        user_id = str(request.user.id)
        bodybuilder_id = "0"
        if "bodybuilder" in request.query_params.keys():
            bodybuilder_id = request.query_params["bodybuilder"]
        if bodybuilder_id == "0":
            paiements = Paiement.objects.filter(user_id=user_id)
        if bodybuilder_id != "0":
            paiements = Paiement.objects.filter(bodybuilder_id=bodybuilder_id)
        paiements = PaiementSerializer(paiements, many=True)
        return Response(paiements.data, status=status.HTTP_200_OK)
    # def put(self,request):
    #     budget = Paiement.objects.get(id=request.data["id"])
    #     ser = PaiementSerializer(instance=budget,data=request.data,partial=True)
    #     ser.is_valid(True)
    #     ser.save()
    #     return Response(status=status.HTTP_201_CREATED)