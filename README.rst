django-static-underscorei18n
=================

.. image:: https://travis-ci.org/zyegfryed/django-statici18n.png?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/zyegfryed/django-statici18n

.. image:: https://coveralls.io/repos/zyegfryed/django-statici18n/badge.png?branch=master
  :target: https://coveralls.io/r/zyegfryed/django-statici18n?branch=master

A Django app that provides helper for compiling underscore templates to static
files.

Overview
--------

This repo an project is forked from ``django-statici18n`` 
`github.com/zyegfryed/django-staticunderscorei18n`_ to tackle the problem of compiling of Underscore templates to single static js file.
The original code was generating static js files for translations.

That's what ``django-static-underscore-i18n`` is for:

    Collecting JavaScript catalogs from each of your Django apps (and any other
    place you specify) into a single location that can easily be served in
    production.


.. _javascript_catalog view: https://docs.djangoproject.com/en/1.6/topics/i18n/translation/#module-django.views.i18n
.. _adding an overhead: https://docs.djangoproject.com/en/1.6/topics/i18n/translation/#note-on-performance
.. _github.com/zyegfryed/django-statici18n: https://github.com/zyegfryed/django-statici18n

Installation
------------

1. Use your favorite Python packaging tool to install ``django-staticunderscorei18n``
   from `PyPI`_, e.g.::

    pip install django-staticunderscorei18n

2. Add ``'statici18n'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = [
        # ...
        'staticunderscorei18n',
    ]

3. Once you have edited your underscore .html templates or `translated`_ and `compiled`_ your messages, use the
   ``compilejsunderscorei18n`` management command::

    python manage.py compilejsunderscorei18n

4. Check that the ``django.core.context_processors.i18n`` context processor is added to your
   ``TEMPLATE_CONTEXT_PROCESSORS`` setting - should have already been set by
   Django. This is needed to resolve request.LANGUAGE_CODE variable during compilation phase::

    TEMPLATE_CONTEXT_PROCESSORS = (
      # ...
      'django.core.context_processors.i18n',
    )

5. Edit your template(s) and insert .js files those were compiled. Good practice is to serve static files without django server (you can you nginx for that):

  .. code-block:: html+django

    <script src="{{ STATIC_URL }}jsunderscorei18n/{{ LANGUAGE_CODE }}/underscore_templates.js"></script>

.. note::

    By default, the generated catalogs are stored to ``STATIC_ROOT/jsunderscorei18n``.
    You can modify the output path and more options by tweaking
    ``django-staticunderscorei18n`` settings.

.. _PyPI: http://pypi.python.org/pypi/django-staticunderscorei18n
.. _translated: https://docs.djangoproject.com/en/1.6/topics/i18n/translation/#message-files
.. _compiled: https://docs.djangoproject.com/en/1.6/topics/i18n/translation/#compiling-message-files