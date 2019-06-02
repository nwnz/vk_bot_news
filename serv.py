from flask import Flask, request, Response, render_template
import sqlite3 as lite
import json
import pickle
import sys
app = Flask(__name__)
def bd_request(qeury_string):
  data = ''
  con = None
  # qeury_string = '''
  #   SELECT *
  #   FROM users
  # '''
  try:
      con = lite.connect('base.sqlite')
      cur = con.cursor()
      cur.execute(qeury_string)
      con.commit()
      #con.rollback
      data = cur.fetchall()
      return data
  except Exception as e:
      print (e)
      sys.exit(1)
  finally:
      if con is not None:
          con.close()

def get_all_users():
  qeury_string = '''
    SELECT *
    FROM users
  '''
  request = bd_request(qeury_string)
  js = json.dumps(request)  
  return Response(js, status=200, mimetype='application/json')


def create_user():
  pass

def update_user(user_id):
  pass

def delete_user(user_id):
  pass

@app.route('/users', methods=['GET'])
def users():
  if request.method == 'GET':
    return get_all_users()
  else:
    print ('АШИПКА')
    

if __name__ == '__main__':
    app.run()



