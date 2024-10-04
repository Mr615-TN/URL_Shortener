# URL_Shortener

Important thing to know is that this should work in WSL, Linux, and MacOs. I am using POP OS, which is Ubuntu based, but I doubt the steps are different for other Linux distros.

Step 1:
To run the URL Shortener, you must first create a virtual environment for it.
To create a virtual environment, you run the following command:
python3 -m venv yourvenv

Make sure to rename yourvenv to whatever you want.

Step 2:
Then you need to install the requirements and you run the following command:
        pip3 install -r requirements.txt

Step 3:
To run the actual URL Shortener,you first do the following command:
        python3 app.py

Step 4:
Then you do this command:
        curl -X POST -H "Content-Type: application/json" -d '{"url":"https://www.example.com"}' http://127.0.0.1:5000/shorten

The reason you need to do the previous command is so that you need to send a POST request to /shorten 

Then you should receive a JSON response with a short url 

Then you can use the short url in your browser.
For example, if you get {"short_url":"http://127.0.0.1:5000/abc123"} as your JSON response, you can do http://127.0.0.1:5000/abc123