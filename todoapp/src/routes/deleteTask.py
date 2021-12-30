from flask import request,make_response
from flask.json import jsonify
from ..database.getConnection import get_connection
from . import routes

@routes.route('/tasks/delete',methods=['post'])
def delete_task():
    """
        use:delete a task in database
        request body:{task_id(int)}
        method:POST
    """
    try:
        if request.is_json:
            id=request.json.get('task_id')
            query='DELETE FROM tasks WHERE id=?'
            conn=get_connection()
            conn.execute(query,(id,))
            conn.commit()
            msg='task deleted successfully'
            status_code=200
        else:
            msg='please send json request'
            status_code=400
    except Exception as err:
        print('exception in delete_task:',err)
        msg='cannot delete task'
        status_code=400
    finally:
        return make_response(jsonify({'message':msg}),status_code)
