## argsparse library
### The Python argparse library:
* Allows the use of positional arguments
* Allows the customization of the prefix chars
* Supports variable numbers of parameters for a single option
* Supports subcommands (A main command line parser can use other command line parsers depending on some arguments.)

#### How to Use the Python argparse Library to Create a Command Line Interface
##### Using the Python argparse library has four steps:
* Import the Python argparse library
* Create the parser
* Add optional and positional arguments to the parser
* Execute .parse_args()

#### Setting the Name or Flags of the Arguments
There are basically two different types of arguments that you can add to your command line interface:
* Positional arguments
* Optional arguments

Positional arguments are the ones our command needs to operate.
Optional arguments are not mandatory, and when they are used they can modify the behavior of the command at runtime