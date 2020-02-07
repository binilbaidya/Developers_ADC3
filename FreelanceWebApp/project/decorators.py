from django.http import HttpResponse
from django.shortcuts import redirect

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:# if the user is authenticated user is redirected to project details
            return view_func(request, *args, **kwargs)
        else:
            return redirect('user:login')

    return wrapper_func

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:# if the user is authenticated user is redirected to project details
            return redirect('user:login')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
# def allowed_user(view_func):
#     def wrapper_func(project_id, request, *args, **kwargs):
#         project_obj = Project.objects.get(pk = project_id)
#         uid = request.user.id
#         pid = project_obj.user_id
#         if uid == pid:#if user id matches with project id then update page is shown
#             return view_func(request, *args, **kwargs)
#         else:
#             return redirect('project:project')

#     return wrapper_func