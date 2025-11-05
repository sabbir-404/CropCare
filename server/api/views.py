from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# GET /api/ping/
def ping(request):
    return JsonResponse({"status": "ok", "message": "CropCare API is running!"})

# GET /api/tips/
def tips(request):
    demo = [
        "Inspect leaves weekly for spots or discoloration.",
        "Avoid overhead watering at night.",
        "Disinfect pruning tools between plants.",
    ]
    return JsonResponse({"tips": demo})

# GET /api/detections/
def detections(request):
    # Return recent detections; replace with real DB later
    sample = [
        {"id": 1, "label": "Leaf Blight", "confidence": 0.92, "severity": "moderate", "image": None},
        {"id": 2, "label": "Powdery Mildew", "confidence": 0.88, "severity": "low", "image": None},
    ]
    return JsonResponse(sample, safe=False)

# GET /api/weather/
def weather(request):
    # Mock now; plug your provider later
    return JsonResponse({"temp_c": 30, "humidity": 70, "uv_index": 8})

# GET /api/air/
def air(request):
    # Mock now; plug your provider later
    return JsonResponse({"pm25": 35, "pm10": 60, "aqi": 85})

@method_decorator(csrf_exempt, name="dispatch")  # remove if you switch to cookie auth+CSRF
class InferView(View):
    # POST /api/infer/   (multipart/form-data with 'image')
    def post(self, request, *args, **kwargs):
        image = request.FILES.get("image")
        if not image:
            return HttpResponseBadRequest("No image uploaded with key 'image'")
        # TODO: run your TensorFlow model here, e.g. model.predict(image)
        # Placeholder response:
        return JsonResponse({
            "label": "Leaf Blight",
            "confidence": 0.93,
            "severity": "moderate",
            "explain": "demo saliency/info here",
        })
