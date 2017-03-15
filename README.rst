django-admin-gitlog
===================

*Display a `git log` in your admin*

To install, :code:`pip3 install django-admin-gitlog`

And then add it to your :code:`INSTALLED_APPS`

.. code:: python

    INSTALLED_APPS = [
        # ...
        'admin_gitlog',
    ]


How it works: It simply overrides the default `admin.index_template` to add the info


.. image:: https://raw.githubusercontent.com/mdamien/django-admin-gitlog/master/screenshot.png
    :target: https://github.com/mdamien/django-admin-gitlog/master/screenshot.png
    :alt: Screenshot
