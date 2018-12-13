Modules
=======

Arguments
^^^^^^^^^
Following values for specific arguments

game : "super3", "extra5", "proto", "lotto", "kino" and "joker" (String)

id : int

dstart, dend (date functions) : String YYYY-MM-DD (example: 2018-05-23)

startid, endid (id functions): Int

def get_last_draw(game)
^^^^^^^^^^^^^^^^^^^^^^^

The get_last_draw(game) returns the results of the last draw from the chosen game.
The returned value is a list, except if the chosen game is joker or lotto in which it's a tuple (Nlist(list), Extra(int)).

get_draw_from_id(game, id)
^^^^^^^^^^^^^^^^^^^^^^^^^^

The get_draw_from_id(game, id) returns the results from a specific draw with the id from the chosen game.
The returned value is a list, except if the chosen game is joker or lotto in which it's a tuple (Nlist(list), Extra(int)).

get_draw_from_id_range(game, startid, endid)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The get_draw_from_id_range(game, startid, endid) returns all the results from a specific id range from the chosen game.
The returned value is a list with each element being a tuple. The first element of the tuple is the draw id (int). The
second is the numbers list (list) and the third element is the extra number (int).

get_last_draws(game, n)
^^^^^^^^^^^^^^^^^^^^^^^

The get_last_draws(game, n) returns the results from the last n draws from the chosen game.
The returned value is a list with each element being a tuple. The first element of the tuple is the draw id (int). The
second is the numbers list (list) and the third element is the extra number (int).

get_draws_between(game, dstart, dend)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The get_draws_between(game, dstart, dend) returns the results from the draws between the specified dates from the chosen game.
The returned value is a list with each element being a tuple. The first element of the tuple is the draw id (int). The
second is the numbers list (list) and the third element is the extra number (int).

get_draw_ids_between(game, dstart, dend)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The get_draws_between_id(game, dstart, dend) returns the results from the draws between the specified ids from the chosen game.
The returned value is a list with each element being a tuple. The first element of the tuple is the draw id (int). The
second is the numbers list (list) and the third element is the extra number (int).

get_last_draw_id(game)
^^^^^^^^^^^^^^^^^^^^^^

The get_last_draw_id(game) returns the id (int) of the last draw.

get_active_draw_id(game)
^^^^^^^^^^^^^^^^^^^^^^^^

The get_active_draw_id(game) returns the id (int) of the last draw.