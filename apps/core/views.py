from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Cams, IceCream
from .serializers import IceCreamSerializer, CamSerializer


class CamListView(generics.ListCreateAPIView):
    queryset = Cams.objects.all()
    serializer_class = CamSerializer


class CamEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cams.objects.all()
    serializer_class = CamSerializer
    look_up_field = 'id'
    

class IceCreamListView(generics.ListCreateAPIView):
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer


class IceCreamEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer
    lookup_field = 'code'
    

class InView(APIView):
    def post(self, request, code):
        try:
            p = IceCream.objects.get(code=code)
            q = request.data.get('quantity')
            if not isinstance(q, int) or q < 0:
                return Response({"message": "Miqdor noto‘g‘ri"}, status=400)
            p.quantity = p.quantity + q
            p.save()
            return Response({"message": "In is Ok!"})
        except IceCream.DoesNotExist:
            return Response({"message": "Mahsulot topilmadi"}, status=404)


class OutView(APIView):
    def post(self, request, code):
        try:
            p = IceCream.objects.get(code=code)
            q = request.data.get('quantity')
            if not isinstance(q, int) or q < 0 or p.quantity < q:
                return Response({"message": "Miqdor yetarli emas yoki noto‘g‘ri"}, status=400)
            p.quantity = p.quantity - q
            p.save()
            return Response({"message": "Out is Ok!"})
        except IceCream.DoesNotExist:
            return Response({"message": "Mahsulot topilmadi"}, status=404)
            