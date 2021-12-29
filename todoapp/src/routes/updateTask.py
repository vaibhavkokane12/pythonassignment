from flask import request,make_response
from flask.json import jsonify
from ..database.getConnection import get_connection
from . import routes
@routes.route('/tasks/update',methods=['post'])
def update_task():
    """
        use:update a task in database
        request body:{task_id(int),task_title(string),task_details(string)}
        method:POST
    """
    try:
        if request.is_json:
            task_id=request.json.get('task_id')
            task_title=request.json.get('task_title')
            task_details=request.json.get('task_details')
            query='UPDATE tasks SET task_title=?,task_details=? WHERE id=?'
            conn=get_connection()
            conn.execute(query,(task_title,task_details,task_id))
            conn.commit()
            msg='task updated successfully'
            status_code=200
        else:
            msg='please send json request'
            status_code=400
    except:
        print('exception in update_task')
        msg='cannot update task'
        status_code=400
    finally:
        return make_response(jsonify({'message':msg}),status_code)
