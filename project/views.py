from django.shortcuts import render


def home_view(request):
    # if 'user' in request.session:
    # current_user = request.session['user']
    # param = {'current_user': current_user}
    return render(request, 'index.html')
    # else:
    #     return redirect('login')
    # return render(request, 'index.html')
