from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import views as jwt_views
from apps.orders.models import Order, Otihistory
from apps.orders.api.serializers import OrderSerializer, OtiSerializer, OrderSerializerRel
from rest_framework.permissions import IsAuthenticated

class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        orders = Order.objects.all()
        orders_serializer = OrderSerializerRel(orders, many = True)
        return Response(orders_serializer.data)

    def post(self, request):
        orders_serializer = OrderSerializer(data = request.data)
        if orders_serializer.is_valid():
            orders_serializer.save()
            return Response(orders_serializer.data)
        return Response(orders_serializer.errors, status=400)

class OrderDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk=None):
        order = Order.objects.filter(id = pk).first()
        order_serializer = OrderSerializer(order)
        return Response(order_serializer.data)
    
    def put(self, request, pk):
        order = Order.objects.filter(id=pk).first()
        order_serializer = OrderSerializer(order, data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data)
        return Response(order_serializer.errors, status=400)

    def delete(self, request, pk):
        order = Order.objects.filter(id = pk).first()
        order.delete()
        return Response("Eliminado")

class OrderListsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        orders = Order.objects.filter(production_id = pk).all()
        orders_serializer = OrderSerializer(orders, many = True)
        return Response(orders_serializer.data)

class OtiHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        otihistory = Otihistory.objects.filter(oti_id = pk).all()
        otihistory_serializer = OtiSerializer(otihistory, many=True)
        return Response(otihistory_serializer.data)
    
    def post(self, request):
        oti_serializer = OtiSerializer(data = request.data)
        if oti_serializer.is_valid():
            oti_serializer.save()
            return Response(oti_serializer.data)
        return Response(oti_serializer.errors, status=400)

class OrderByUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        orders = Order.objects.filter(current_operator = pk).all()
        orders_serializer = OrderSerializer(orders, many = True)
        return Response(orders_serializer.data)