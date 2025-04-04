# this file is manually Created
from django.urls import path
from .import views
urlpatterns = [
    path('exams/',views.exam_view),
    path('attendance/',views.attendance_view),
    path('fees/',views.fees_view),
]   

# Not Exexuting this we are import into the another urls



# In kunalproject folder we can not Create an app only copy the app into the applevelurlsprojet 
# into and paste  the kunalproject 

# copy the testapp into the kunalproject folder and code reusability is  there 
