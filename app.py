#importing the necessary libraries needed
from flask import Flask, request, jsonify
import datetime

#given the file a name
app = Flask(__name__)

#setting up a path
@app.route('/api', methods=['GET'])

#defining a function used to get info
def get_info():
    slack_name = request.args.get('slack_name')#this code tells the computer to look for 'slack_name' to be used later
    track = request.args.get('track')
    
    current_day = datetime.datetime.now().strftime('%A') # code to find out which day it is
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')#finding out the current time
    
    github_repo_url = "https://github.com/Ollie345/create_hosting_backend"
    github_file_url = "https://github.com/Ollie345/create_hosting_backend/blob/main/app.py"
    
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
    
    