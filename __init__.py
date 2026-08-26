"""HubBase Architecture v2 is here!

To extend on the new architecture create a project with this file structure:

{name}/
| __init__.py
| Programs/
|| {id}/
||| main.py
|| ... \n

__init__.py must define an all_programs list.
Each main.py must have a run method.
"""
from .Programs import all_programs

