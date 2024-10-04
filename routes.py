from flask import Blueprint, request,jsonify,redirect, current_app
from models import URL
from app import db 

main = Blueprint('main', __name__)

@main.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json['url']
    existing_url = URL.query.filter_by(original_url=original_url).first()
    if existing_url:
        return jsonify({'short_url':request.host_url + existing_url.short_url})

    short_url = URL.generate_shortUrl()
    while URL.query.filter_by(short_url=short_url).first():
        short_url = URL.generate_shortUrl()
    
    new_url = URL(original_url=original_url, short_url=short_url)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({'short_url':request.host_url + short_url})

@main.route('/<short_url>')
def redirect_to_url(short_url):
    current_app.logger.info(f"Attempting to redirect to short URL: {short_url}")
    url_object = URL.query.filter_by(short_url=short_url) 
    if url_object:
        current_app.logger.info(f"Redirecting to original URL: {url_object.original_url}")
        return redirect(url_object.original_url)
    else:
        current_app.logger.info(f"URL not found: {short_url}")
        return jsonify({'error':'URL not found'}), 404

@main.route('/')
def home():
    return "Welcome to URL Shortener"
    