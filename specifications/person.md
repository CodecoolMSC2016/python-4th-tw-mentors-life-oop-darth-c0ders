# Person

## Description
This class represents a Person in real life, but we only use it to inherit it's features in Student and Mentor classes. 
You can find more details at our Trello site. (https://trello.com/b/82EL1p6I/mentors-life).


## Parent class
None

## Attributes

* ```first_name```
  * data type: string
  * description: first name of person
* ```last_name```
  * data type: string
  * description: last name of person
* ```year_of_birth```
   * data type: integer
   * description: birth date of person
* ```gender```
  * data type: string
  * description: gender of person

## Instance methods

### ```__init__```
The class should certainly have a constructor, which gets all the attributes above. It should raise an error, if any of the attributes is empty, and also if the provide gender is not valid