from flask import make_response
from flask.json import jsonify
from ..database.getConnection import get_connection
from . import routes

@routes.route('/tasks/<id>')
def get_task(id):
    """
        use:fetch a single task from database
        request parameter:task_id(int)
        method:GET
    """
    try:
        query='SELECT * FROM tasks WHERE id=?'
        task={}
        msg=''
        status_code=0
        conn=get_connection()
        row=conn.execute(query,(id,)).fetchone()
        if row:
            task={
                'id':row[0],
                'task_title':row[1],
                'task_details':row[2],
                'created_at':row[3]
            }
            msg='task found'
            status_code=200
        else:
            msg='task not found'
            status_code=404
    except Exception as err:
        print('exception in get_task',err)
        msg='task not found'
        status_code=404
    finally:       
        return make_response(jsonify({'message':msg,'task':task}),status_code)


