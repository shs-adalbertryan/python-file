#!/opt/cloudera/parcels/Anaconda/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Robert (Bob) L. Jones'
__coauthor__ = 'N/A'
__copyright__ = 'Copyright 2018, File'
__credits__ = ['Robert (Bob) L. Jones']
__license__ = 'GPL'
__version__ = '0.0.1'
__maintainer__ = 'Robert (Bob) L. Jones'
__status__ = 'Development'
__created_date__= 'Dec 5, 2018'
__modified_date__= 'Dec 5, 2018'

'''
FILE
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
file.py

SYNOPSIS
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
File(subpath1[, subpath2, ..., extension=extension, dir=dir])

DESCRIPTION
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
The class "File":
* Encapulates file metadata;
* Handles file operations.

EXAMPLES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
from file import File

file1 = File('file1.csv', dir='~')
print("TEST 1a: file1.name=%s" % file1.name)
print("TEST 1b: file1.stem=%s" % file1.stem)
print("TEST 1c: file1.parent=%s" % file1.parent)
print("TEST 1d: file1.suffix=%s" % file1.suffix)
print("TEST 1e: file1=%s" % file1)
print("")

file2 = File('file2', extension='.csv', dir='.')
print("TEST 2a: file2.name=%s" % file2.name)
print("TEST 2b: file2.stem=%s" % file2.stem)
print("TEST 2c: file2.parent=%s" % file2.parent)
print("TEST 2d: file2.suffix=%s" % file2.suffix)
print("TEST 2e: file2=%s" % file2)
print("")

file3 = File('file3', extension='.json.jinja', dir='.')
print("TEST 3a: file3.name=%s" % file3.name)
print("TEST 3b: file3.stem=%s" % file3.stem)
print("TEST 3c: file3.parent=%s" % file3.parent)
print("TEST 3d: file3.suffix=%s" % file3.suffix)
print("TEST 3e: file3=%s" % file3)

file4 = File('file4.json.jinja', extension='.json.jinja', dir='.')
print("TEST 4a: file4.name=%s" % file4.name)
print("TEST 4b: file4.stem=%s" % file4.stem)
print("TEST 4c: file4.parent=%s" % file4.parent)
print("TEST 4d: file4.suffix=%s" % file4.suffix)
print("TEST 4e: file4=%s" % file4)

file5 = File('../etc/file5.json.jinja', extension='.json.jinja', dir='.')
print("TEST 5a: file5.name=%s" % file5.name)
print("TEST 5b: file5.stem=%s" % file5.stem)
print("TEST 5c: file5.parent=%s" % file5.parent)
print("TEST 5d: file5.suffix=%s" % file5.suffix)
print("TEST 5e: file5=%s" % file5)

file6 = File('../etc/file6.json.jinja', dir='.')
print("TEST 6a: file6.name=%s" % file6.name)
print("TEST 6b: file6.stem=%s" % file6.stem)
print("TEST 6c: file6.parent=%s" % file6.parent)
print("TEST 6d: file6.suffix=%s" % file6.suffix)
print("TEST 6e: file6=%s" % file6)

file7a = File('../etc/file7.json', dir='.')
file7b = File(file7a.name, extension='.jinja', dir=file7a.parent)
print("TEST 7a: file7b.name=%s" % file7b.name)
print("TEST 7b: file7b.stem=%s" % file7b.stem)
print("TEST 7c: file7b.parent=%s" % file7b.parent)
print("TEST 7d: file7b.suffix=%s" % file7b.suffix)
print("TEST 7e: file7b=%s" % file7b)

REFERENCES
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1. https://codereview.stackexchange.com/questions/162426/subclassing-pathlib-path
2. https://cpython-test-docs.readthedocs.io/en/latest/library/pathlib.html
3. https://github.com/bc-python/mistool/blob/master/mistool/os_use.py
4. https://github.com/chris1610/pbpython/blob/master/extras/Pathlib-Cheatsheet.pdf
5. https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
6. https://realpython.com/python-pathlib/
7. https://spyhce.com/blog/understanding-new-and-init
8. https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
'''

### Libraries ###

# 3rd-party

#from pathlib import Path, _windows_flavour, _posix_flavour
from pathlib import Path

# Custom


### Class Declaration ###

