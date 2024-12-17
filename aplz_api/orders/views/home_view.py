from rest_framework import status # type: ignore
from aplz_api.api_response import ApiResponse
from rest_framework.views import APIView # type: ignore
from orders.models import Order
from django.db.models import Sum, Count, Avg # type: ignore
from datetime import datetime

class HomeView(APIView):

    def get(self, request):

        try:

            branches = ""
            date = ""

            queryset = Order.objects.all()

            if request.query_params is not None and request.query_params.get("branches") is not None :
                branches = request.query_params.get("branches")
                branch_ids = branches.split(",") 
                queryset = queryset.filter(branchId__in=branch_ids)

            if request.query_params is not None and request.query_params.get("date") is not None :
                date = request.query_params.get("date")
                date_obj = datetime.strptime(date, "%Y-%m-%d")
                queryset = queryset.filter(updatedAt__date=date_obj.date())

            totals = queryset.aggregate(
                total_price=Sum('price'),
                total_records=Count('id'),
                average_price=Avg('price')
            )

            total_price = totals['total_price'] if totals['total_price'] is not None else 0
            total_records = totals['total_records'] if totals['total_records'] is not None else 0
            average_price = totals['average_price'] if totals['average_price'] is not None else 0

            data = {"total_price": total_price, "total_records":total_records,"average_price":average_price}

            return ApiResponse(
                success=True,
                data=[data],
                status=status.HTTP_200_OK
            )
        except Order.DoesNotExist:
            data = {"total_price": 0, "total_records":0,"average_price":0}

            return ApiResponse(
                    success=True,
                    data=[data],
                    status=status.HTTP_200_OK
                )
