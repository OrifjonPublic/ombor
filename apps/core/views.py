from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ActionLog, Cams, IceCream
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

    def perform_create(self, serializer):
        instance = serializer.save()
        instance._log_user = self.request.user
        instance.save()



class IceCreamEditView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer
    lookup_field = 'code'

    def perform_update(self, serializer):
        instance = self.get_object()
        instance._old_quantity = instance.quantity  # signalda ishlatamiz
        instance = serializer.save()
        instance._log_user = self.request.user
        instance.save()

    def perform_destroy(self, instance):
        instance._log_user = self.request.user
        instance.delete()
    

class InView(APIView):
    def post(self, request, code):
        try:
            p = IceCream.objects.get(code=code)
            q = request.data.get('quantity')
            if not isinstance(q, int) or q < 0:
                return Response({"message": "Miqdor noto‘g‘ri"}, status=400)
            p.quantity = p.quantity + q
            p.save()

            ActionLog.objects.create(
                    user=request.user,
                    action='in',
                    object_name=p.name,
                    object_id=p.code,
                    object_repr=f"{q} ta kirim qilindi",
                    quantity=q
                )
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
            ActionLog.objects.create(
                    user=request.user,
                    action='out',
                    object_name=p.name,
                    object_id=p.code,
                    object_repr=f"{q} ta chiqim qilindi",
                    quantity=q
                )

            return Response({"message": "Out is Ok!"})
        except IceCream.DoesNotExist:
            return Response({"message": "Mahsulot topilmadi"}, status=404)
            