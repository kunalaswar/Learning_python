
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class MyPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'mypage' # this is for when you put  http://127.0.0.1:8000/api/?mypage=9 this page 9  is open for this we use 
    page_size_query_param = 'num' # todo - http://127.0.0.1:8000/api/?mypage=9&num=12 this is use for display how many number of record you want to display to this page 
    max_page_size = 15 
    last_page_strings = ('endpage') # http://127.0.0.1:8000/api/?mypage=endpage&num=15

#LimitOffsetPagination 
# 40 resourse start from 56th index(57th record )   
# meaning:
# limit : 40
# Offset :56
class MyPagination2(LimitOffsetPagination):
    default_limit = 15 #todo - this is for display the 15 record and start with http://127.0.0.1:8000/api/?offset=50
    # offset  = where you want to start 
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset' 
    max_limit = 20   # http://127.0.0.1:8000/api/?mylimit=20&myoffset=40


# To get all record of all employee acording to ascending order of emp salaries  but 5 per page
class MyPagination3(CursorPagination):
    ordering = 'esal' # '-esal'
    page_size = 5
    



