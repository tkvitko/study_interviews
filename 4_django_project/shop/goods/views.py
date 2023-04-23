from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .models import Good
from .forms import GoodForm


def list_view(request):
    context = {"goods": Good.objects.all()}
    return render(request, "goods_list.html", context)


def create_good(request):
    data = dict()
    if request.method == "POST":
        good_form = GoodForm(request.POST)
        if good_form.is_valid():
            good_form.save()
            data['form_is_valid'] = True
            goods = Good.objects.all()
            data['products_html'] = render_to_string('goods_list.html', {'goods': goods})
            # messages.success(request, 'Your good was successfully added!')
        else:
            # messages.error(request, 'Error saving form')
            data['form_html'] = render_to_string('form.html', {'form': good_form}, request=request)
        # return redirect("goods")
    else:
        data['form_is_valid'] = False
        data['form_html'] = render_to_string('form.html', {'form': GoodForm()}, request=request)

    return JsonResponse(data)


# def save_good_form(request, form, template_name):
#     data = dict()
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             data['form_is_valid'] = True
#             goods = Good.objects.all()
#             data['html_good_list'] = render_to_string('good_list.html', {
#                 'goods': goods
#             })
#         else:
#             data['form_is_valid'] = False
#     context = {'form': form}
#     data['html_form'] = render_to_string(template_name, context, request=request)
#     return JsonResponse(data)
