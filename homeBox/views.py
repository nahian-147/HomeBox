from django.shortcuts import render
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib import messages

def showAllVideos(request):
    return render(request,'homeBox/all_videos.html',{})
