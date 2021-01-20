import json
import pandas as pd
from datetime import date, timedelta
from .file_commits import get_commit_date
from .data import (
    get_meta, get_transport, get_timeseries_category,
    get_timeseries_new, get_timeseries_total
)

from app.config import (
    CURRENT_JSON_PATH, TIMESERIES_JSON_PATH,
    TIMESERIES_CONFIRMED_JSON_PATH, TIMESERIES_DEAD_JSON_PATH,
    TIMESERIES_TESTED_JSON_PATH, TIMESERIES_TESTED_LAB_JSON_PATH,
    TIMESERIES_HOSPITALIZED_JSON_PATH, TRANSPORT_JSON_PATH,
    TIMESERIES_VACCINE_DOSES_JSON_PATH
)


def current():
    today = pd.to_datetime(date.today())
    yesterday = today - timedelta(days=1)

    confirmed = get_meta('confirmed')
    tested = get_meta('tested')
    dead = get_meta('dead')
    hospitalized = get_meta('hospitalized')
    vaccine_doses = get_meta('vaccine_doses')

    hospitalized['adm_new'] = hospitalized.admissions.diff().fillna(0)
    hospitalized['resp_new'] = hospitalized.respiratory.diff().fillna(0)
    hospitalized['adm_sma7'] = hospitalized.adm_new.rolling(window=7).mean()
    hospitalized['resp_sma7'] = hospitalized.resp_new.rolling(window=7).mean()

    try:
        vaccine_newToday = vaccine_doses.new.at[today]
    except KeyError:
        vaccine_newToday = 0

    try:
        vaccine_newYesterday = vaccine_doses.new.at[yesterday]
    except KeyError:
        vaccine_newYesterday = 0

    r = {
        'area': {
            'code': '00',
            'name': 'Norge',
            'name_en': 'Norway',
            'population': 5367580
        },
        'data': {
            'tested': {
                'newToday': int(tested.new.at[today]),
                'newYesterday': int(tested.new.at[yesterday]),
                'newSince_d7': int(tested.new.tail(7).sum()),
                'newSince_d8': int(tested.new.tail(8).sum()),
                'newSince_d14': int(tested.new.tail(14).sum()),
                'newSince_d15': int(tested.new.tail(15).sum()),
                'newDaily_avg_7': round(float(tested.new.tail(7).mean()), 2),
                'newDaily_avg_14': round(float(tested.new.tail(14).mean()), 2),
                'total': int(tested.total.at[today]),
                'updated': {
                    'source': str(tested.source.at[today]),
                    'timestamp': str(get_commit_date('tested'))
                }
            },
            'confirmed': {
                'newToday': int(confirmed.new.at[today]),
                'newYesterday': int(confirmed.new.at[yesterday]),
                'newSince_d7': int(confirmed.new.tail(7).sum()),
                'newSince_d8': int(confirmed.new.tail(8).sum()),
                'newSince_d14': int(confirmed.new.tail(14).sum()),
                'newSince_d15': int(confirmed.new.tail(15).sum()),
                'newDaily_avg_7': round(float(confirmed.new.tail(7).mean()), 2),
                'newDaily_avg_14': round(float(confirmed.new.tail(14).mean()), 2),
                'total': int(confirmed.total.at[today]),
                'updated': {
                    'source': str(confirmed.source.at[today]),
                    'timestamp': str(get_commit_date('confirmed'))
                }
            },
            'dead': {
                'newToday': int(dead.new.at[today]),
                'newYesterday': int(dead.new.at[yesterday]),
                'newSince_d7': int(dead.new.tail(7).sum()),
                'newSince_d8': int(dead.new.tail(8).sum()),
                'newSince_d14': int(dead.new.tail(14).sum()),
                'newSince_d15': int(dead.new.tail(15).sum()),
                'newDaily_avg_7': round(float(dead.new.tail(7).mean()), 2),
                'newDaily_avg_14': round(float(dead.new.tail(14).mean()), 2),
                'total': int(dead.total.at[today]),
                'updated': {
                    'source': str(dead.source.at[today]),
                    'timestamp': str(get_commit_date('dead'))
                }
            },
            'admissions': {
                'changeToday': int(hospitalized.adm_new.at[today]),
                'changeYesterday': int(hospitalized.adm_new.at[yesterday]),
                'change_d7': int(hospitalized.adm_new.tail(7).sum()),
                'change_d8': int(hospitalized.adm_new.tail(8).sum()),
                'change_d14': int(hospitalized.adm_new.tail(14).sum()),
                'change_d15': int(hospitalized.adm_new.tail(15).sum()),
                'total': int(hospitalized.admissions.at[today]),
                'updated': {
                    'source': str(hospitalized.source.at[today]),
                    'timestamp': str(get_commit_date('hospitalized'))
                }
            },
            'respiratory': {
                'changeToday': int(hospitalized.resp_new.at[today]),
                'changeYesterday': int(hospitalized.resp_new.at[yesterday]),
                'change_d7': int(hospitalized.resp_new.tail(7).sum()),
                'change_d8': int(hospitalized.resp_new.tail(8).sum()),
                'change_d14': int(hospitalized.resp_new.tail(14).sum()),
                'change_d15': int(hospitalized.resp_new.tail(15).sum()),
                'total': int(hospitalized.respiratory.at[today]),
                'updated': {
                    'source': str(hospitalized.source.at[today]),
                    'timestamp': str(get_commit_date('hospitalized'))
                }
            },
            'vaccine_doses': {
                'newToday': int(vaccine_newToday),
                'newYesterday': int(vaccine_newYesterday),
                'newSince_d7': int(vaccine_doses.new.tail(7).sum()),
                'newSince_d8': int(vaccine_doses.new.tail(8).sum()),
                'newSince_d14': int(vaccine_doses.new.tail(14).sum()),
                'newSince_d15': int(vaccine_doses.new.tail(15).sum()),
                'newDaily_avg_7': round(float(vaccine_doses.new.tail(7).mean()), 2),
                'newDaily_avg_14': round(float(vaccine_doses.new.tail(14).mean()), 2),
                'total': int(vaccine_doses.total.iloc[-1:].values[0]),
                'updated': {
                    'source': str(vaccine_doses.source.iloc[-1:].values[0]),
                    'timestamp': str(get_commit_date('vaccine_doses'))
                }
            }
        }
    }

    output_json(CURRENT_JSON_PATH, r)


