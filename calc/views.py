from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from django.views.generic import View
from .forms import OrderPreForm


def quantity(request):
    quantity = 100
    return render(request, 'calc/board_template.html', context = {'quantity' : quantity})

class OrderPre(View):
    def get (self, request):
        form = OrderPreForm()
        return render (request, 'calc/pre_order.html', context={'form' : form})

    def post (self, request):
        print()
        print(dir(request))
        print()
        print(request.POST)
        print()



        # bound_form = OrderPreForm(request.POST)
        # if bound_form.is_valid():
        #     new_pre_order = bound_form.save()
        #     print(new_pre_order)
        #     return redirect(new_pre_order)
        # return render(request, 'calc/pre_order.html', context={'form' : bound_form})