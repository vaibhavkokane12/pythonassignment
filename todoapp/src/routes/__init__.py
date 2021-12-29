from flask import Blueprint
routes=Blueprint('routes',__name__)

from .getTasks import *
from .addTask import *
from .deleteTask import * 
from .findTask import *
from .updateTask import *