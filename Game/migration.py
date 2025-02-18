import ducks

flock = ducks.Flock()
donald = ducks.Duck()
daisy = ducks.Duck()
duck3 = ducks.Duck()
duck4 = ducks.Duck()
duck5 = ducks.Duck()
duck6 = ducks.Duck()
duck7 = ducks.Duck()
percy = ducks.Penguin()  # since Mallard and not Duck, add_duck treats as not duck and doesn't fly
# Penguin doesn't have fly method so getattr returns None and hence not added to flock
flock.add_duck(donald)
flock.add_duck(daisy)  # we can handle errors in many ways, first way is to do nothing XD
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(percy)  # error as penguin object has no attribute fly
flock.add_duck(duck5)  # other 3 remained grounded, unable to fly, only 4 ducks fly
flock.add_duck(duck6)  # error is shown in different places, gets passed to call stack until something handles it or reaches runtime
flock.add_duck(duck7)  # stack trace and output can be mixed up and hence output can't always be trusted
# often better to leave errors for something further up the call chain to deal with the error
flock.migrate()  # <module> means main program
# fly didn't handle error, propagated to flock (migrate) in main and that didn't handle it so it propagated to python runtime
# TODO: this is a todo
