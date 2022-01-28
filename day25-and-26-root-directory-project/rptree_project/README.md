#  A Directory Tree Generator Tool in Python
* **Create a CLI application with Python’s argparse**
* **Recursively traverse a directory structure using pathlib**
* **Generate, format, and display a directory tree diagram**
* **Save the directory tree diagram to an output file**
##### Organizing the Code:
* **Provide the CLI**
* **Walk the root directory and build the tree diagram**
* **Display the tree diagram**

##### The tree diagram will have two main components:
**Head** will provide the root directory representation.
**Body** will provide the directory content representation.

##### Output
```
$ python tree.py --help
usage: tree [-h] [-v] [-d] [-o [OUTPUT_FILE]] [ROOT_DIR]

RP tree, a directory tree generator

positional arguments:
  ROOT_DIR              Generate a full directory tree starting the root
                        directory

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d, --dir-only        Generate a irectory-tree only
  -o [OUTPUT_FILE], --output-file [OUTPUT_FILE]
                        Generate a full directory tree and save it to a file

Thanks for using RP Tree!
```
```
$ python tree.py hello
hello\
│
├──hello
│   ├──hello.py
│   └──__init__.py
│
├──tests
│   ├──unit
│   │   ├──unit_test.py
│   │   └──__init__.py
│   │
│   └──test_hello.py
│
├──LICENSE
├──README.md
├──requirements.txt
└──setup.py
```
```
$ python .\tree.py -d
.\
│
├──hello
│   ├──hello      
│   │
│   └──tests      
│       └──unit   
│
│
│
└──rptree
    └──__pycache__
```
```
$ python tree.py hello -o output_file.md
```
Reference: [Real Python](https://realpython.com/directory-tree-generator-python/)