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
TIMESERIES_VACCINE_DOSES_JSON_PATH = './created_json/timeseries_vaccine_doses.json'
TRANSPORT_JSON_PATH = './created_json/transport.json'
SOURCES_JSON_PATH = './created_json/sources.json'

# Datafiles
CONFIRMED_CSV_PATH = './data/confirmed.csv'
DEAD_CSV_PATH = './data/dead.csv'
TESTED_CSV_PATH = './data/tested.csv'
TESTED_LAB_CSV_PATH = './data/tested_lab.csv'
HOSPITALIZED_CSV_PATH = './data/hospitalized.csv'
TRANSPORT_CSV_PATH = './data/transport.csv'
VACCINE_DOSES_CSV_PATH = './data/vaccine_doses.csv'

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
        "respiratory": 0,
        "vaccine_doses": 0
      },
      {
        "date": "2020-02-22",
        "tested": 0,
        "confirmed": 0,
        "dead": 0,
        "admissions": 0,
        "respiratory": 0,
        "vaccine_doses": 0
      }
    ],
    "total": [{
        "date": "2020-02-21",
        "tested": 0,
        "confirmed": 1,
        "dead": 0,
        "admissions": 0,
        "respiratory": 0,
        "vaccine_doses": 0
      },
      {
        "date": "2020-02-22",
        "tested": 0,
        "confirmed": 1,
        "dead": 0,
        "admissions": 0,
        "respiratory": 0,
        "vaccine_doses": 0
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
      "newToday": 57967,
      "newYesterday": 0,
      "newSince_d7": 179550,
      "newSince_d8": 245004,
      "newSince_d14": 334086,
      "newSince_d15": 334086,
      "newDaily_avg_7": 25650.0,
      "newDaily_avg_14": 23863.29,
      "total": 3122606,
      "updated": {
        "source": "fhi:web",
        "timestamp": "2021-01-14 13:10:02+01:00"
      }
    },
    "confirmed": {
      "newToday": 240,
      "newYesterday": 81,
      "newSince_d7": 2920,
      "newSince_d8": 3654,
      "newSince_d14": 7381,
      "newSince_d15": 7816,
      "newDaily_avg_7": 417.14,
      "newDaily_avg_14": 527.21,
      "total": 57522,
      "updated": {
        "source": "msis:api",
        "timestamp": "2021-01-14 15:10:05+01:00"
      }
    },
    "dead": {
      "newToday": 2,
      "newYesterday": 27,
      "newSince_d7": 44,
      "newSince_d8": 46,
      "newSince_d14": 75,
      "newSince_d15": 75,
      "newDaily_avg_7": 6.29,
      "newDaily_avg_14": 5.36,
      "total": 511,
      "updated": {
        "source": "fhi:git",
        "timestamp": "2021-01-14 13:25:04+01:00"
      }
    },
    "admissions": {
      "changeToday": 8,
      "changeYesterday": 7,
      "change_d7": 37,
      "change_d8": 35,
      "change_d14": 24,
      "change_d15": 19,
      "total": 164,
      "updated": {
        "source": "helsedir:api",
        "timestamp": "2021-01-14 12:00:04+01:00"
      }
    },
    "respiratory": {
      "changeToday": -1,
      "changeYesterday": 2,
      "change_d7": 4,
      "change_d8": 7,
      "change_d14": 8,
      "change_d15": 9,
      "total": 23,
      "updated": {
        "source": "helsedir:api",
        "timestamp": "2021-01-14 12:00:04+01:00"
      }
    },
    "vaccine_doses": {
      "newToday": 7622,
      "newYesterday": 3809,
      "newSince_d7": 19549,
      "newSince_d8": 28121,
      "newSince_d14": 31529,
      "newSince_d15": 31949,
      "newDaily_avg_7": 2792.71,
      "newDaily_avg_14": 2252.07,
      "total": 33611,
      "updated": {
        "source": "fhi:web",
        "timestamp": "2021-01-14 20:31:57+01:00"
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
