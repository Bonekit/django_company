from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Company
from .forms import CompanyForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class CompanyCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """ View to add a new company to the database """
    model = Company
    form_class = CompanyForm
    template_name = "company/company_add.html"
    extra_context = {
        'page_title': "Company - Create Form",
    }
    raise_exception = True
    success_message = "Company created successfully"


class CompanyList(LoginRequiredMixin, ListView):
    """ View to list all existing Companies """
    model = Company
    template_name = "company/company_list.html"
    extra_context = {
        'page_title': "Company - List",
    }
    paginate_by = 10
    queryset = Company.objects.order_by('-brand')
    context_object_name = 'company_list'
    raise_exception = True


class CompanyDetail(LoginRequiredMixin, DetailView):
    """ View to get details about a company """
    model = Company
    template_name = "company/company_detail.html"
    extra_context = {
        'page_title': "Company - Details",
    }
    raise_exception = True
    context_object_name = 'company_single'


class CompanyUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """ View to update a companies data """
    model = Company
    template_name = "company/company_update.html"
    extra_context = {
        'page_title': "Company - Update Form",
    }
    form_class = CompanyForm
    raise_exception = True
    success_message = "Company updated successfully"


class CompanyDelete(LoginRequiredMixin, DeleteView):
    """ View to delete an existing company """
    model = Company
    template_name = "company/company_delete.html"
    context_object_name = 'company_single'
    raise_exception = True
    success_message = "Company was deleted successfully"
    success_url = reverse_lazy('company:company-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CompanyDelete, self).delete(request, *args, **kwargs)
