import ducks

flock = ducks.Flock()
donald = ducks.Duck()
daisy = ducks.Duck()
duck3 = ducks.Duck()
duck4 = ducks.Duck()
duck5 = ducks.Duck()
duck6 = ducks.Duck()
duck7 = ducks.Duck()
percy = ducks.Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(percy)  # error as penguin object has no attribute fly
flock.add_duck(duck5)  # other 3 remained grounded, unable to fly, only 4 ducks fly
flock.add_duck(duck6)  # error is shown in different places, gets passed to call stack until something handles it or reaches runtime
flock.add_duck(duck7)

flock.migrate()