class File(type(Path())):
    '''
    This class:
        * Encapulates file metadata;
        * Handles file operations.
    
    Properties:
        All properties are inherited as is from the parent class "Path".
        
    Return (object):
        An uninitialized 'File' class instance.
    '''

    # '__new__' is the constructor and exists solely for creating the object.
    def __new__(cls, *args, **kwargs):
        
        '''
        The initializer for the class 'File' that exists solely for creating the object.
        
        Args:
            args: A comma-separated list of arguments representing parts of path
            kwargs: An optional comma-separated list of key/value pairs
        
        Return (object):
            An initialized 'File' class instance.
        '''

        extension = kwargs.get('extension', '') # The file's extension (e.g., ".csv")
        dir = kwargs.get('dir', '')             # The path (absolute or relative) of the file's parent directory

        name = args[-1]
        name_part = name.split('/')[-1] or name.split('\\')[-1]
        name_parts = name_part.split('.')
        name_extension = '.' + '.'.join(name_parts[1:len(name_parts)])
        
        new_name = name if extension == '' or extension == name_extension else name + extension
        
        return super(File, cls).__new__(cls, dir, new_name, **kwargs)


if __name__ == '__main__':
    #pass
    
    print('UNIT TESTS:')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('')
    
    file1 = File('file1.csv', dir='~')
    print("file1 = File('file1.csv', dir='~')")
    print("TEST 1a: file1.name=%s" % file1.name)
    print("TEST 1b: file1.stem=%s" % file1.stem)
    print("TEST 1c: file1.parent=%s" % file1.parent)
    print("TEST 1d: file1.suffix=%s" % file1.suffix)
    print("TEST 1e: file1=%s" % file1)
    print("")
    
    file2 = File('file2', extension='.csv', dir='.')
    print("file2 = File('file2', extension='.csv', dir='.')")
    print("TEST 2a: file2.name=%s" % file2.name)
    print("TEST 2b: file2.stem=%s" % file2.stem)
    print("TEST 2c: file2.parent=%s" % file2.parent)
    print("TEST 2d: file2.suffix=%s" % file2.suffix)
    print("TEST 2e: file2=%s" % file2)
    print("")
    
    file3 = File('file3', extension='.json.jinja', dir='.')
    print("file3 = File('file3', extension='.json.jinja', dir='.')")
    print("TEST 3a: file3.name=%s" % file3.name)
    print("TEST 3b: file3.stem=%s" % file3.stem)
    print("TEST 3c: file3.parent=%s" % file3.parent)
    print("TEST 3d: file3.suffix=%s" % file3.suffix)
    print("TEST 3e: file3=%s" % file3)
    print("")
    
    file4 = File('file4.json.jinja', extension='.json.jinja', dir='.')
    print("file4 = File('file4.json.jinja', extension='.json.jinja', dir='.')")
    print("TEST 4a: file4.name=%s" % file4.name)
    print("TEST 4b: file4.stem=%s" % file4.stem)
    print("TEST 4c: file4.parent=%s" % file4.parent)
    print("TEST 4d: file4.suffix=%s" % file4.suffix)
    print("TEST 4e: file4=%s" % file4)
    print("")
    
    file5 = File('../etc/file5.json.jinja', extension='.json.jinja', dir='.')
    print("file5 = File('../etc/file5.json.jinja', extension='.json.jinja', dir='.')")
    print("TEST 5a: file5.name=%s" % file5.name)
    print("TEST 5b: file5.stem=%s" % file5.stem)
    print("TEST 5c: file5.parent=%s" % file5.parent)
    print("TEST 5d: file5.suffix=%s" % file5.suffix)
    print("TEST 5e: file5=%s" % file5)
    print("")
    
    file6 = File('../etc/file6.json.jinja', dir='.')
    print("file6 = File('../etc/file6.json.jinja', dir='.')")
    print("TEST 6a: file6.name=%s" % file6.name)
    print("TEST 6b: file6.stem=%s" % file6.stem)
    print("TEST 6c: file6.parent=%s" % file6.parent)
    print("TEST 6d: file6.suffix=%s" % file6.suffix)
    print("TEST 6e: file6=%s" % file6)
    print("")
    
    file7a = File('../etc/file7.json', dir='.')
    file7b = File(file7a.name, extension='.jinja', dir=file7a.parent)
    print("file7a = File('../etc/file7.json', dir='.')")
    print("file7b = File(file7a.name, extension='.jinja', dir=file7a.parent)")
    print("TEST 7a: file7b.name=%s" % file7b.name)
    print("TEST 7b: file7b.stem=%s" % file7b.stem)
    print("TEST 7c: file7b.parent=%s" % file7b.parent)
    print("TEST 7d: file7b.suffix=%s" % file7b.suffix)
    print("TEST 7e: file7b=%s" % file7b)
    print("")
