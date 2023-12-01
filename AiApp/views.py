from django.shortcuts import render
from AiApp.models import Visual
import openai

# Create your views here.
def home(request):
    openai.api_key = "Your OpenAI API"
    if request.method == "POST":
        text = request.POST.get("prompt")
        visual = Visual(prompt=text)
        visual.save()
        response = openai.Image.create(
            prompt=text,
            n=1,
            size='1024x1024'
        )

        image_url = response["data"][0]["url"]
        visual_dict = {
            "url": image_url
        }
        return render(request, "index.html", visual_dict)
    return render(request, "index.html")

def custom_404(request, exception):
    return render(request, '404.html', status=404)
