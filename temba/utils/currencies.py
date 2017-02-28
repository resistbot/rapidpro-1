import pycountry
import six

"""
These are exceptions according to ISO 4217 because they are super-national
currencies, not belonging to any single country.
"""
CURRENCY_EXCEPTIONS = {
    'AD': 'EUR',
    'AF': 'AFN',
    'AG': 'XCD',
    'AI': 'XCD',
    'AO': 'AOA',
    'AQ': '',
    'AS': 'USD',
    'AT': 'EUR',
    'AX': 'EUR',
    'AZ': 'AZN',
    'BA': 'BAM',
    'BE': 'EUR',
    'BF': 'XOF',
    'BG': 'BGN',
    'BJ': 'XOF',
    'BL': 'EUR',
    'BQ': 'USD',
    'BR': 'BRL',
    'BV': 'NOK',
    'BY': 'BYR',
    'CC': 'AUD',
    'CD': 'CDF',
    'CF': 'XAF',
    'CG': 'XAF',
    'CI': 'XOF',
    'CK': 'NZD',
    'CM': 'XAF',
    'CW': 'ANG',
    'CX': 'AUD',
    'DE': 'EUR',
    'DM': 'XCD',
    'EC': 'USD',
    'EH': 'MAD',
    'ES': 'EUR',
    'ET': 'ETB',
    'FI': 'EUR',
    'FM': 'USD',
    'FO': 'DKK',
    'FR': 'EUR',
    'GA': 'XAF',
    'GD': 'XCD',
    'GE': 'GEL',
    'GF': 'EUR',
    'GG': 'GBP',
    'GH': 'GHS',
    'GL': 'DKK',
    'GP': 'EUR',
    'GQ': 'XAF',
    'GR': 'EUR',
    'GS': 'GBP',
    'GU': 'USD',
    'GW': 'XOF',
    'HM': 'AUD',
    'IE': 'EUR',
    'IM': 'GBP',
    'IO': 'USD',
    'IT': 'EUR',
    'JE': 'GBP',
    'KI': 'AUD',
    'KN': 'XCD',
    'LC': 'XCD',
    'LI': 'CHF',
    'LU': 'EUR',
    'MC': 'EUR',
    'ME': 'EUR',
    'MF': 'EUR',
    'MG': 'MGA',
    'MH': 'USD',
    'ML': 'XOF',
    'MP': 'USD',
    'MQ': 'EUR',
    'MS': 'XCD',
    'MZ': 'MZN',
    'NC': 'XPF',
    'NE': 'XOF',
    'NF': 'AUD',
    'NL': 'EUR',
    'NR': 'AUD',
    'NU': 'NZD',
    'PA': 'USD',
    'PF': 'XPF',
    'PL': 'PLN',
    'PM': 'EUR',
    'PN': 'NZD',
    'PR': 'USD',
    'PS': 'ILS',
    'PT': 'EUR',
    'PW': 'USD',
    'RE': 'EUR',
    'RO': 'RON',
    'RS': 'RSD',
    'SD': 'SDG',
    'SI': 'EUR',
    'SJ': 'NOK',
    'SK': 'EUR',
    'SM': 'EUR',
    'SN': 'XOF',
    'SR': 'SRD',
    'SS': 'SSP',
    'SX': 'ANG',
    'TC': 'USD',
    'TD': 'XAF',
    'TF': 'EUR',
    'TG': 'XOF',
    'TJ': 'TJS',
    'TK': 'NZD',
    'TL': 'USD',
    'TR': 'TRY',
    'TV': 'AUD',
    'TW': 'TWD',
    'UA': 'UAH',
    'UM': 'USD',
    'VA': 'EUR',
    'VC': 'XCD',
    'VE': 'VEF',
    'VG': 'USD',
    'VI': 'USD',
    'WF': 'XPF',
    'YE': 'YER',
    'YT': 'EUR'}


def currency_for_country(alpha2):
    country = pycountry.countries.get(alpha_2=six.text_type(alpha2))
    try:
        return pycountry.currencies.get(numeric=country.numeric)
    except:
        currency_code = CURRENCY_EXCEPTIONS.get(six.text_type(alpha2))
        return pycountry.currencies.get(alpha_3=currency_code)


def get_currency_name(code):
    try:
        currency = pycountry.currencies.get(alpha_3=code)
        return currency.name
    except:
        return code


def search_currency_names(query):
    matches = []
    for currency in pycountry.currencies:
        query = query.lower()
        if query in currency.name.lower():
            matches.append(dict(id=currency.alpha_3, text=currency.name.strip()))
    return matches
