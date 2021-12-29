from flask.json import jsonify
from ..database.getConnection import get_connection
from . import routes
@routes.route('/tasks/')
def get_tasks():
    """
        use:fetch all tasks from database
        request body:none
        method:GET
    """
    try:
        query='SELECT * FROM tasks'
        tasks=[]
        conn=get_connection()
        result=conn.execute(query)
        for row in result:
            tasks.append({
                'id':row[0],
                'task_title':row[1],
                'task_details':row[2],
                'created_at':row[3]
            })
    except:
        print('exception in get_tasks')
    finally:
        return jsonify(tasks)
