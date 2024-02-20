from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from peststagram.common.forms import CommentForm
from peststagram.pests.models import Pest
from peststagram.pests.forms import PestAddForm, PestEditForm, PestDeleteForm


class AddPestView(CreateView):
    model = Pest
    form_class = PestAddForm
    template_name = 'pests/pest_add_page.html'
    success_url = reverse_lazy('details_user', kwargs={"pk": 1})


# def add_pest(request: HttpRequest) -> HttpResponse:
#     form = PestAddForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("details_user", pk=1)
#
#     context = {
#         "form": form,
#     }
#     return render(request, "pests/pest_add_page.html", context=context)

class DetailsPestView(DetailView):
    model = Pest
    template_name = "pests/pest_details_page.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["all_photos"] = self.object.tagged_pets.all()
        context["comment_form"] = CommentForm()
        return context


# def details_pest(request: HttpRequest, username: str, slug: str) -> HttpResponse:
#     try:
#         pest = Pest.objects.get(slug=slug)
#         all_photos = pest.tagged_pests.all()
#         comment_form = CommentForm()
#         context = {
#             "pest": pest,
#             "all_photos": all_photos,
#             "comment_form": comment_form,
#         }
#         return render(request, "pests/pest_details_page.html", context=context)
#
#     except Pest.DoesNotExist:
#         return redirect(request.META["HTTP_REFERER"])


# def edit_pest(request: HttpRequest, username: str, slug: str) -> HttpResponse:
#     try:
#         pest = Pest.objects.get(slug=slug)
#         form = PestEditForm(request.POST or None, instance=pest)
#         if form.is_valid():
#             form.save()
#             redirect("details_user", username=username, pest_slug=slug)
#
#         else:
#             context = {
#                 "form": form,
#                 "username": username,
#                 "slug": slug,
#             }
#             return render(request, "pests/pest_edit_page.html", context)
#
#     except Pest.DoesNotExist:
#         return redirect(request.META["HTTP_REFERER"])


class EditPestView(UpdateView):
    model = Pest
    form_class = PestEditForm
    template_name = "pests/pest_edit_page.html"

    def get_success_url(self) -> str:
        return reverse_lazy(
            "details_user",
            kwargs={
                "username": self.kwargs["username"],
                "slug": self.kwargs["slug"],
            }
        )


# def delete_pest(request: HttpRequest, username: str, slug: str) -> HttpResponse:
#     try:
#         pest = Pest.objects.get(slug=slug)
#         form = PestDeleteForm(request.POST or None, instance=pest)
#         if request.method == "POST":
#             form.save()
#             return redirect("home")
#
#         else:
#             context = {
#                 "form": form,
#                 "username": username,
#                 "pest": pest,
#             }
#         return render(request, "pests/pest_delete_page.html", context=context)
#
#     except Pest.DoesNotExist:
#         return redirect(request.META["HTTP_REFERER"])


class DeletePestView(DeleteView):
    model = Pest
    form_class = PestDeleteForm
    template_name = "pests/pest_delete_page.html"
    success_url = reverse_lazy(
        "details_user",
        kwargs={
            "pk": 1,
        }
    )

    def get_object(self, queryset=None) -> Pest:
        return Pest.objects.get(slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = PestDeleteForm(initial=self.object.__dict__)
        return context

    def delete(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        pest = self.get_object()
        pest.delete()
        return redirect(self.success_url)
