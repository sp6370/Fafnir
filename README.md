# Fafnir
A minimalistic key-value database implemented in C.

### Database Assumptions

#### Temporary Assumptions
- Key is always valid
- Key contains ASCII alphabet characters only
- Values are always integers

#### Implementation assumptions
- Data is stored in a single txt file
- Key value paris are stored int the format: key=value
- Each line in the file contains a single key value pair