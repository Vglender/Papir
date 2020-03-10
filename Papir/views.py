from django.template import Template, Context
from django.http import HttpResponse
def calc(request):
    t = Template(
'Стоимость 1 листа {{ cost_off_sheet }}'
 )
    c =Context({'cost_off_sheet' : 100})
    html = t.render(c)
    return HttpResponse(html)