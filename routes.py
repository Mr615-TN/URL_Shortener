from flask import Blueprint, request,jsonify,redirect
from models import URL
from app import db 

main = Blueprint('main', __name__)

@main.route('shorten', methods=[POST])
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
    url = URL.query.filter_by(short_url=short_url) 
    if url:
        return redirect(url.original_url)
    else:
        return jsonify({'error':'URL not found'}), 404
    