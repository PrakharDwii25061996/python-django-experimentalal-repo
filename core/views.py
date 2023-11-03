from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("Prakhar Dwivedi")


def master_function(request):
	return HttpResponse("Master Branch")

def second_function_develop_branch(request):
	return HttpResponse("Second function develop branch")

def third_function_develop(request):
	return HttpResponse("third function develop.")

def function_incorrect_commmit_branch(request):
	return HttpResponse("Function Incorrect branch.")

