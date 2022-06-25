from django.urls import path
from .views import Indexview,Details, Results, Vote
app_name='polls'
urlpatterns=[
    path('', Indexview,name='home'),
    path('<int:pk>/details/',Details,name='details'),
    path('<int:pk>/results/',Results,name='results'),
    path('<int:pk>/vote/',Vote,name='vote')
]