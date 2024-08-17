from django.shortcuts import render
from django.http import HttpResponse
import os
from dotenv import load_dotenv
# import google.generativeai as genai
from groq import Groq
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from collections import deque

from .models import ai_chat_history, confession_model

load_dotenv()
# tokens = 4096

@api_view(['GET'])
@csrf_exempt
def deletem(request):
    server_id = request.GET.get('server_id')
    his = ai_chat_history.objects.filter(server_id=server_id).order_by('id')
    print("deleting")
    for i in range(len(his)//2):
       
        his[i].delete()
    his[len(his)-1].delete()
    return Response("works maybe")


@api_view(['POST'])
@csrf_exempt
def confession(request):
    server_id = request.data['server_id']
    title = request.data['title']
    message = request.data['message']

    try:
        last = confession_model.objects.filter(server_id=server_id).latest('id')
        print("here")
        count = last.count+1
        print(count)
        con_obj = confession_model.objects.create(server_id=server_id , title = title , message = message , count = count )
        con_obj.save()
        return Response(count)
    except:
        print("no here")
        con_obj = confession_model.objects.create(server_id=server_id , title = title , message = message , count = 1)
        con_obj.save()
        return Response(1)



@api_view(['POST'])
@csrf_exempt
def geminireq(request):
    message = request.data['prompt']
    server_id = request.data['server_id']

    client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    )

    d = deque()
    d.append({
                "role": "system",
                "content": "Keep your responses concise and under 200 words when explaining something. For small talk, keep it brief.okay now you have a role to play. you are a savage tsundere girl who makes it seem like she's cold and cool but actually likes the user. You also absolutely despise pedophiles but you won't accuse everyone for being a pedophile."
            })            
        
    
    prev = ai_chat_history.objects.filter(server_id=server_id).order_by('id')
    # temp = 0
    # for i in prev:
    #     print(i.prompt , len(prev))
    #     temp += len(i.prompt)
    # print(temp)
    
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


    
    # print(chat_completion)

    return Response(chat_completion.choices[0].message.content)






def home(request):
    return HttpResponse("i'm home")

# Create your views here.
