from django.shortcuts import render
from django.http import HttpResponse

import git


def index(request):
	return HttpResponse("Prakhar Dwivedi")


def master_function(request):
	return HttpResponse("Master Branch")

def second_function_develop_branch(request):
	return HttpResponse("Second function develop branch")

def third_function_develop(request):
	return HttpResponse("third function develop.")

def incorrect_reset_command(request):
	return HttpResponse("incorrect_reset_command")


def git_display_function(request):
	repo = git.Repo('/home/psit09/Projects/demo-projects/experimental_repo')
	
	# get the current index
	# index = repo.index

	# List the files in the staging area
	# staged_files = [item.a_path for item in index.diff(None).iter_change_type('A')]

	print('Files in the staging area.')

	# for file in staged_files:
	# 	print(file)

	# print("Files in the unstaging area")

	# unstaged_files = [ item.a_path for item in index.diff(None).iter_change_type('D')]
	
	# for file in unstaged_files:
	# 	print(file)

	return HttpResponse("git_display_function")
