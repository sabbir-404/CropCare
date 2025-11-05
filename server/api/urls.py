from django.urls import path
from .views import ping, InferView, tips, detections, weather, air

urlpatterns = [
    path("ping/", ping),
    path("infer/", InferView.as_view()),
    path("tips/", tips),
    path("detections/", detections),
    path("weather/", weather),
    path("air/", air),
]
