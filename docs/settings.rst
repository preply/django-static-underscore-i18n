Settings
========

.. currentmodule:: django.conf.settings


.. attribute:: STATICI_UNDERSCORE_18N_PACKAGES

    :default: ``('django.conf')``

    A list of packages to check for translations.

    Can be overrided with the ``-p/--package`` option of :ref:`compilejsunderscorei18n`
    command.

    Each string in packages should be in Python dotted-package syntax (the
    same format as the strings in ``INSTALLED_APPS``) and should refer to a
    package that contains a locale directory. If you specify multiple
    packages, all those catalogs are merged into one catalog. This is useful
    if you have JavaScript that uses strings from different applications.

.. attribute:: STATIC_UNDERSCORE_TEMPLATES_DOMAIN

    :default: ``underscore_templates``
    filename of generated static js file.

.. attribute:: STATIC_UNDERSCORE_TEMPLATES

    :default: ``{}``

    Dictionary of variables/template name bindings. Example:
    .. code-block:: django
    {
        STATIC_UNDERSCORE_TEMPLATES = {
        'popup_template': '_templates/popup.html',
    }
    .. note::


.. attribute:: STATIC_UNDERSCORE_I18N_ROOT

    :default: ``STATIC_ROOT``

    Controls the file path that catalog files will be written into.


.. attribute:: STATIC_UNDERSCORE_CONTEXT

    :default: ``{}``

    Context to render _templates

.. attribute:: STATICI_UNDERSCORE_I18N_OUTPUT_DIR

    :Default: ``'underscore_templates'``

    Controls the directory inside :attr:`STATIC_UNDERSCORE_I18N_ROOT` that generated files
    will be written into.

.. attribute:: STATIC_UNDERSCORE_I18N_FILENAME_FUNCTION

    :default: ``'staticunderscorei18n.utils.default_filename'``

    The dotted path to the function that creates the filename.

    The function receives two parameters:

    * ``locale``: a string representation of the locale currently processed

    * ``domain``: a string representation of the gettext domain used to check
      for translations

    By default, the function returns the path ``'<language_code>/<domain>.js'``.

    The final filename is resulted by joining :attr:`STATIC_UNDERSCORE_I18N_ROOT`,
    :attr:`STATIC_UNDERSCORE_I18N_OUTPUT_DIR` and :attr:`STATIC_UNDERSCORE_I18N_FILENAME_FUNCTION`.

    For example, with default settings in place and ``STATIC_ROOT = 'static'``, the JavaScript catalog
    generated for the ``en_GB`` locale is: ``'static/jsunderscorei18n/en-gb/underscore_templates.js'``
