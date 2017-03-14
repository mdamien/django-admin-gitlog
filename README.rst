django-admin-gitlog
===================

*Display a `git log` in your admin*

To install, :code:`pip3 install django-admin-gitlog`

And then add it to your :code:`INSTALLED_APPS`

.. code:: python

    INSTALLED_APPS = [
        # your have to put this first
        'admin_gitlog',

        'django.contrib.admin',
        # ...
    ]


How it works: I replace the `AdminSite` with a custom one and do a `git log -n 5`


.. image:: https://raw.githubusercontent.com/mdamien/django-admin-gitlog/master/screenshot.png
    :target: https://github.com/mdamien/django-admin-gitlog/master/screenshot.png
    :alt: Screenshot