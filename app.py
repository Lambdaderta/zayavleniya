from flask import Flask, render_template, session, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'ключик_секретик'


def create_db():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('''DROP TABLE IF EXISTS parent''')
    cur.execute('''DROP TABLE IF EXISTS teacher''')
    cur.execute('''DROP TABLE IF EXISTS class''')
    cur.execute('''DROP TABLE IF EXISTS children''')
    cur.execute('''DROP TABLE IF EXISTS statements''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS parent (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
        )
        ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS teacher (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        subject TEXT NOT NULL
        )
        ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS class (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        class_name TEXT NOT NULL UNIQUE,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teacher (id)
        )
        ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS children (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        parent_id INTEGER,
        class_id INTEGER,
        child_name TEXT NOT NULL,
        FOREIGN KEY (parent_id) REFERENCES parent (id),
        FOREIGN KEY (class_id) REFERENCES class (id)
        )
        ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS statements (
        state_id INTEGER PRIMARY KEY AUTOINCREMENT,
        statement TEXT,
        parent_id INTEGER,
        child_id INTEGER,
        FOREIGN KEY (parent_id) REFERENCES parent (id),
        FOREIGN KEY (child_id) REFERENCES children (id)
        )
        ''')

    cur.execute('''CREATE INDEX idx_parent_username ON parent (username)''')
    cur.execute('''CREATE INDEX idx_statements_statement ON statements (statement)''')
    cur.execute('''CREATE INDEX idx_parent_email ON parent (email)''')
    cur.execute('''CREATE INDEX idx_teacher_username ON teacher (username)''')
    cur.execute('''CREATE INDEX idx_teacher_email ON teacher (email)''')
    cur.execute('''CREATE INDEX idx_class_name ON class (class_name)''')
    cur.execute('''CREATE INDEX idx_children_parent_id ON children (parent_id)''')
    cur.execute('''CREATE INDEX idx_children_class_id ON children (class_id)''')
    cur.execute('''CREATE INDEX idx_statements_parent_id ON statements (parent_id)''')
    cur.execute('''CREATE INDEX idx_statements_child_id ON statements (child_id)''')

    conn.commit()
    conn.close()



@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def reg():
    if request.method=="POST":
        account_type = request.form.get('account_type')
        if account_type == "teacher":
            name = request.form.get('full_name')
            email = request.form.get('email')
            password = request.form.get('password')
            subject = request.form.get('subject')

            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            cur.execute('''
                INSERT INTO teacher (username, email, password, subject)
                VALUES (?, ?, ?, ?)
                ''', (name, email, password, subject))
            conn.commit()
            conn.close()

            return redirect(url_for('home'))
        else:
            name = request.form.get('full_name')
            email = request.form.get('email')
            password = request.form.get('password')
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            cur.execute('''
                INSERT INTO parent (username, email, password)
                VALUES (?, ?, ?)
                ''', (name, email, password))
            conn.commit()
            conn.close()
            return redirect(url_for('home'))
        
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        account_type = request.form.get('account_type')
        if account_type == "teacher":
            name = request.form.get('full_name')
            email = request.form.get('email')
            password = request.form.get('password')
            subject = request.form.get('subject')

            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM teacher WHERE email = ? and password = ?", (email, password))
            user = cur.fetchone()
            conn.close()

            if user:
                session["account_type"] = account_type
                session["name"] = name
                session["subject"] = subject
                session['user_id'] = user[0]
            else:
                return redirect(url_for('login'))
            return redirect(url_for("home"))
        elif account_type == "parent":
            name = request.form.get('full_name')
            email = request.form.get('email')
            password = request.form.get('password')

            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM parent WHERE email = ? and password = ?", (email, password))
            user = cur.fetchone()
            conn.close()

            if user:
                session["account_type"] = account_type
                session["name"] = name
                session['user_id'] = user[0]
            else:
                return redirect(url_for('login'))
            return redirect(url_for("home"))
        else:
            return redirect(url_for('login'))
    return render_template("login.html")
    
if __name__=="__main__":
    create_db()
    app.run(debug=True)