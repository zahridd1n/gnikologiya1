from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework import generics

from client_panel.models.booking import Booking
from client_panel.serializers.bookingSR import BookingSerializer
import requests

BOT_TOKEN = '6614663716:AAFez4utvUS_vVIhQIdnXsuietyS6QWhQcQ'
CHAT_IDS = ['1327096215','176697616']
class CreateBooking(APIView):
    def post(self, request):
        try:
            serializer = BookingSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                # Ma'lumotlarni olish
                name = serializer.validated_data['full_name']
                phone = serializer.validated_data['phone_number']
                
                text = text = f"""Saytdan xabar:\n📌 Mavzu: Ro'yhatga olish\n👤 Ismi: {name}\n📞 Tel: {phone}"""

                for chat_id in CHAT_IDS:
                    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}'
                    requests.get(url)

                return Response({'success':True,"message":"Ro'yhatga olish muvaffaqiyatli yakunlandi. Tez orada mutaxassilarimiz siz bilan bog'lanishadi"})
            return Response({'success':False,"message":"Ma'lumotlar to'liq kiritilmagan. Iltimos qayta urinib ko'ring"})
        except Exception as e:
            return Response({"error": str(e)}, status=500)
