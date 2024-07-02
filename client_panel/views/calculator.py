from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class PregnancyDetailView(APIView):
    def get(self, request, *args, **kwargs):
        # Query parametrlarini qabul qilamiz
        lmp_date_str = request.query_params.get('xayz', None)  # '15-03-2023' kabi
        eku_date_str = request.query_params.get('urug', None)  # '15-03-2023' kabi

        # Kamida bittasini kiritganligini tekshiramiz
        if not lmp_date_str and not eku_date_str:
            return Response({"detail": "Iltimos, yuqoridagi bo'limlardan birini tanlash"}, status=status.HTTP_400_BAD_REQUEST)

        # Bugungi kun
        today = datetime.now().date()
        
        # Maksimal orqa sanani hisoblash
        max_past_date = today - timedelta(days=294)  # 10 oy = taxminan 304 kun
        
        results = {}
        
        if lmp_date_str:
            try:
                lmp_date = datetime.strptime(lmp_date_str, '%d-%m-%Y').date()
            except ValueError:
                return Response({"detail": "Oxirgi xayz sanasi formati noto'g'ri. To'g'ri format: DD-MM-YYYY."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Sana tekshiruvi
            if lmp_date < max_past_date:
                return Response({"detail": "Oxirgi xayz sanasi bugungi kundan 10 oy orqadan ko'p bo'lmasligi kerak."}, status=status.HTTP_400_BAD_REQUEST)

            # LMP asosida homiladorlik muddatini hisoblash
            delta_days = (today - lmp_date).days
            current_weeks = delta_days // 7
            current_days = delta_days % 7

            # LMP asosida tug'ruqqacha qolgan kunlar
            days_left = 280 - delta_days  # 280 = 40 hafta * 7 kun
            due_date = lmp_date + timedelta(days=280)

            results['title'] = f"Tabriklaymiz! Siz homiladorlikning {current_weeks}-haftasidasiz!"
            results['details'] = {
            'text1': f"Homiladorlikning hozirgi muddati {current_weeks} hafta {current_days} kun",
            'text2': f"Tug’ruqqacha qolgan kunlar {days_left} kun",
            'text3': f"Taxminiy tug’ruq kuni {due_date.strftime('%Y-%m-%d')}"}

        if eku_date_str:
            try:
                eku_date = datetime.strptime(eku_date_str, '%d-%m-%Y').date()
            except ValueError:
                return Response({"detail": "EKU qilingan kun formati noto'g'ri. To'g'ri format: DD-MM-YYYY."}, status=status.HTTP_400_BAD_REQUEST)
            
            # Sana tekshiruvi
            if eku_date < max_past_date:
                return Response({"detail": "EKU qilingan kun bugungi kundan 10 oy orqadan ko'p bo'lmasligi kerak."}, status=status.HTTP_400_BAD_REQUEST)

            # EKU qilingan sana asosida homiladorlik muddatini hisoblash
            delta_days = (today - eku_date).days
            current_weeks = (delta_days // 7) + 2  # EKU sanasiga 2 hafta qo'shamiz
            current_days = delta_days % 7

            # EKU qilingan sana asosida tug'ruqqacha qolgan kunlar
            days_left = 266 - delta_days  # 266 = 38 hafta * 7 kun
            due_date = eku_date + timedelta(days=266)

            results['title'] = f"Tabriklaymiz! Siz homiladorlikning {current_weeks}-haftasidasiz!"
            results['details'] = {
            'text1': f"Homiladorlikning hozirgi muddati {current_weeks} hafta {current_days} kun",
            'text2': f"Tug’ruqqacha qolgan kunlar {days_left} kun",
            'text3': f"Taxminiy tug’ruq kuni {due_date.strftime('%Y-%m-%d')}"}

        
        response_data = {
            'success': True,
            'message': "Success",
            'data': results
        }

        return Response(response_data, status=status.HTTP_200_OK)
