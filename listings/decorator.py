from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def is_landlord(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request,
                "Please login to access this page.",
                extra_tags="danger",
            )
            return redirect("login")

        # Check superuser before checking user_type
        if request.user.is_superuser:
            messages.error(
                request,
                "Admin accounts cannot access this landlord page.",
                extra_tags="danger",
            )
            return redirect("/admin/")

        if request.user.user_type != "landlord":
            messages.error(
                request,
                "You do not have permission to access this page.",
                extra_tags="danger",
            )
            return redirect("home")

        return view_func(request, *args, **kwargs)

    return wrapper


# def is_landlord(view_func):
#     @wraps(view_func)
#     def wrapper(request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             if request.user.user_type == 'landlord':
#                 return view_func(request, *args, **kwargs)
#             elif request.user.user_type == 'tenant':
#                 messages.error(request, 'You do not have permission to access this page.', extra_tags='danger')
#                 return redirect('home')
#             elif request.user.is_superuser:
#                 messages.error(request,"Login as admin to access this page", extra_tags='danger')
#                 return redirect('admin:index')
#         else:
#             messages.error(request, 'Please login to access this page.', extra_tags='danger')
#             return redirect('home')
#     return wrapper
