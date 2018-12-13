hbapi
========

hbapi is a basic api for the site Humble Bundle

Look how easy it is to use::

    import hbapi

    dict = hbapi.get_bundles()

    for bundle, bundle_url in dict.items():

        list = hbapi.get_items(bundle, bundle_url)
        print("Bundle Name:\n")
        print(list[0])
        print("\n")

        for item in list[1:]:
            print("Price: \n", item[0])
            print("Contains: \n", item[1])
            print("\n\n")

Features
--------

- Return the bundles in a dictionary
- Return the bundle's name, price levels and items

Installation
------------

Install hbapi by running::

    pip install hbapi

License
-------

The project is licensed under the MIT license.