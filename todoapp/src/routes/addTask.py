from flask import request,make_response
from flask.json import jsonify
from ..database.getConnection import get_connection
from . import routes

@routes.route('/tasks/add',methods=['post'])
def add_task():
    """
        use:insert a task into database
        request body:{task_title(string),task_details(string)}
        method:POST
    """
    try:
        if request.is_json:
            task_title=request.json.get('task_title')
            task_details=request.json.get('task_details')
            query='INSERT INTO tasks(task_title,task_details) VALUES(?,?)'
            conn=get_connection()
            conn.execute(query,(task_title,task_details))
            conn.commit()
            msg='task added successfully'
            status=201
        else:
            msg='please send json request'
            status=400
    except Exception as err:
        print('exception in add_task function:',err)
        msg='cannot add task'
        status=400
    finally:
        return make_response(jsonify({'message':msg}),status)
