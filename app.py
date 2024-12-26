from flask import Flask, render_template, session, redirect
import sqlite3

app = Flask(__name__)


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
def main():
    return render_template("index.html")

if __name__=="__main__":
    create_db()
    app.run(debug=True)