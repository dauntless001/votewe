from django.http import JsonResponse
from django.shortcuts import redirect, render
from poll import models, forms
from django.contrib import messages
# Create your views here.

def home(request):
    if request.is_ajax():
        id = request.GET['id']
        lga = models.LGA.objects.get(lga_id = id)
        polling_units = models.PollingUnit.objects.filter(lga__lga_id=lga.lga_id).values_list('id', flat=True)
        results = models.Result.objects.filter(polling_unit__id__in=polling_units)
        parties = models.Party.objects.all()
        result_list = []
        for party in parties:
            prs = results.filter(party=party)
            party_result = sum([pr.score for pr in prs])
            data = [party.name, party_result]
            result_list.append(data)
        return JsonResponse({"data":tuple(result_list)})
    context = {
        'units' : models.PollingUnit.objects.all(),
        'LGAs': models.LGA.objects.all()
    }
    return render(request, 'index.html', context)

def new_polling_unit(request):
    form = forms.PollingUnitForm()
    if request.POST:
        form = forms.PollingUnitForm(request.POST)
        parties = request.POST.getlist('parties')
        if form.is_valid():
            pu = form.save()
            index = 0
            for party in models.Party.objects.all():
                models.Result.objects.create(polling_unit=pu, party=party, 
                    entered_by=pu.entered_by, score=parties[index])
                index+=1
            messages.success(request, 'Polling Unit Created Successfully')
        return redirect('home')
    context = {
        'form' : form,
        'parties' : models.Party.objects.all()
    }
    return render(request, 'new.html', context)