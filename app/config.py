# Settings
UPDATE_INTERVAL = 300

# Custom OpenAPI
OPENAPI_TITLE = "COVID-19 Norway API"
OPENAPI_API_VERSION = "1.0.0"
OPENAPI_DESCRIPTION = "API for tracking the COVID-19 outbreak in Norway."
OPENAPI_CONTACT = "api (at) c19norge.no"
OPENAPI_HOST = "c19norge.no"
OPENAPI_SERVER_URL = "https://c19norge.no"
OPENAPI_SERVER_BASEPATH = "api"
OPENAPI_EXTERNALDOCS_DESC = "Find out more about this project"
OPENAPI_EXTERNALDOCS_URL = "https://github.com/frefrik/c19norge-api"

# Output json path
CURRENT_JSON_PATH = './created_json/current.json'
TIMESERIES_JSON_PATH = './created_json/timeseries.json'
TIMESERIES_CONFIRMED_JSON_PATH = './created_json/timeseries_confirmed.json'
TIMESERIES_DEAD_JSON_PATH = './created_json/timeseries_dead.json'
TIMESERIES_TESTED_JSON_PATH = './created_json/timeseries_tested.json'
TIMESERIES_TESTED_LAB_JSON_PATH = './created_json/timeseries_tested_lab.json'
TIMESERIES_HOSPITALIZED_JSON_PATH = './created_json/timeseries_hospitalized.json'
TRANSPORT_JSON_PATH = './created_json/transport.json'
SOURCES_JSON_PATH = './created_json/sources.json'

# Datafiles
CONFIRMED_CSV_PATH = './data/confirmed.csv'
DEAD_CSV_PATH = './data/dead.csv'
TESTED_CSV_PATH = './data/tested.csv'
TESTED_LAB_CSV_PATH = './data/tested_lab.csv'
HOSPITALIZED_CSV_PATH = './data/hospitalized.csv'
TRANSPORT_CSV_PATH = './data/transport.csv'

# Datasource - Github API
REPO_URL = 'https://api.github.com/repos/frefrik/c19norge-data/'
COMMITS_URL = 'commits?path=data/{0}.csv&page=1&per_page=1'
CONTENTS_URL = 'contents/data/{0}.csv?ref={1}'

# Example json output
TIMESERIES_EXAMPLE = {
  "timeseries": {
    "new": [{
        "date": "2020-02-21",
        "tested": 0,
        "confirmed": 1,
        "dead": 0,
        "admissions": 0,
        "respiratory": 0
      },
      {
        "date": "2020-02-22",
        "tested": 0,
        "confirmed": 0,
        "dead": 0,
        "admissions": 0,
        "respiratory": 0
      }
    ],
    "total": [{
        "date": "2020-02-21",
        "tested": 0,
        "confirmed": 1,
        "dead": 0,
        "admissions": 0,
        "respiratory": 0
      },
      {
        "date": "2020-02-22",
        "tested": 0,
        "confirmed": 1,
        "dead": 0,
        "admissions": 0,
        "respiratory": 0
      }
    ]
  }
}

TIMESERIES_CATEGORY_EXAMPLE = {
  "confirmed": [{
      "date": "2020-02-21",
      "new": 1,
      "total": 1
    },
    {
      "date": "2020-02-22",
      "new": 0,
      "total": 1
    },
    {
      "date": "2020-02-23",
      "new": 0,
      "total": 1
    },
    {
      "date": "2020-02-24",
      "new": 0,
      "total": 1
    }
  ]
}

