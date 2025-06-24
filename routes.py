from flask import Blueprint, request, jsonify, redirect, current_app
from models import URL
from extensions import db

main = Blueprint('main', __name__)

@main.route('/shorten', methods=['POST'])
def shorten_url():
    try:
        # Check if request has JSON data
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400
            
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({'error': 'URL is required'}), 400
            
        original_url = data['url']
        
        # Basic URL validation
        if not original_url.startswith(('http://', 'https://')):
            original_url = 'https://' + original_url
        
        # Check if URL already exists
        existing_url = URL.query.filter_by(original_url=original_url).first()
        if existing_url:
            return jsonify({'short_url': request.host_url + existing_url.short_url})

        # Generate unique short URL with safety limit
        short_url = URL.generate_shortUrl()
        attempts = 0
        max_attempts = 10
        
        while URL.query.filter_by(short_url=short_url).first() and attempts < max_attempts:
            short_url = URL.generate_shortUrl()
            attempts += 1
            
        if attempts >= max_attempts:
            return jsonify({'error': 'Unable to generate unique short URL'}), 500
        
        # Create and save new URL
        new_url = URL(original_url=original_url, short_url=short_url)
        db.session.add(new_url)
        db.session.commit()

        return jsonify({'short_url': request.host_url + short_url})
    
    except Exception as e:
        current_app.logger.error(f"Error in shorten_url: {str(e)}")
        db.session.rollback()
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@main.route('/<short_url>')
def redirect_to_url(short_url):
    try:
        current_app.logger.info(f"Attempting to redirect to short URL: {short_url}")
        
        # Execute the query properly
        url_object = URL.query.filter_by(short_url=short_url).first()
        
        if url_object:
            current_app.logger.info(f"Redirecting to original URL: {url_object.original_url}")
            return redirect(url_object.original_url)
        else:
            current_app.logger.info(f"URL not found: {short_url}")
            return jsonify({'error': 'URL not found'}), 404
            
    except Exception as e:
        current_app.logger.error(f"Error in redirect_to_url: {str(e)}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@main.route('/')
def home():
    return jsonify({
        'message': 'Welcome to URL Shortener',
        'endpoints': {
            'shorten': '/shorten (POST)',
            'redirect': '/<short_url> (GET)'
        }
    })

@main.route('/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200
