from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import News
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница сайта'
        return ctx


class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_queryset(self): # Изменить SQL запрос(чтоб выдавлись именно статьи одного автора)
        user = get_object_or_404(User, username=self.kwargs.get('username')) # Либо получаем <str:username> пользователя, либо ошибку 404
        return News.objects.filter(avtor=user).order_by('-date') # Получим статьи который avtor = равен автору в url статьи

    def get_context_data(self, **kwards):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)
        ctx['title'] = f'Статьи от пользователя {self.kwargs.get("username")}'
        return ctx


class NewsDetailView(DetailView):
    model = News
    template_name = 'blog/news_detail.html' # default= news_detail.html - так как news-model, detail-class
    # context_object_name = 'post' # default= object

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text', 'img_article']

    def form_valid(self, form): # При создании делает avtor который добавляет статью - это форма которая подставляет
        form.instance.avtor = self.request.user # request.user - это зарегистрированный на данный момент пользователь
        return super().form_valid(form) # form - это полученный сам автор

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text', 'img_article']

    def form_valid(self, form): # При создании делает avtor который добавляет статью - это форма которая подставляет
        form.instance.avtor = self.request.user # request.user - это зарегистрированный на данный момент пользователь
        return super().form_valid(form) # form - это полученный сам автор

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True

        return False


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete-news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True

        return False

    def get_context_data(self, **kwards):
        ctx = super(DeleteNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Удаление статьи'
        # ctx['title_text'] = News.objects.get(pk=self.kwargs['pk'])
        ctx['btn_text_yes'] = 'Удалить статью'
        ctx['btn_text_no'] = 'Не удалять статью'
        return ctx


def contacti(request):
    return render(request, 'blog/contacti.html', context={'title': "Страница контакты!"})