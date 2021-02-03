# COVID-19 Norway API

API for tracking the COVID-19 outbreak in Norway.  


## Data Sources

All the data presented in this API is sourced from **official Norwegian authorities**.  
See link for more detailed information.
- https://github.com/frefrik/c19norge-data

## Documentation
Swagger UI: https://c19norge.no/api  
ReDoc: https://c19norge.no/api/docs


## Endpoints
- **[<code>GET</code> Current Key Figures](#current-key-figures)**
- **[<code>GET</code> Timeseries](#timeseries)**
- **[<code>GET</code> Timeseries (Category)](#timeseries-category)**
- **[<code>GET</code> Transport](#transport)**


## Current Key Figures

    GET /v1/current

Returns current key figures

- **tested**: Tested cases
- **confirmed**: Confirmed cases
- **dead**: Death cases
- **admissions**: Admissions
- **respiratory**: Respiratory
- **vaccine_doses**: Vaccine doses administered

### Example
#### Request

    GET https://c19norge.no/api/v1/current

#### Response
``` json
{
  "area": {
    "code": "00",
    "name": "Norge",
    "name_en": "Norway",
    "population": 5367580
  },
  "data": {
    "tested": {
      "newToday": 20820,
      "newYesterday": 14383,
      "newSince_d7": 119406,
      "newSince_d8": 145179,
      "newSince_d14": 231266,
      "newSince_d15": 252672,
      "newDaily_avg_7": 17058,
      "newDaily_avg_14": 16519,
      "total": 3454305,
      "updated": {
        "source": "fhi:web",
        "timestamp": "2021-02-03 13:00:03+01:00"
      }
    },
    "confirmed": {
      "newToday": 192,
      "newYesterday": 50,
      "newSince_d7": 1428,
      "newSince_d8": 1771,
      "newSince_d14": 3495,
      "newSince_d15": 3850,
      "newDaily_avg_7": 204,
      "newDaily_avg_14": 249.64,
      "total": 63745,
      "updated": {
        "source": "msis:api",
        "timestamp": "2021-02-03 15:15:03+01:00"
      }
    }
  }
}
```

## Timeseries

    GET /v1/timeseries

Returns timeseries data

### Example
#### Request

    GET https://c19norge.no/api/v1/timeseries

#### Response
``` json
{
  "timeseries": {
    "new": [
      {
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
    "total": [
      {
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
```

## Timeseries (Category)

    GET /v1/timeseries/{category}

Returns timeseries data for specified category

### Query Parameters
Parameter | Valid values
--- | ---
category | tested<br/>tested_lab<br/>confirmed<br/>dead<br/>hospitalized<br/>vaccine_doses<br/>smittestopp<br/>

### Example
#### Request

    GET https://c19norge.no/api/v1/timeseries/confirmed

#### Response
``` json
{
  "confirmed": [
    {
      "date": "2021-01-30",
      "new": 175,
      "total": 63069,
      "source": "fhi:git"
    },
    {
      "date": "2021-01-31",
      "new": 175,
      "total": 63244,
      "source": "fhi:git"
    },
    {
      "date": "2021-02-01",
      "new": 259,
      "total": 63503,
      "source": "fhi:git"
    },
    {
      "date": "2021-02-02",
      "new": 50,
      "total": 63553,
      "source": "fhi:git"
    }
  ]
}
```

## Transport

    GET /v1/transport

Returns departures where persons infected with covid-19 have been on board (aircraft, ships, trains and buses).

### Example
#### Request

    GET https://c19norge.no/api/v1/transport

#### Response
``` json
{
  "transport": {
    "aircraft": [{
        "type": "Fly",
        "route": "QR175",
        "company": "Qatar Airways",
        "from": "Doha",
        "to": "Oslo",
        "departure": "2021-01-31 08:00:00",
        "arrival": "2021-01-31 13:00:00"
      },
      {
        "type": "Fly",
        "route": "TK1751",
        "company": "Turkish Airlines",
        "from": "Istanbul",
        "to": "Oslo",
        "departure": "2021-01-30 08:50:00",
        "arrival": "2021-01-30 10:35:00"
      }
    ],
    "bus": [{
        "type": "Buss",
        "route": "FB11",
        "company": "Flybussen",
        "from": "Fredrikstad",
        "to": "Oslo lufthavn",
        "departure": "2021-01-10 12:30:00",
        "arrival": "2021-01-10 14:40:00"
      },
      {
        "type": "Buss",
        "route": "600",
        "company": "Bus4You",
        "from": "Malmö",
        "to": "Oslo",
        "departure": "2021-01-08 15:50:00",
        "arrival": "2021-01-08 19:10:00"
      }
    ],
    "ship": [{
        "type": "Skip",
        "route": "Superspeed 2",
        "company": "Color Line ",
        "from": "Hirtshals",
        "to": "Larvik",
        "departure": "2021-01-29 12:45:00",
        "arrival": "2021-01-29 16:30:00"
      },
      {
        "type": "Skip",
        "route": "Superspeed 1",
        "company": "Color Line ",
        "from": "Hirthals",
        "to": "Kristiansand",
        "departure": "2021-01-16 20:45:00",
        "arrival": "2021-01-16 23:59:00"
      }
    ],
    "train": [{
        "type": "Tog",
        "route": "41.0",
        "company": "VY",
        "from": "Oslo",
        "to": "Bergen",
        "departure": "2021-01-16 08:25:00",
        "arrival": "2021-01-16 14:55:00"
      },
      {
        "type": "Tog",
        "route": "41",
        "company": "VY",
        "from": "Oslo",
        "to": "Bergen",
        "departure": "2021-01-16 08:25:00",
        "arrival": "2021-01-16 14:55:00"
      }
    ]
  }
}
```