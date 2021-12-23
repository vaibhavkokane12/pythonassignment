from flask import request,make_response
from flask.json import jsonify
from . import app
from .database.createDb import conn

@app.route('/tasks/add',methods=['post'])
def add_task():
    if request.is_json:
        task_title=request.json.get('task_title')
        task_details=request.json.get('task_details')
        query='INSERT INTO tasks(task_title,task_details) VALUES(?,?)'
        conn.execute(query,(task_title,task_details))
        conn.commit()
        return make_response(jsonify({'message':'task added successfully'}),201)
    else:
        return make_response(jsonify({'message':'please send json request',}),400)

@app.route('/tasks/')
def get_tasks():
    query='SELECT * FROM tasks'
    result=conn.execute(query)
    tasks=[]
    for row in result:
        tasks.append({
            'id':row[0],
            'task_title':row[1],
            'task_details':row[2],
            'created_at':row[3]
        })
    return jsonify(tasks)

@app.route('/tasks/<id>')
def get_task(id):
    query='SELECT * FROM tasks WHERE id=?'
    row=conn.execute(query,(id,)).fetchone()
    if row:
        task={
            'id':row[0],
            'task_title':row[1],
            'task_details':row[2],
            'created_at':row[3]
        }
        return jsonify(task)
    else:
        return make_response(jsonify({'message':'task not found'}),404)

@app.route('/tasks/update',methods=['post'])
def update_task():
    if request.is_json:
        task_id=request.json.get('task_id')
        task_title=request.json.get('task_title')
        task_details=request.json.get('task_details')
        query='UPDATE tasks SET task_title=?,task_details=? WHERE id=?'
        conn.execute(query,(task_title,task_details,task_id))
        conn.commit()
        return jsonify({'message':'task updated successfully'})
    else:
        return make_response(jsonify({'message':'please send json request',}),400)

@app.route('/tasks/delete',methods=['post'])
def delete_task():
    id=request.json.get('task_id')
    query='DELETE FROM tasks WHERE id=?'
    conn.execute(query,(id,))
    return jsonify({'message':'task deleted successfully'})