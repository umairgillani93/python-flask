# 2. SETTING UP FLASK DATABASE

from database import db, Puppy

db.create_all() # Transforms the Model class to the database table

sam = Puppy('Sam', 3) # Creating database entries
frank = Puppy('Frankie', 1)

# This will report back "None", since we haven't added these into our database yet
print(sam.id)
print(frank.id)

db.session.add_all([sam, frank])

db.session.commit() # commit the changes in the database

print(frank.id)
print(sam.id)
