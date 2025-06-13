from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD']
    )
    return conn

@app.route('/user', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        first_name = data['first_name']
        last_name = data['last_name']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING id;',
            (first_name, last_name)
        )
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({'id': user_id, 'first_name': first_name, 'last_name': last_name}), 201
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, first_name, last_name FROM users WHERE id = %s;', (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user:
        return jsonify({'id': user[0], 'first_name': user[1], 'last_name': user[2]})
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
