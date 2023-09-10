from re import A
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

slack_name = "SamG1"
github_file = "https://github.com/sammygeze15/intern0/edit/main/endpoint.py"
github_repo = "https://github.com/sammygeze15/intern0"
track = "Backend"

@app.route('/getit', methods=['GET'])

def getit():
    
    
    #get currernt day of the week 
    current_day = datetime.datetime.utcnow().strftime('%A')

    #get current utc time wiht validation of +/-2 hours
    current_time_utc = datetime.datetime.utcnow()
    min_valid_time = current_time_utc - datetime.timedelta(hours=2)
    max_valid_time = current_time_utc + datetime.timedelta(hours=2)
    
    #check if the current time is within the valid range
    if min_valid_time <= current_time_utc <= max_valid_time:
        time_validation = "Valid"
    else:
        time_validation = "Invalid"

    #response in json format
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': current_time_utc.strftime('%Y-%m-%d %H:%M:%S UTC'),
        'github_file': github_file,
        'github_repo': github_repo,
        'track': track,
        'status_code': 200
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
