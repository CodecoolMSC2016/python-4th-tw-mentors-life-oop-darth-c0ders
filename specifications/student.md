# Student

## Description
This class represents a student in real life. It should inherit all properties from the Person class, but also has some other functionalities.
You can find more details at our Trello site. (https://trello.com/b/82EL1p6I/mentors-life).


## Parent class
Person

## Attributes

* ```knowledge level```
  * data type: integer
  * description: knowledge level of students
* ```energy level```
  * data type: integer
  * description: energy level of students

## Instance methods

### ```__init__```

The class should have a constructor, which calls the Person's constructor, but also set's the attributes above (should raise an error, if any is empty).

### ```create_by_csv```

The class should have a method called create_by_csv, which gets a csv file path as an argument (the csv contains all the data needed to instantiate a student object) and gives back a list of students.

### ```fire_student```

This method check students' knowledge and energy level, and if values under 0, students are fired from CodeCool.