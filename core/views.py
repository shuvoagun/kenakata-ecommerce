from django.shortcuts import render
from .models import *
from Store.models import SupportSection

# Create your views here.

def load_districts(request):
    division_id = request.GET.get('division_id')
    objs = District.objects.filter(division__id=division_id).order_by('name')
    return render(request, 'store/load_data/dropdown_list.html', {'objs': objs})


def load_sub_districts(request):
    district_id = request.GET.get('district_id')
    objs = SubDistrict.objects.filter(district__id=district_id).order_by('name')
    return render(request, 'store/load_data/dropdown_list.html', {'objs': objs})

def about(request):
    abouts = AboutUs.objects.all()
    services = SupportSection.objects.all().last()

    context = {
        'abouts':abouts,
        'services':services,
    }
    return render(request, 'store/about_us.html', context)



def faqs(request):
    faqs = faq.objects.all()
    
    context = {
        'faqs':faqs
    }
    return render(request, 'store/faq.html', context)



def terms_condition(request):
    TermsConditions = TermsCondition.objects.all()
    
    context = {
        'TermsConditions':TermsConditions
    }
    return render(request, 'store/terms-condition.html', context)



def privacy_policy(request):
    PrivacyPolicys = PrivacyPolicy.objects.all()
    
    context = {
        'PrivacyPolicys':PrivacyPolicys
    }
    return render(request, 'store/privacy-policy.html', context)