from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Stage 2 Task {Host an API with your HNG Details }
# @app.route('/',)
@app.route("/api",methods=['GET'])
def My_Profile():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    date = datetime.datetime.now()
    github_repo = 'https://github.com/alex-waiganjo/HNG'
    github_file ='https://github.com/alex-waiganjo/HNG/blob/main/app.py'
    details = {
        "slack_name": slack_name,
        "current_day": date.strftime('%A'),
        "utc_time": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": github_file,
        "github_repo_url": github_repo,
        "status_code": 200
    }
    output =jsonify(details)
    output.headers['Content-Type']='application/json'
    return output


if __name__ == '__main__':
    app.run()
