from functools import partial, reduce
from datetime import date
import pandas as pd
from ..config import (
    CONFIRMED_CSV_PATH, DEAD_CSV_PATH,
    TESTED_CSV_PATH, TESTED_LAB_CSV_PATH,
    HOSPITALIZED_CSV_PATH, TRANSPORT_CSV_PATH,
    VACCINE_DOSES_CSV_PATH
)


def get_transport():
    df = pd.read_csv(
        TRANSPORT_CSV_PATH,
        usecols=[
            'tr_type', 'route', 'company',
            'tr_from', 'tr_to', 'departure',
            'arrival']
    )

    mapping = {
        'tr_type': 'type',
        'tr_from': 'from',
        'tr_to': 'to'
    }

    df = df.rename(columns=mapping)

    return df


def get_timeseries_category(category):
    categories = {
        'tested': TESTED_CSV_PATH,
        'tested_lab': TESTED_LAB_CSV_PATH,
        'confirmed': CONFIRMED_CSV_PATH,
        'dead': DEAD_CSV_PATH,
        'hospitalized': HOSPITALIZED_CSV_PATH,
        'vaccine_doses': VACCINE_DOSES_CSV_PATH
    }

    try:
        data_url = categories[category]

        df = pd.read_csv(data_url, parse_dates=['date'], index_col=['date'])

        df = df.reset_index().rename(columns={'index': 'date'})
        df['date'] = df['date'].astype('str')

        return df

    except Exception:
        return None


def get_meta(category):
    categories = {
        'tested': {
            'url': TESTED_CSV_PATH,
            'start_date': '2020-03-12'
        },
        'tested_lab': {
            'url': TESTED_LAB_CSV_PATH,
            'start_date': '2020-02-24'
        },
        'confirmed': {
            'url': CONFIRMED_CSV_PATH,
            'start_date': '2020-02-21'
        },
        'dead': {
            'url': DEAD_CSV_PATH,
            'start_date': '2020-03-10'
        },
        'hospitalized': {
            'url': HOSPITALIZED_CSV_PATH,
            'start_date': '2020-03-08'
        },
        'vaccine_doses': {
            'url': VACCINE_DOSES_CSV_PATH,
            'start_date': '2020-12-27'
        }
    }

    try:
        data_url = categories[category]['url']

        df = pd.DataFrame(
            index=pd.date_range(categories[category]['start_date'], date.today())
        )

        df2 = pd.read_csv(data_url, parse_dates=['date'], index_col=['date'])
        df = df.merge(df2, left_index=True, right_index=True, how='outer')

        if category == 'hospitalized':
            df['admissions'] = df['admissions'].fillna(method='ffill').astype('int')
            df['respiratory'] = df['respiratory'].fillna(method='ffill').astype('int')
        elif category == 'tested_lab':
            cols_int = ['new_neg', 'new_pos', 'new_total', 'total_neg', 'total_pos', 'total']
            cols_fzero = ['new_neg', 'new_pos', 'pr100_pos', 'new_total']
            cols_fffill = ['total_neg', 'total_pos', 'total']

            df[cols_fzero] = df[cols_fzero].fillna(0)
            df[cols_fffill] = df[cols_fffill].fillna(method='ffill')
            df[cols_int] = df[cols_int].astype('int')
            df['pr100_pos'] = df['pr100_pos'].astype('float')
        elif category == 'vaccine_doses':
            df = df.rename(
                columns={
                    'new_doses_administered': 'new',
                    'total_doses_administered': 'total'
                }
            )
            df = df.shift(1, fill_value=0)
            df['new'] = df['new'].fillna(0).astype(int)
            df['total'] = df['total'].fillna(method='ffill').astype(int)
        else:
            df['new'] = df['new'].fillna(0).astype('int')
            df['total'] = df['total'].fillna(method='ffill').astype('Int64')
            df['total'] = df['total'].fillna(0)

        df['source'] = df['source'].fillna(method='ffill')

        return df

    except Exception:
        return None


def get_timeseries_new():
    df = pd.DataFrame(
        index=pd.date_range('2020-02-21', date.today())
    )

    tested = pd.read_csv(
        TESTED_CSV_PATH,
        index_col=['date'],
        usecols=['date', 'new']
    ).rename(
        columns={'new': 'tested'}
    )

    confirmed = pd.read_csv(
        CONFIRMED_CSV_PATH,
        index_col=['date'],
        usecols=['date', 'new']
    ).rename(
        columns={'new': 'confirmed'}
    )

    dead = pd.read_csv(
        DEAD_CSV_PATH,
        index_col=['date'],
        usecols=['date', 'new']
    ).rename(
        columns={'new': 'dead'}
    )

    hospitalized = pd.read_csv(
        HOSPITALIZED_CSV_PATH,
        index_col=['date'],
        usecols=['date', 'admissions', 'respiratory']
    )
    hospitalized = hospitalized.diff()

    vaccine_doses = pd.read_csv(
        VACCINE_DOSES_CSV_PATH,
        index_col=['date'],
        usecols=['date', 'new_doses_administered']
    ).rename(
        columns={'new_doses_administered': 'vaccine_doses'}
    )

    dfs = [df, tested, confirmed, dead, hospitalized, vaccine_doses]
    merge = partial(pd.merge, left_index=True, right_index=True, how='outer')
    df = reduce(merge, dfs).fillna(0).reset_index()
    df = df.rename(columns={'index': 'date'})

    df['date'] = df['date'].astype('str')
    df.iloc[:, 1:] = df.iloc[:, 1:].astype('int')

    return df


def get_timeseries_total():
    df = pd.DataFrame(
        index=pd.date_range('2020-02-21', date.today())
    )

    tested = pd.read_csv(
        TESTED_CSV_PATH,
        index_col=['date'],
        usecols=['date', 'total']
    ).rename(
        columns={'total': 'tested'}
    )

    confirmed = pd.read_csv(
        CONFIRMED_CSV_PATH,
        index_col=['date'],
        usecols=['date', 'total']
    ).rename(
        columns={'total': 'confirmed'}
    )

    dead = pd.read_csv(
        DEAD_CSV_PATH,
        index_col=['date'],
        usecols=['date', 'total']
    ).rename(
        columns={'total': 'dead'}
    )

    hospitalized = pd.read_csv(
        HOSPITALIZED_CSV_PATH,
        index_col=['date'],
        usecols=['date', 'admissions', 'respiratory']
    )

    vaccine_doses = pd.read_csv(
        VACCINE_DOSES_CSV_PATH,
        index_col=['date'],
        usecols=['date', 'total_doses_administered']
    ).rename(
        columns={'total_doses_administered': 'vaccine_doses'}
    )

    dfs = [df, tested, confirmed, dead, hospitalized, vaccine_doses]
    merge = partial(pd.merge, left_index=True, right_index=True, how='outer')
    df = reduce(merge, dfs).fillna(method='ffill').reset_index()
    df = df.rename(columns={'index': 'date'}).fillna(0)

    df['date'] = df['date'].astype('str')
    df.iloc[:, 1:] = df.iloc[:, 1:].astype('int')

    return df
