from django.shortcuts import render

def index(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email', '')
        if '@' in email:
            username, domain = email.split('@', 1)
            context['username'] = username
            context['domain'] = domain
            context['email'] = email
        else:
            context['error'] = "Please enter a valid email address."
    return render(request, 'slicer/index.html', context)
