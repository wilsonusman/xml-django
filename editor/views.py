from django.views.generic import TemplateView


class EditorPageView(TemplateView):
    template_name = "editor.html"
