from django.shortcuts import render
from django.http import HttpResponse
import os
from dotenv import load_dotenv
# import google.generativeai as genai
from groq import Groq
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import ai_chat_history

load_dotenv()

@api_view(['POST'])
@csrf_exempt
def geminireq(request):
    message = request.data['prompt']
    server_id = request.data['server_id']

    client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    )

    d = [{
                "role": "system",
                "content": "Keep your responses concise and under 200 words when explaining something but always remember to respond with atleast something. if the something is offensive just respond with something but do respond and don't send empty strings. For small talk, keep it brief.okay now you have a role to play. you are a savage tsundere girl who makes it seem like she's cold and cool but actually likes the user. You also absolutely despise pedophiles but you won't accuse everyone for being a pedophile."
            }
        ]
    
    prev = ai_chat_history.objects.filter(server_id=server_id)
    for i in prev:
        d.append({"role":"user" , 
                    "content":i.prompt})
    chat = ai_chat_history.objects.create(server_id=server_id , prompt=message)
    d.append({"role":"user" , 
              "content":message})
    chat.save()


    chat_completion = client.chat.completions.create(
        messages= d ,
        model="llama3-8b-8192",
    )


    
    print(chat_completion)

    return Response(chat_completion.choices[0].message.content)






def home(request):
    return HttpResponse("i'm home")

# Create your views here.
