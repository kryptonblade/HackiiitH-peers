from flask import Flask, render_template, request, jsonify, session, url_for
from flask_socketio import SocketIO, emit
import secrets
import sqlite3

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)  # Generate a random 32-character hexadecimal secret key
socketio = SocketIO(app)

@app.route('/index')
def index_page():
    print("uiavw")
    user_data = session.get('user_data', {})
    return render_template('index.html', user_data=user_data)
    # return render_template('index.html',session.get('user_data'))

@app.route('/user')
def user():
    # username = request.args.get('username', '')

    # # Find the user data for the given username
    # user_info = next((user for user in user_data if user['username'] == username), None)

    # if user_info:
    #     recipient_sid = user_info['sid']
    # else:
    #     recipient_sid = ''
    return render_template('user.html')

@app.route('/user_receiver')
def user_receiver():
    return render_template('user_receiver.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    # if request.method == 'POST':
    #     search_query = request.form.get('search_query')
    #     results = []

        
    #     for user in user_data:
    #         if search_query.lower() in [value.lower() for value in user.values()]:
    #             results.append(user)
    #     print(results)
    #     recipient_sid = results[0]['sid']
    #     # return jsonify(success=True)
    #     return render_template('search.html', recipient_sid=recipient_sid)
    user_data = session.get('user_data', {})
    return render_template('search.html',user_data=user_data)

conn = sqlite3.connect('example.db')
cur = conn.cursor()

# Define the SQL query to create a table (if it doesn't exist)
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    rollNumber INTEGER PRIMARY KEY,
    Handle TEXT NOT NULL,
    sid STRING NULLABLE,
    password TEXT NOT NULL
);
'''

# Execute the query to create the table
cur.execute(create_table_query)
conn.commit()

# Insert data into the table
insert_data_query = "INSERT INTO users (rollNumber, Handle, sid, password) VALUES (?, ?, ?, ?)"

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

        query = f"SELECT * FROM users WHERE rollNumber = {username}"


        with sqlite3.connect("example.db") as con:
            cur = con.cursor()
            cur.execute(query)
            user = cur.fetchone()
            con.commit()
        print(user)
        if user and user[3] == password:
            session['user_data'] = {
                'Handle': user[1],
                'rollNumber': user[0],
                'sid': user[2],
                'password': user[3]
            }
            print("hjib")
            # redirect_url = url_for('index.html', user_data=session.get('user_data'))
            return jsonify(success=True, redirect_url="/index")
        else:
            print("hi")
            # redirect_url = url_for('login.html', user_data=session.get('user_data'))
            return jsonify(success=True, redirect_url="/login")
    except Exception as e:
        print(e)
        # redirect_url = url_for('login.html', user_data=session.get('user_data'))
        return jsonify(success=True, redirect_url="/login")

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    print("hello")
    return render_template('signup.html')

@app.route('/signingup', methods=['POST'])
def signingup():
    print("hi")
    try:
        data = request.get_json()
        roll_number = data['rollNumber']
        codeforces_username = data['Handle']
        password = data['password']
        print("Hi", roll_number, codeforces_username, password)
        with sqlite3.connect("example.db") as con:
            cur = con.cursor()
            cur.execute(insert_data_query, (roll_number, codeforces_username, None,password))
            con.commit()

        # cursor.execute(insert_data_query, (roll_number, codeforces_username, password))
        # conn.commit()

        return jsonify(success=True)
    except Exception as e:
        print(e)
        return jsonify(success=False)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@socketio.on('connect')
def handle_connect():
    print(f'User connected')

@socketio.on('disconnect')
def handle_disconnect():
    print(f'User disconnected')

@socketio.on('send_message')
def handle_message(data):
    search_query = data['username']
    message = data['message']
    sock = data['socket_id']
    challenger = data['mainuser']
    print(search_query,message,sock)

    # if request.method == 'POST':
    # search_query = request.form.get('search_query')
    results = []


    # query2 = f'''UPDATE users SET sid={sock} WHERE rollNumber={search_query}'''
    query2 = "UPDATE users SET sid = ? WHERE rollNumber = ?"
    values = (sock, challenger)
    with sqlite3.connect("example.db") as con:
        cur = con.cursor()
        cur.execute(query2,values)
        # user_data = cur.fetchall()
        con.commit()

    query = f'''SELECT * FROM users WHERE rollNumber={search_query}'''
    # print("Hi", roll_number, codeforces_username, password)
    with sqlite3.connect("example.db") as con:
        cur = con.cursor()
        cur.execute(query)
        user_data = cur.fetchone()
        con.commit()
    # print(users[0])
    # for user in user_data:
    #     if search_query.lower() in [value.lower() for value in user.values()]:
    print(user_data)
    #         results.append(user)
    # print(results)
    # recipient_sid = results[0]['sid']
    # print(recipient_sid,message)
    emit('receive_message', {'message': message}, room=user_data[2])



@socketio.on('login')
def handle_login(data):
    socket_id = data.get('socket_id')
    print(f'Socket ID {socket_id} logged in')

@socketio.on('send_challenge')
def handle_challenge(data):
    challenger_username = int(data['mainUser'])
    recipient_username = data['username']
    message = data['message']
    print(challenger_username,recipient_username,message)
    print(type(challenger_username))
    query = f'''SELECT sid FROM users WHERE rollNumber = {recipient_username}'''
    with sqlite3.connect("example.db") as con:
        cur = con.cursor()
        cur.execute(query)
        user_data = cur.fetchone()
        con.commit()
    
    print(user_data)
    # You can implement additional logic here, such as checking if the recipient is online, etc.

    # Notify the recipient about the challenge request
    emit('receive_challenge', {'message': message, 'challenger_username': challenger_username}, room=user_data)

@socketio.on('accept_challenge')
def handle_accept_challenge(data):
    challenger_username = data['challenger_username']
    message = data['message']
    print(type(challenger_username))
    query = f'''SELECT sid FROM users WHERE rollNumber = {challenger_username}'''
    with sqlite3.connect("example.db") as con:
        cur = con.cursor()
        cur.execute(query)
        user_data = cur.fetchone()
        con.commit()
    
    print(user_data)
    # Notify the challenger that the challenge is accepted
    emit('challenge_status', {'status': 'accepted', 'message': message}, room=user_data)

    return render_template()

@socketio.on('reject_challenge')
def handle_reject_challenge(data):
    challenger_username = data['challenger_username']
    message = data['message']
    query = f'''SELECT sid FROM users WHERE rollNumber = {challenger_username}'''
    with sqlite3.connect("example.db") as con:
        cur = con.cursor()
        cur.execute(query)
        user_data = cur.fetchone()
        con.commit()
    
    print(user_data)
    # Notify the challenger that the challenge is rejected
    emit('challenge_status', {'status': 'rejected', 'message': message}, room=user_data)


# after response for request sent is received
    


# @socketio.on('send_request')
# def handle_request(data):
#     recipient_sid = data['recipient_sid']
#     sender_sid = request.sid
#     emit('receive_request', {'sender_sid': sender_sid}, room=recipient_sid)

# @socketio.on('accept_request')
# def handle_accept_request(data):
#     sender_sid = data['sender_sid']
#     emit('request_status', {'status': 'accepted'}, room=sender_sid)

# @socketio.on('decline_request')
# def handle_decline_request(data):
#     sender_sid = data['sender_sid']
#     emit('request_status', {'status': 'declined'}, room=sender_sid)



if __name__ == '__main__':
    socketio.run(app, debug=True)



