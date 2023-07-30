from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


from products.apis.serializers import *
from rest_framework import viewsets
from products.models import *


class CustomPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'page'




    def get_paginated_response(self, data):
        response = Response(data)
        response['count'] = self.page.paginator.count
        response['next'] = self.get_next_link()
        response['previous'] = self.get_previous_link()
        return response



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    pagination_class = CustomPagination