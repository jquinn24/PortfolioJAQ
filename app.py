from flask import Flask, render_template, request, jsonify, redirect, url_for
import os

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

@app.route('/')
def index():
    """Render the home page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page"""
    return redirect(url_for('index') + '#about')

@app.route('/projects')
def projects():
    """Render the projects page"""
    return redirect(url_for('index') + '#projects')

@app.route('/contact')
def contact():
    """Render the contact page"""
    return redirect(url_for('index') + '#contact')

@app.route('/api/send-message', methods=['POST'])
def send_message():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        # TODO: Add email sending functionality here
        # For now, just return success
        
        return jsonify({
            'success': True,
            'message': 'Message received! Thank you for reaching out.'
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Error processing your message.'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
