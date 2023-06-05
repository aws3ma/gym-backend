import datetime
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PaiementSerializer
from .models import Paiement
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

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
            paiements = Paiement.objects.filter(bodybuilder__user=user_id)
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

class PaiementStats(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_id = str(request.user.id)
        year = datetime.date.today().year
        if "year" in request.query_params.keys():
            year = int(request.query_params["year"])
        format = '%Y-%m-%d'
        return_data={
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0,
            9:0,
            10:0,
            11:0,
            12:0
        }
        paiements = Paiement.objects.filter(Q(start_date__year=year) | Q(due_date__year=year),bodybuilder__user=user_id)
        paiements = PaiementSerializer(paiements, many=True)
        # print(paiements.data)
        for p in paiements.data:
            st_date = datetime.datetime.strptime(p['start_date'], format)
            end_date = datetime.datetime.strptime(p['due_date'], format)
            if(end_date.year>year):
                diff=int((end_date-st_date).days/30)
                amout_to_add = float(p['amount'])/diff
                old_diff = diff-end_date.month
                diff -= old_diff
                p['amount']=float(p['amount'])-amout_to_add*old_diff
                end_date = datetime.date(year,12,31)
            elif(st_date.year<year):
                diff=int((end_date-st_date).days/30)
                amout_to_add = float(p['amount'])/diff
                old_diff = diff-(12-st_date.month)
                diff=diff-old_diff
                print(st_date.month)
                p['amount']=float(p['amount'])-amout_to_add*old_diff
                st_date = datetime.date(year,1,1)
            else:
                diff=int((end_date-st_date).days/30)
            for j in range(st_date.month,st_date.month+diff):
                return_data[j]+=float(p['amount'])/diff
        return Response(data=return_data, status=status.HTTP_200_OK)