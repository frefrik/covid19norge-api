import json
from .utils import (
    get_commit_data, get_commit_sha,
    create_json_files, get_file_contents
)


async def check_for_updates():
    print('Checking for updates...')
    refresh_data = False
    datafiles = [
        'confirmed',
        'dead',
        'hospitalized',
        'tested',
        'tested_lab',
        'transport',
        'vaccine_doses'
    ]

    with open('./created_json/sources.json') as f:
        data_json = json.load(f)

    for datafile in datafiles:
        commit = get_commit_data(datafile)
        sha_git = commit[0]['sha']

        commit_date = commit[0]['commit']['author']['date']
        sha_current = data_json[datafile]['sha']

        if sha_git != sha_current:
            refresh_data = True
            print(datafile, 'NEW FILE FOUND')

            data_json[datafile]['datafile'] = f'{datafile}.csv'
            data_json[datafile]['sha'] = sha_git
            data_json[datafile]['updated'] = commit_date

            with open('./created_json/sources.json', 'w') as json_file:
                json.dump(data_json, json_file, indent=4)

            contents = get_file_contents(datafile, sha_git)

            with open(f'./data/{datafile}.csv', 'w') as outfile:
                outfile.write(contents)

    if refresh_data:
        create_json_files()


async def get_datafiles():
    print('Downloading datafiles from source')
    datafiles = [
        'confirmed',
        'dead',
        'hospitalized',
        'tested',
        'tested_lab',
        'transport',
        'vaccine_doses'
    ]

    for datafile in datafiles:
        sha = get_commit_sha(datafile)
        contents = get_file_contents(datafile, sha)

        with open(f'./data/{datafile}.csv', 'w') as outfile:
            outfile.write(contents)
