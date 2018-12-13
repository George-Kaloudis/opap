Modules
=======

get_bundles()
^^^^^^^^^^^^^

The module get_bundles() returns all the bundles curently on sale in Humble Bundle.
The returned value is a dictionary that contains: the name of the bundles as the key and the url as the value
(Both are strings).

get_items(bundle, bundle_url)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The module get_items() returns the price levels and items of a specific bundle.
The returned value is a list that contains: the name of the bundle as the 0th element.
Every other element is a list with the price as the 0th element and the contained items as the 1st element.