#from app.views import TodoListAndCreat, TodoDetailChangeAndDelete
from app.views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodoViewSet)

urlpatterns = router.urls


"""from django.urls import path

urlpatterns = [
    path('', TodoListAndCreat.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),
]"""