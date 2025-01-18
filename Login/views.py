from flask import render_template, request, redirect, url_for, session, flash, make_response
from . import login_blueprint

@login_blueprint.route('/', methods=['GET', 'POST'])
def login():
    if 'user' in session:  # Redirect to dashboard if already logged in
        return redirect(url_for('login.dashboard'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Simple authentication (replace with actual logic)
        if username == 'admin' and password == 'password':
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('login.dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
            
    response = make_response(render_template('login.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    return response
    

@login_blueprint.route('/dashboard')
def dashboard():
    if 'user' not in session:  # Ensure user is logged in
        flash('Please log in first.', 'warning')
        return redirect(url_for('login.login'))
    return render_template('dashboard.html')


@login_blueprint.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login.login'))
