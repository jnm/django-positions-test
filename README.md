django-positions-test
=====================

Demonstration of django-positions issue when using a ModelForm that does not
contain the position field.

The superuser in the database has username `a` and password `a`.

After starting `manage.py runserver`, access http://localhost:8000/silly/1 and
observe that the `position` is 0. The `position` field is not part of the form.
Submit the form and notice that `position` has changed to 3.
