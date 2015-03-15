from django.shortcuts import render


def b_test(request):
    return render(request,
                  'b_test.html',
                  {})