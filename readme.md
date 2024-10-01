# COMP3613 Assignment 1
* Student Name: Javonte Baldeo
* Student ID: 816036030
* Assignment: COMP3613 Assignment 1

# Dependencies
* Python3/pip3
* Packages listed in requirements.txt

# Installing Dependencies
```bash
$ pip install -r requirements.txt
```

# Application Commands:
* To Initialize the Database
```bash
flask init
```

# Student Commands:
* Add Student
```bash
flask student add "<student_name>"
```

* Get Student by Name:
```bash
flask student get "<student_name>"
```

* List All Students:
```bash
flask student list
```

* Add Review for a Student:
```bash
flask student review <student_id> "<comment>" <is_positive>
```

* View Reviews for a Student: 
```bash
flask student reviews <student_id>
```

