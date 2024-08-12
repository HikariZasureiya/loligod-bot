from django.shortcuts import render
from django.http import HttpResponse
import os
from dotenv import load_dotenv
import google.generativeai as genai
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

load_dotenv()

@api_view(['POST'])
@csrf_exempt
def geminireq(request):
    message = request.data['prompt']
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
    history=[
    ]
    )

    response = chat_session.send_message(message)

    print(response.text)

    return Response(response.text)




def home(request):
    return HttpResponse("i'm home")

# Create your views here.
