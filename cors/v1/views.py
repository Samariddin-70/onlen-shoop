from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from .serializer import CategorySerializer
from cors.models.products import Category


class CategoryViews(GenericAPIView):
    permission_classes = AllowAny,
    serializer_class = CategorySerializer
    queryset = Category.objects.all

    def get_object(self, id):
        return Category.objects.get(id=id)

    def get(self, request, id=None):
        status = HTTP_200_OK
        if id:
            data = self.get_object(id)
            if not data:
                data = {
                    "error": "Data pustoy"
                }
                status = HTTP_404_NOT_FOUND
            else:
                data = data.get_response()
            return Response(data, status=status)

        else:
            data = [x.get_response() for x in self.queryset()]

        return Response({
            'Natija': data
        }, status=status )


    def post(self, request):
        
        "asosan post zaprosi yangi narsani qushish uchun ishlatiladi"

        return Response({
            'Natija': 'Bu bizni POST funksiyamiz'
        })

    def put(self, request):
        return Response({
            'Natija' : 'Bu bizni PUT funksiyamiz'
        })

    def patch(self, request):
        return Response({
            'Natija': 'Bu bizni PATCH funksiyamiz'
        })

    def delete(self, request):
        return Response({
            'Natija': 'Bu bizni DELETE funksiyamiz'
        })
