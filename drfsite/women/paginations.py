from rest_framework.pagination import PageNumberPagination


class WomenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'  # http://127.0.0.1:8000/api/v1/women/?offset=2&page=2&page_size=4
    max_page_size = 10_000  # max value for page_size