CURRENT_EXAMPLE = {
  "area": {
    "code": "00",
    "name": "Norge",
    "name_en": "Norway",
    "population": 5367580
  },
  "data": {
    "tested": {
      "newToday": 16009,
      "newYesterday": 55298,
      "newSince_d7": 151794,
      "newSince_d8": 170282,
      "newSince_d14": 321036,
      "newSince_d15": 338749,
      "newDaily_avg_7": 21684.86,
      "newDaily_avg_14": 22931.14,
      "total": 2050737,
      "updated": {
        "source": "fhi:web",
        "timestamp": "2020-11-17 13:25:02+01:00"
      }
    },
    "confirmed": {
      "newToday": 239,
      "newYesterday": 78,
      "newSince_d7": 2926,
      "newSince_d8": 3525,
      "newSince_d14": 6947,
      "newSince_d15": 7627,
      "newDaily_avg_7": 418.0,
      "newDaily_avg_14": 496.21,
      "total": 29749,
      "updated": {
        "source": "msis:api",
        "timestamp": "2020-11-17 15:10:04+01:00"
      }
    },
    "dead": {
      "newToday": 4,
      "newYesterday": 0,
      "newSince_d7": 13,
      "newSince_d8": 13,
      "newSince_d14": 16,
      "newSince_d15": 16,
      "newDaily_avg_7": 1.86,
      "newDaily_avg_14": 1.14,
      "total": 298,
      "updated": {
        "source": "fhi:git",
        "timestamp": "2020-11-17 13:20:03+01:00"
      }
    },
    "admissions": {
      "changeToday": 4,
      "changeYesterday": 8,
      "change_d7": 35,
      "change_d8": 42,
      "change_d14": 78,
      "change_d15": 75,
      "total": 139,
      "updated": {
        "source": "helsedir:api",
        "timestamp": "2020-11-17 12:40:02+01:00"
      }
    },
    "respiratory": {
      "changeToday": -1,
      "changeYesterday": 3,
      "change_d7": 3,
      "change_d8": 0,
      "change_d14": 12,
      "change_d15": 12,
      "total": 15,
      "updated": {
        "source": "helsedir:api",
        "timestamp": "2020-11-17 12:40:02+01:00"
      }
    }
  }
}

TRANSPORT_EXAMPLE = {
  "transport": {
    "aircraft": [
      {
        "type": "Fly",
        "route": "SK1320",
        "company": "SAS",
        "from": "Oslo",
        "to": "Ålesund",
        "departure": "2020-11-13 13:00:00",
        "arrival": "2020-11-13 13:55:00"
      },
      {
        "type": "Fly",
        "route": "SK2862",
        "company": "SAS",
        "from": "København",
        "to": "Bergen",
        "departure": "2020-11-13 08:10:00",
        "arrival": "2020-11-13 09:35:00"
      }],
    "bus": [
      {
        "type": "Buss",
        "route": "NW400-Kystbussen",
        "company": "NOR-WAY Bussekspress",
        "from": "Stavanger",
        "to": "Bergen",
        "departure": "2020-11-09 16:45:00",
        "arrival": "2020-11-09 22:10:00"
      },
      {
        "type": "Buss",
        "route": "657",
        "company": "VY Bus4You",
        "from": "Malmö",
        "to": "Oslo",
        "departure": "2020-11-07 14:15:00",
        "arrival": "2020-11-07 21:40:00"
      }],
    "ship": [
      {
        "type": "Tog",
        "route": "474",
        "company": "SJ",
        "from": "Bodø",
        "to": "Mosjøen",
        "departure": "2020-11-05 17:39:00",
        "arrival": "2020-11-05 21:33:00"
      },
      {
        "type": "Tog",
        "route": "473",
        "company": "SJ",
        "from": "Mosjøen",
        "to": "Bodø",
        "departure": "2020-11-05 06:55:00",
        "arrival": "2020-11-05 10:55:00"
      }],
    "train": [
      {
        "type": "Skip",
        "route": "Husøy",
        "company": "Boreal",
        "from": "Træna",
        "to": "Stokkvågen",
        "departure": "2020-11-05 06:45:00",
        "arrival": "2020-11-05 08:45:00"
      },
      {
        "type": "Skip",
        "route": "Husøy",
        "company": "Boreal",
        "from": "Stokkvågen",
        "to": "Træna",
        "departure": "2020-11-04 09:05:00",
        "arrival": "2020-11-04 11:05:00"
      }
    ]
  }
}
