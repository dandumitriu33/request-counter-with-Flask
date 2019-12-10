# request-counter-with-Flask
Codecool exercise

Small exercise app that counts requests sent to the localhost:5000/request-counter page.

## Installation

### Ubuntu
1. Download the repository
2. In the terminal, go to the folder where the project is downloaded and install virtualenv
        
        pip3 install virtualenv
        
3. Create a virtual environment and activate it
        
        virtualenv venv
        source venv/bin/activate
        
4. Install the requirements.txt software like Flask
        
        pip3 install -r requirements.txt
        
5. Run the server, while in the root folder
        
        python3 app.py
        
6. On a browser, go to localhost:5000/

### For other operating systems please look for the exact steps

## How to use

1. Go to the request-counter page by clicking the link at the top of the page
This will count as a 'GET' request. Click the link multiple times to get more requests
2. Click the "Press me to generate a POST request" button, even multiple times, for POST requests
3. For DELETE and PUT requests:
    - install curl (again on Ubuntu, for other OSs please look up the steps)
        
        apt-get install curl (or sudo apt-get install curl)
        
    - curl -X "DELETE" http://localhost:5000/request-counter
    - curl -X "PUT" http://localhost:5000/request-counter
4. Finally go to the statistics page and see the results, or print them to the file
        
