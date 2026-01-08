# ============================================================
# general idea here is to give the widgets on the front end
# an "updater" that the algorithm can change as needed during the
# animation. 
# an updater is supposed to have the update() function that the 
# widget calls during a paintEvent when widget is updated.
# this way the algorithm can specify how to update the visuals 
# which is particular only to the algorithm.
# ============================================================