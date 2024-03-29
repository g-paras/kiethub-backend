from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size=4
    page_query_param='p'
    page_size_query_param='count'
    max_page_size=20

