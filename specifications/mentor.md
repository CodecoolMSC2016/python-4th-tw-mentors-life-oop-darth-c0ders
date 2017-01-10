# Mentor

## Description
This class represents Mentors @ Codecool Miskolc.
You can find more details at our Trello site. (https://trello.com/b/82EL1p6I/mentors-life).


## Parent class
Person

## Attributes

* ```nickname```
  * data type: string
  * description: stores the mentor's secret nickname between the students)

## Instance methods

### ```__init__```

The class should have a constructor, which calls the Person's constructor, but also set's the nickname attribute (should raise an error, if empty).

### ```create_by_csv```

which gets a csv file path as an argument (the csv contains all the data needed to instantiate a mentor object) and gives back a list of mentors.
