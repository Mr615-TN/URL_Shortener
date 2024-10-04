# URL_Shortener
A simple web application that shortens URLs. This URL Shortener allows users to send a POST request with a long URL and receive a shortened version for easy access.

URL Shortener is implemented using:
A Back End Flask server.


Setting up and running the URL Shortener:

Setting up a Virtual Environment

Step 1: To begin, you must first create a virtual environment. Use the following command:


python3 -m venv yourvenv

Note: Replace yourvenv with the name of your choice for the virtual environment.

Step 2: Activate the virtual environment. Use the following command:

# On Linux and MacOS:
source yourvenv/bin/activate

# On Windows (for WSL):
source yourvenv/Scripts/activate


Note: Replace yourvenv with the virtual environment name you used.

Installing Requirements

After activating the virtual environment, install the required dependencies using the following command:

pip3 install -r requirements.txt


Running the Back End Flask Server
Step 1: Start the Flask server by running the following command:


python3 app.py
Sending a POST Request to Shorten a URL
Step 1: Once the Flask server is running, you can shorten a URL by sending a POST request. Use the following command:

curl -X POST -H "Content-Type: application/json" -d '{"url":"https://www.example.com"}' http://127.0.0.1:5000/shorten


Note: Replace "https://www.example.com" with the URL you want to shorten.


Receiving the Shortened URL


After sending the POST request, you will receive a JSON response containing the shortened URL. For example, if you receive the following response:


{"short_url":"http://127.0.0.1:5000/abc123"}


You can access the shortened URL in your browser by visiting:


http://127.0.0.1:5000/abc123


Requirements:
Python 3.6 or higher
Additional Notes:
Ensure that the correct version of Python is installed.
Linux, Mac, and WSL developers should use python3 for all Python commands.
