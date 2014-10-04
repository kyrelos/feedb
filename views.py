from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from feedb.models import*
from feedb.forms import*
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def main_page(request):
    company_list=Company.objects.all()
    return render(request,'feedb/main_page.html',{'company_list':company_list})


def feedback_page(request,cid):
    company=get_object_or_404(Company,pk=cid)
    
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            customer=Customer.objects.create(first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    phone_number=form.cleaned_data['phone_number'],
                    comment=form.cleaned_data['comment'],
                    company=company)
            return HttpResponseRedirect('/feedb/feedback_page/%d'%company.pk)

    else:
        form=FeedbackForm
##    return render(request, 'feedb/feedback_page.html', {'company':company,'form':form})
    variables=RequestContext(request,{'form':form,'company':company})
    return render_to_response('feedb/feedback_page.html', variables)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/feedb/')


@login_required(login_url='/feedb/accounts/login')
def staff_page(request,u):
    user= get_object_or_404(User, username=u)
    if u==request.user.username:
        if hasattr(user, 'employee'):
            company_list=user.employee.company.all()
            variables = RequestContext(request, {'company_list':company_list,'user':user})
            return render_to_response('feedb/staff_page.html',variables)
        else:
            return render(request,'feedb/staff_page.html')
##            return HttpResponseRedirect('PAGEDOESNOTEXIST')

    else:
        return HttpResponseRedirect('/feedb/logout')

def staff_redir(request):
    return HttpResponseRedirect('/feedb/user/staff/%s'%request.user)

    

