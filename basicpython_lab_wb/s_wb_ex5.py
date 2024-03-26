from flask import Flask, render_template, session, redirect, url_for, request


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Sample user data (replace with your authentication mechanism)
users = {
    'john_doe': {'role': 'student', 'name': 'John Doe'},
    'prof_smith': {'role': 'faculty', 'name': 'Professor Smith'},
}

@app.route('/')
def home():
    if 'username' in session:
        # Redirect to the appropriate profile based on the user's role
        return redirect(url_for('profile'))

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Replace this with your authentication mechanism
    if username in users and password == 'password':
        session['username'] = username
        return redirect(url_for('profile'))

    return render_template('login.html', error='Invalid username or password')

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('home'))

    username = session['username']
    user = users.get(username)

    if user['role'] == 'student':
        return render_template('student_profile.html', user=user)
    elif user['role'] == 'faculty':
        return render_template('faculty_profile.html', user=user)

    # Handle other roles as needed

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
