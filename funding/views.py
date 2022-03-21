
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
        try :
            asisten = Asisten.objects.get(pk = data["nim"])
            print(asisten)  
        except:
            return Response("Nim tidak terdaftar !")

        # database error
        # update pembayaran
        try:
            tanggal_bayar = datetime.now()
            pembayaran_baru = Pembayaran(nim=asisten, nominal=data["nominal"], tanggal_bayar=data["tanggal_pembayaran"])
            pembayaran_baru.save()
        except:
            return Response("Data tidak terecord")
        # database error
        # update tagihan
        # (misal asisten tagihan 5000, bayar 3000, tagihannya jadi 2000)
        tagihan = asisten.tagihan
        print(tagihan)
        tagihan = tagihan - data["nominal"]
        
        serializer = InputPembayaranSerializer(data=data)
        serializerpembayaran = PembayaranSerializer()
        Asisten.objects.filter(pk=data["nim"]).update(tagihan=tagihan)
        
        if serializer.is_valid():
            return Response("success input data") 

    def get(self, request):
        return Response("Hallo mas")