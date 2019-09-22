from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Company
from .forms import CompanyForm


class CompanyCreate(CreateView):
    """ View to add a new company to the database """
    model = Company
    form_class = CompanyForm
    template_name = "company/company_add.html"


class CompanyList(ListView):
    """ View to list all existing Companies """
    model = Company
    template_name = "company/company_list.html"
    extra_context = {
        'page_title': "Company - TableView",
    }
    paginate_by = 5


class CompanyDetail(DetailView):
    """ View to get details about a company """
    model = Company
    template_name = "company/company_detail.html"


class CompanyUpdate(UpdateView):
    """ View to update a companies data """
    model = Company
    template_name = "company/company_update.html"
    form_class = CompanyForm
    success_url = reverse_lazy('company:company-list')


class CompanyDelete(DeleteView):
    """ View to delete an existing company """
    model = Company
    success_url = reverse_lazy('company:company-list')
