# 3. CALLING CRUD OPERATIONS
from database import db, Puppy

# CREATE
my_puppy = Puppy('Rufus', 3)
db.session.add(my_puppy)
db.session.commit()


# READ
all_puppies = Puppy.query.all() # reports back the list of puppy objects in table
print(all_puppies)

# SELECT
puppy_one = Puppy.query.get(1) # selects puppy by id
print(puppy_one.name)

# FILTERS
# PRODUCES SOME SQL CODE
puppy_frankie = Puppy.query.filter_by(name = 'Frankie')
print(puppy_frankie.all())
# ['Frankie' is '1' years old] -> reports back result in our __repr__() form

# UPADATE
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

# DELETE
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)
