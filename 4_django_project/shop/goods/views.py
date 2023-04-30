from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Good
from .forms import GoodForm


def list_view(request):
    context = {"goods": Good.objects.all()}
    return render(request, "goods_list.html", context)


def create_good(request):
    if request.method == "POST":
        good_form = GoodForm(request.POST)
        if good_form.is_valid():
            good_form.save()
            messages.success(request, 'Your good was successfully added!')
        else:
            messages.error(request, 'Error saving form')
        return redirect("goods")
    else:
        good_form = GoodForm()
        # context = {"goods": Good.objects.all()}
        return render(request, "good_create.html", {"form": good_form})
