from flask import Flask, request
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
    details = {
        "Slack_name": slack_name,
        "Current_day": date.strftime('%A'),
        "Utc_time": date.isoformat(),
        "Track": track,
        "Github_file_url": github_repo,
        "Github_repo_url": github_repo,
        "Status_code": 200
    }
    return details


if __name__ == '__main__':
    app.run()