def timeseries():
    new = get_timeseries_new()
    total = get_timeseries_total()

    r = {
        'timeseries': {
            'new': json.loads(new.to_json(orient='records')),
            'total': json.loads(total.to_json(orient='records'))
        }
    }

    output_json(TIMESERIES_JSON_PATH, r)


def timeseries_categories():
    categories = {
        'tested': TIMESERIES_TESTED_JSON_PATH,
        'tested_lab': TIMESERIES_TESTED_LAB_JSON_PATH,
        'confirmed': TIMESERIES_CONFIRMED_JSON_PATH,
        'dead': TIMESERIES_DEAD_JSON_PATH,
        'hospitalized': TIMESERIES_HOSPITALIZED_JSON_PATH,
        'vaccine_doses': TIMESERIES_VACCINE_DOSES_JSON_PATH
    }

    for category in categories:
        df = get_timeseries_category(category)
        #df = df.drop(['source'], axis=1)

        if df is not None:
            r = {
                category: json.loads(df.to_json(orient='records'))
            }
        else:
            r = {
                category: 'not found'
            }

        output_json(categories[category], r)


def transport():
    df = get_transport()

    aircraft = df.loc[df['type'] == 'Fly']
    bus = df.loc[df['type'] == 'Buss']
    ship = df.loc[df['type'] == 'Skip']
    train = df.loc[df['type'] == 'Tog']

    r = {
        'transport': {
            'aircraft': json.loads(aircraft.to_json(orient='records')),
            'bus': json.loads(bus.to_json(orient='records')),
            'ship': json.loads(ship.to_json(orient='records')),
            'train': json.loads(train.to_json(orient='records'))
        }
    }

    output_json(TRANSPORT_JSON_PATH, r)


def output_json(json_path, datadict):
    print('Updating jsonfile:', json_path)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(datadict, f, indent=2, ensure_ascii=False)


def create_json_files():
    current()
    timeseries()
    timeseries_categories()
    transport()
