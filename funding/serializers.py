from dataclasses import field
from rest_framework import serializers

from funding.models import Pembayaran
# from funding.models import Asisten

class InputPembayaranSerializer(serializers.Serializer):
    nim = serializers.CharField()
    nominal = serializers.IntegerField()
    tanggal_pembayaran = serializers.DateTimeField()

# class ModelAsistenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Asisten
#         fields = "__all__"

class PembayaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembayaran
        fields = ['nominal', 'nim', 'tanggal_bayar']