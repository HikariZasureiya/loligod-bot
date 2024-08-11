from django.shortcuts import render
from django.http import HttpResponse
import os
import discord
from dotenv import load_dotenv
import random
from discord.ext import commands

def home(request):
    return HttpResponse("i'm home")

# Create your views here.
