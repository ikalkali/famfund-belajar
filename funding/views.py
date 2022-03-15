from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from funding.serializers import (InputPembayaranSerializer, PembayaranSerializer)
from .models import Asisten, Pembayaran
from datetime import datetime

# TODO : kasih try except sama validasi
# Create your views here.
class InputPembayaran(APIView):
    def post(self, request):
        # ambil data (parse data)
        data = {}

        # possible error disini
        data["nim"] = request.data["nim"]
        data["nominal"] = request.data["nominal"]
        data["tanggal_pembayaran"] = request.data["tanggal_pembayaran"]

        # possible error (asistennya gaada)
        # get asisten
        asisten = Asisten.objects.get(pk = data["nim"])
        print(asisten)  

        # database error
        # update pembayaran
        tanggal_bayar = datetime.now()
        pembayaran_baru = Pembayaran(nim=asisten, nominal=data["nominal"], tanggal_bayar=tanggal_bayar)
        pembayaran_baru.save()

        # database error
        # update tagihan
        # (misal asisten tagihan 5000, bayar 3000, tagihannya jadi 2000)

        serializer = InputPembayaranSerializer(data)
        return Response("success") 

    def get(self, request):
        return Response("hello")