from orders.serializer import OrderSerializer
from rest_framework import status # type: ignore
from aplz_api.api_response import ApiResponse
from rest_framework.views import APIView # type: ignore
from orders.models import Order
from datetime import datetime
from django.core.paginator import Paginator # type: ignore

class HistoryView(APIView):

    def get(self, request):

        try:

            date = ""

            first_date = None
            end_date = None

            queryset = Order.objects.all()

            first_date = request.query_params.get("first_date")
            end_date = request.query_params.get("end_date")

            order_by = request.query_params.get("order_by", "updatedAt") 
            direction = request.query_params.get("direction", "asc")  

            if first_date is not None and end_date is not None:
                first_date_obj = datetime.strptime(first_date, "%Y-%m-%d")
                end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
                queryset = queryset.filter(updatedAt__date__gte=first_date_obj.date(), updatedAt__date__lte=end_date_obj.date())
        
            elif first_date is not None:
                first_date_obj = datetime.strptime(first_date, "%Y-%m-%d")
                queryset = queryset.filter(updatedAt__date__gte=first_date_obj.date())

            elif end_date is not None:
                end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
                queryset = queryset.filter(updatedAt__date__lte=end_date_obj.date())

            if direction == "desc":
                order_by = f"-{order_by}"
            else:
                order_by = order_by 

            queryset = queryset.order_by(order_by)
        

            paginator = Paginator(queryset, 10)
            page_number = request.query_params.get("page", 1)
            page_data = paginator.page(page_number)

            serializer = OrderSerializer(instance=page_data.object_list, many=True)
            data = {"orders": serializer.data,"total":queryset.count()}

            return ApiResponse(
                success=True,
                data=[data],
                status=status.HTTP_200_OK
            )
        except Order.DoesNotExist:
            data = {"orders": [],"total":0}

            return ApiResponse(
                    success=True,
                    data=[data],
                    status=status.HTTP_200_OK
                )
