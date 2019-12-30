# Django mail template

Application to create mails templates with context variables and then send mails
with context variables replaced with values. Mails templates are created with
 *Django admin interface*.

For example, if context variables are: *first_name* and *last_name*, while
cycling a collection of people (clients, providers, and like) is possible to
send a mail to each of them using their first name and last name to replace
the context variables in each mail.

Also a double mapping between a mail template and process configuration make
possible to change the used mail template in a process at run time from admin 
GUI. 

For example, two mail template are created: one with christmas greeting text
and subject, and other mail template with the same but for new year greeting.
Then the same process (code) used in upper example can be used to send
christmas and new year greeting to all people. 

Change which mail template is used by which process at *Django admin
interface* (or make your own views).

#### Works with:

* Django 1.10+ (Python 3.5+)

* Django 2+ (Python 3.5+)

* Django 3+ (Python 3.5+)

* [Documentation](https://django-roles-access.github.io)


## Requirements


Django mail template needs *Django admin interface* to create mails templates
and to map mails templates with process. Requirements for *Django admin
interface* can be checked at the
[official documentation:](https://docs.djangoproject.com/en/dev/ref/contrib/admin/)


## Quick start


### Installation and configuration


1. Install **django_mail_template** from pypi:
```
    pip install django-mail-template
```

2. Add **'django_mail_template'** to your INSTALLED_APPS setting:
```    
    INSTALLED_APPS = [
        ...
        'django_mail_template',
    ]
```
    
3. Run migrations to create **django_mail_template** models:
```
    python manage.py migrate
```


Code example

```
    from django_roles_access.mixin import RolesMixin

    class MyView(RolesMixin, View):

        ...
```

>Note example:
>
>   When user has no access to a view, by default **django_roles_access**
>   response with *django.http.HttpResponseForbidden*.

>Warning example:
>
>   Pre existent security behavior can be modified if a **django_roles_access**
>   configuration for the same view results in a more restricted view access.


## Test Django mail template

You can check the **django_mail_template** test execution at 
[Travis CI integration](https://travis-ci.org/django-roles-access/master)
([![Build Status](https://travis-ci.org/django-roles-access/master.svg?branch=master)](https://travis-ci.org/django-roles-access/master))

You can also check **django_mail_template** test coverage at
[Coverage](https://django-roles-access.github.io/coverage.html)
([![codecov](https://codecov.io/gh/django-roles-access/master/branch/master/graph/badge.svg)](https://codecov.io/gh/django-roles-access/master))


## Related sites

* [Documentation](https://django-roles-access.github.io)

* [Package at pypi.org](https://pypi.org/project/django-roles-access/)

* [source code](https://github.com/django-roles-access/master)

* [Travis CI integration](https://travis-ci.org/django-roles-access/master)

* [Codecov](https://codecov.io/gh/django-roles-access/master)

