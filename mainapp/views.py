import json
import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView



class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        with open(os.path.join(os.getcwd() + '/mainapp/content/news.json')) as f:
            example_dict = json.load(f)

        context = super().get_context_data(**kwargs)
        context['news_title'] = 'Loud news title'
        context['news_preview'] = 'Description interesting for anyone'
        context['range'] = range(5)
        context['data_obj'] = datetime.now()
        context['some_news'] = example_dict
        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context['page_num'] = page
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"




