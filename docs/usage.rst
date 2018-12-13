Usage
=====
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
