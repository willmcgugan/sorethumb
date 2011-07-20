Django Integration
==================

To use Sore Thumb in Django, add "sorethumb" to your list of INSTALLED_APPS in `settings.py`. This is required to expose the `sorethumb` filter to template -- no models or views are included.

Add {% load sorethumb %] to the top of any template that requires the sorethumb filter.