import mkpnHeader  # module for classes

# Objects
start = mkpnHeader.Menu()       # object of class menu, default menu
pidgley = mkpnHeader.Pidgley()  # object pidgley, enemy attacks
menu2 = mkpnHeader.Squittle()   # object menu2, call user's attacks
menu4 = mkpnHeader.Bag()        # object menu4, call bag items

# Lists
pg_life = pidgley.rtrn_val()  # get initial values for enemy values
sq_life = menu2.rtrn_val()    # get initial values for user's values
ap = sq_life[1]               # list of action points
sq_life = sq_life[0]          # slice off end of list; get rid of ap
items = menu4.rtrn_val()      # get item values

start.intro()  # Call introduction
start.welcome(pg_life, sq_life, items, ap)  # run through game

