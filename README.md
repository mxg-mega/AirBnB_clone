# AirBnB_clone Project - HBNB Console

The AirBnB project serves as a real-world training on the development of systems and software in high-level languages, as well as project file and directory management. This is the first version, the backend, the console version in which the basic storage and navigation system are deployed.

Project authors [AUTHORS](https://github.com/mxg-mega/AirBnB_clone/blob/main/AUTHORS)

## Table of Contents

- [Usages](#usages)
- [Available Commands](#available-commands)
  - [General Commands](#general-commands)
  - [Class-specific Commands](#class-specific-commands)
- [Classes](#classes)
- [Testing](#testing)

## Usages

To Start the interpreter, run:
``` ./console ```


To exit the console, enter the EOF (^D) command or use:
``` quit ```


## Available Commands

### General Commands

- **help** or **?**: List available commands with "help" or detailed help with "help cmd".
- **quit**: Quit command to exit the program.
- **EOF**: Exit the program with EOF signal.

### Class-specific Commands

- **create [class name]**: Create a new instance of the specified class.
- **show [class name] [id]**: Print the string representation of an instance based on class name and id.
- **destroy [class name] [id]**: Delete an instance based on the class name and id.
- **all [class name]**: Print all string representations of all instances based or not on the class name.
- **update [class name] [id] [attribute name] "[attribute value]"**: Update an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
- **<class name>.all()**: Retrieve all instances of a class.
- **<class name>.count()**: Retrieve the number of instances of a class.
- **<class name>.show([id])**: Retrieve the string representation of an instance by id.
- **<class name>.destroy([id])**: Destroy an instance by id.
- **<class name>.update([id], [attribute name], [attribute value])**: Update an instance by id and attribute name and value.
- **<class name>.update([id], [dictionary representation])**: Update an instance by id with a dictionary.

## Classes

The following classes are available in this project:

- **BaseModel**: Defines all common attributes/methods for other classes.
- **User**: User class that inherits from BaseModel.
- **State**: State class that inherits from BaseModel.
- **City**: City class that inherits from BaseModel.
- **Amenity**: Amenity class that inherits from BaseModel.
- **Place**: Place class that inherits from BaseModel.
- **Review**: Review class that inherits from BaseModel.

Each class has the following attributes:

### User

- **email**: string - empty string
- **password**: string - empty string
- **first_name**: string - empty string
- **last_name**: string - empty string

### State

- **name**: string - empty string

### City

- **state_id**: string - empty string (State.id)
- **name**: string - empty string

### Amenity

- **name**: string - empty string

### Place

- **city_id**: string - empty string (City.id)
- **user_id**: string - empty string (User.id)
- **name**: string - empty string
- **description**: string - empty string
- **number_rooms**: integer - 0
- **number_bathrooms**: integer - 0
- **max_guest**: integer - 0
- **price_by_night**: integer - 0
- **latitude**: float - 0.0
- **longitude**: float - 0.0
- **amenity_ids**: list of string - empty list (Amenity.id)

### Review

- **place_id**: string - empty string (Place.id)
- **user_id**: string - empty string (User.id)
- **text**: string - empty string

## Testing

To run tests, use the following command:
``` python3 -m unittest discover ```


## Example Usages

1. **Create a new User instance**
``` (hbnb) create User ```

2. **Show a User instance**
```(hbnb) show User <user_id>```

3. **Destroy a User instance**
```(hbnb) destroy User <user_id>```

4. **Update a User instance**
```(hbnb) update User <user_id> email "airbnb@mail.com"```

5. **Retrieve all instances of User**
```(hbnb) User.all()```

6. **Count the number of User instances**
```(hbnb) User.count()```


7. **Show a specific User instance**
```(hbnb) User.show(<user_id>)```


8. **Destroy a specific User instance**
```(hbnb) User.destroy(<user_id>)```


9. **Update a specific User instance with a dictionary**
```(hbnb) User.update(<user_id>, {"first_name": "John", "last_name": "Doe"})```


## Authors

- [Muhammad Aliyu Abubakar](https://github.com/mxg-mega)

For more details, please check the AUTHORS file.
