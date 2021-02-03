import os
import base64
import requests
from datetime import datetime
from dotenv import load_dotenv
from pytz import timezone, utc
from ..config import REPO_URL, COMMITS_URL, CONTENTS_URL

load_dotenv()


def get_commit_data(datafile):
    try:
        headers = {"Authorization": "token " + os.getenv("GITHUB_API_TOKEN")}
    except TypeError:
        headers = {}

    r = requests.get(
        os.path.join(REPO_URL, COMMITS_URL.format(datafile)), headers=headers
    ).json()

    return r


def get_commit_date(datafile):
    r = get_commit_data(datafile)

    commit_date = r[0]["commit"]["author"]["date"]
    commit_date = datetime.strptime(commit_date, "%Y-%m-%dT%H:%M:%SZ")

    commit_date_utc = utc.localize(commit_date)
    commit_date_tz = commit_date_utc.astimezone(timezone("Europe/Oslo"))

    return commit_date_tz


def get_commit_sha(datafile):
    r = get_commit_data(datafile)
    sha = r[0]["sha"]

    return sha


def get_file_contents(datafile, sha):
    try:
        headers = {"Authorization": "token " + os.getenv("GITHUB_API_TOKEN")}
    except TypeError:
        headers = {}

    r = requests.get(
        os.path.join(REPO_URL, CONTENTS_URL.format(datafile, sha)), headers=headers
    ).json()

    content = r["content"]
    decoded_content = base64.b64decode(content).decode("utf-8")

    return decoded_content
