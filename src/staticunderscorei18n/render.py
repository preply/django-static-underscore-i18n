from django.http import HttpRequest
from django.template.context import RequestContext
from django.template import loader
from django import http
from django.utils.html import escapejs
from django.utils.translation import activate

def js_templates(templates, language):
    compiled_js = ""
    request = HttpRequest()
    context = RequestContext(request, {})
    activate(language)
    for (name, template) in templates.iteritems():
        text = loader.get_template(template_name=template).render(context)
        compiled_js += "var %s = '%s';\r\n" % (name, escapejs(text))
    return http.HttpResponse(compiled_js, 'text/javascript')
