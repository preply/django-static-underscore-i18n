Management commands
===================

.. highlight:: console

.. _compilejsunderscorei18n:

compileunderscorejsi18n
-------------

Compile JavaScript Underscore templates files from templates to js file in a single location supporting i18n.

Some commonly used options are:

``-l LOCALE`` or ``--locale=LOCALE``
    The locale to process. Default is to process all.

``-o OUPUT_DIR`` or ``--output=OUTPUT_DIR``
    Output directory to store generated catalogs. Defaults to the joining path
    of :attr:`~django.conf.settings.STATIC_UNDERSCORE_I18N_ROOT` and
    :attr:`~django.conf.settings.STATIC_UNDERSCORE_I18N_OUTPUT_DIR`.

For a full list of options, refer to the ``compilejsi18n`` management command
help by running::

   $ python manage.py compilejsunderscorei18n --help


.. note::

    Missing directories will be created on-the-fly by the command when invoked.
