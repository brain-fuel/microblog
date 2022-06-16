from app import app

@app.route('/')
@app.route('/index')
def index():
    user = ['username': 'Matt']
    return '''
<html>
    <head>
        <title>Hope Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
'''
