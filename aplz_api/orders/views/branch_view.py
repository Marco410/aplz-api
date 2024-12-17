from rest_framework import status # type: ignore
from aplz_api.api_response import ApiResponse
from rest_framework.views import APIView # type: ignore
from orders.models import Order


class BranchView(APIView):

    def get(self, request):

        try:
            unique_branch_ids = Order.objects.exclude(branchId__isnull=True).values_list('branchId', flat=True).distinct()

            data = {"branches": list(unique_branch_ids)}

            return ApiResponse(
                success=True,
                data=[data],
                status=status.HTTP_200_OK
            )
        except Order.DoesNotExist:
            data = {"branches": None}

            return ApiResponse(
                    success=True,
                    data=[data],
                    status=status.HTTP_200_OK
                )
