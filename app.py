from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import os

app = Flask(__name__)
# Absolute path to db to avoid issues when running from different dirs
DATABASE = os.path.join(os.path.dirname(__file__), 'kidguard.db')
SCHEMA = os.path.join(os.path.dirname(__file__), 'schema.sql')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with open(SCHEMA, mode='r', encoding='utf-8') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def dashboard():
    db = get_db()
    children = db.execute('SELECT * FROM child').fetchall()
    stats = []
    for c in children:
        devices = db.execute('SELECT * FROM device WHERE child_id = ?', (c['id'],)).fetchall()
        total_time = 0
        for d in devices:
            res = db.execute('SELECT SUM(duration) as td FROM activity WHERE device_id = ?', (d['id'],)).fetchone()
            if res and res['td']:
                total_time += res['td']
        
        # Calculate app limit progress logic purely for UI presentation
        max_limit = sum(d['screen_time_limit'] for d in devices) if devices else 1
        percentage = min(100, int((total_time / max_limit) * 100)) if max_limit > 0 else 0
        
        stats.append({
            'child': c, 
            'devices': devices, 
            'total_time': total_time,
            'max_limit': max_limit,
            'percentage': percentage
        })
    return render_template('dashboard.html', stats=stats)

@app.route('/time_limits', methods=['GET', 'POST'])
def time_limits():
    db = get_db()
    if request.method == 'POST':
        device_id = request.form['device_id']
        new_limit = request.form['limit']
        school_mode = 1 if 'school_mode' in request.form else 0
        db.execute('UPDATE device SET screen_time_limit = ?, school_mode = ? WHERE id = ?', (new_limit, school_mode, device_id))
        db.commit()
        return redirect(url_for('time_limits'))
    
    devices = db.execute('SELECT d.*, c.name as child_name, c.avatar as avatar FROM device d JOIN child c ON d.child_id = c.id').fetchall()
    return render_template('time_limits.html', devices=devices)

@app.route('/reports')
def reports():
    db = get_db()
    activities = db.execute('''
        SELECT a.app_name, SUM(a.duration) as total_duration, c.name as child_name, c.avatar as avatar 
        FROM activity a 
        JOIN device d ON a.device_id = d.id 
        JOIN child c ON d.child_id = c.id
        GROUP BY a.app_name, c.name
        ORDER BY total_duration DESC
    ''').fetchall()
    return render_template('reports.html', activities=activities)

@app.route('/toggle_lock/<int:device_id>', methods=['POST'])
def toggle_lock(device_id):
    db = get_db()
    current = db.execute('SELECT is_locked FROM device WHERE id = ?', (device_id,)).fetchone()
    new_status = 0 if current['is_locked'] else 1
    db.execute('UPDATE device SET is_locked = ? WHERE id = ?', (new_status, device_id))
    db.commit()
    return redirect(url_for('dashboard'))

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/settings')
def settings():
    db = get_db()
    blocked = db.execute('SELECT * FROM blocked_site').fetchall()
    return render_template('settings.html', blocked=blocked)

@app.route('/add_block', methods=['POST'])
def add_block():
    url = request.form.get('url')
    if url:
        db = get_db()
        db.execute('INSERT INTO blocked_site (url) VALUES (?)', (url,))
        db.commit()
    return redirect(url_for('settings'))

@app.route('/delete_block/<int:id>', methods=['POST'])
def delete_block(id):
    db = get_db()
    db.execute('DELETE FROM blocked_site WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('settings'))

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        print("Initializing database...")
        init_db()
    print("Starting KidGuard server...")
    app.run(debug=True, port=5000)
