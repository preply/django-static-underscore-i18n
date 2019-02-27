from __future__ import with_statement

import io
import os

import django
from django.core.management.base import BaseCommand
from django.utils.translation import to_locale
from django.utils.encoding import force_text
from staticunderscorei18n.conf import settings
from staticunderscorei18n.utils import get_filename
from staticunderscorei18n.render import js_templates


class Command(BaseCommand):
    help = "Collect Javascript catalog files in a single location."
    requires_system_checks = False

    def add_arguments(self, parser):
        parser.add_argument('--locale', '-l', dest='locale',
                            help="The locale to process. Default is to process all."),
        parser.add_argument('-o', '--output', dest='outputdir', metavar='OUTPUT_DIR',
                            help="Output directory to store generated catalogs. "
                                 "Defaults to static/jsunderscorei18n.")

    def handle(self, **options):
        domain = settings.STATIC_UNDERSCORE_TEMPLATES_DOMAIN
        templates = settings.STATIC_UNDERSCORE_TEMPLATES
        context = settings.STATIC_UNDERSCORE_CONTEXT
        locale = options.get('locale')
        outputdir = options.get('outputdir')
        verbosity = int(options.get('verbosity'))

        if locale is not None:
            languages = [locale]
        elif django.VERSION < (1, 10):
            languages = [to_locale(lang_code)
                         for (lang_code, lang_name) in settings.LANGUAGES]
        else:
            languages = [lang_code for (lang_code, lang_name) in settings.LANGUAGES]

        if outputdir is None:
            outputdir = os.path.join(settings.STATIC_UNDERSCORE_I18N_ROOT,
                                     settings.STATIC_UNDERSCORE_I18N_OUTPUT_DIR)

        for locale in languages:
            if verbosity > 0:
                self.stdout.write("processing language %s\n" % locale)

            jsfile = os.path.join(outputdir, get_filename(locale, domain))
            basedir = os.path.dirname(jsfile)
            if not os.path.isdir(basedir):
                os.makedirs(basedir)
            response = js_templates(locale, templates, context)
            with io.open(jsfile, "w", encoding="utf-8") as fp:
                fp.write(force_text(response.content))
