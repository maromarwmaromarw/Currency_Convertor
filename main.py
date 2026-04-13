import requests
from dotenv import load_dotenv
import os

load_dotenv("config/.env")

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://v6.exchangerate-api.com/v6/"

def exchange_currency(amount, is_pair, first_code, second_code=""):
    
    if not API_KEY:
        print("Error: API_KEY not found in config/.env file.")
        return

    try:
        if is_pair:
            url = f"{BASE_URL}{API_KEY}/pair/{first_code}/{second_code}/{amount}"
            response = requests.get(url)
            
            if response.status_code == 200:
                print("\nConnection Established!")
                data = response.json()
                if data.get("result") == "error":
                    print(f"Error on the API's side! \nError type: {data.get('error-type')}\n")
                    return
                
                base_code = data["base_code"]
                target_code = data["target_code"]
                print("\n" + "="*40)
                print(f"Operation Status: {data['result']}")
                print(f"Base Code: {base_code}")
                print(f"Target Code: {target_code}")
                print(f"Original Amount: {amount} {base_code}")
                print(f"Conversion Result: {data['conversion_result']} {target_code}")
                print("="*40)
            elif response.status_code == 404:
                print("Page not found!")
        else:
            url = f"{BASE_URL}{API_KEY}/latest/{first_code}"
            response = requests.get(url)
            
            if response.status_code == 200:
                print("\nConnection Established!")
                data = response.json()
                if data.get("result") == "error":
                    print(f"Error on the API's side! \nError type: {data.get('error-type')}\n")
                    return
                
                base_code = data["base_code"]
                conversion_rates = data["conversion_rates"]
                print(f"\nOperation Status: {data['result']}")
                print(f"Base Code: {base_code}")
                print(f"Amount to Calculate: {amount} {base_code}\n")
                
                for target_code, rate in conversion_rates.items():
                    result = amount * rate
                    print(f"Target: {target_code} - Result: {result:,.2f}")
            elif response.status_code == 404:
                print("Page not found!")
                
    except Exception as e:
        print(f"Error: {e}")

def main_function():
    """
    Main CLI Interface
    """
    help_msg = (
        "\n--- HELP MENU ---"
        "\nWelcome to the currency conversion tool!"
        "\n- Toggle 'Pair Mode' to switch between specific conversion or seeing all rates."
        "\n- Enter the numeric amount, then the 3-letter currency code (e.g., USD, EUR)."
        "\n- Use Option 4 to search for a code by country or currency name."
    )
    
    CURRENCY_DATA = {
        'AED': ('UAE Dirham', 'United Arab Emirates'),
        'AFN': ('Afghan Afghani', 'Afghanistan'),
        'ALL': ('Albanian Lek', 'Albania'),
        'AMD': ('Armenian Dram', 'Armenia'),
        'ANG': ('Netherlands Antillian Guilder', 'Netherlands Antilles'),
        'AOA': ('Angolan Kwanza', 'Angola'),
        'ARS': ('Argentine Peso', 'Argentina'),
        'AUD': ('Australian Dollar', 'Australia'),
        'AWG': ('Aruban Florin', 'Aruba'),
        'AZN': ('Azerbaijani Manat', 'Azerbaijan'),
        'BAM': ('Bosnia and Herzegovina Mark', 'Bosnia and Herzegovina'),
        'BBD': ('Barbados Dollar', 'Barbados'),
        'BDT': ('Bangladeshi Taka', 'Bangladesh'),
        'BGN': ('Bulgarian Lev', 'Bulgaria'),
        'BHD': ('Bahraini Dinar', 'Bahrain'),
        'BIF': ('Burundian Franc', 'Burundi'),
        'BMD': ('Bermudian Dollar', 'Bermuda'),
        'BND': ('Brunei Dollar', 'Brunei'),
        'BOB': ('Bolivian Boliviano', 'Bolivia'),
        'BRL': ('Brazilian Real', 'Brazil'),
        'BSD': ('Bahamian Dollar', 'Bahamas'),
        'BTN': ('Bhutanese Ngultrum', 'Bhutan'),
        'BWP': ('Botswana Pula', 'Botswana'),
        'BYN': ('Belarusian Ruble', 'Belarus'),
        'BZD': ('Belize Dollar', 'Belize'),
        'CAD': ('Canadian Dollar', 'Canada'),
        'CDF': ('Congolese Franc', 'Democratic Republic of the Congo'),
        'CHF': ('Swiss Franc', 'Switzerland'),
        'CLF': ('Chilean Unidad de Fomento', 'Chile'),
        'CLP': ('Chilean Peso', 'Chile'),
        'CNH': ('Offshore Chinese Renminbi', 'China'),
        'CNY': ('Chinese Renminbi', 'China'),
        'COP': ('Colombian Peso', 'Colombia'),
        'CRC': ('Costa Rican Colon', 'Costa Rica'),
        'CUP': ('Cuban Peso', 'Cuba'),
        'CVE': ('Cape Verdean Escudo', 'Cape Verde'),
        'CZK': ('Czech Koruna', 'Czech Republic'),
        'DJF': ('Djiboutian Franc', 'Djibouti'),
        'DKK': ('Danish Krone', 'Denmark'),
        'DOP': ('Dominican Peso', 'Dominican Republic'),
        'DZD': ('Algerian Dinar', 'Algeria'),
        'EGP': ('Egyptian Pound', 'Egypt'),
        'ERN': ('Eritrean Nakfa', 'Eritrea'),
        'ETB': ('Ethiopian Birr', 'Ethiopia'),
        'EUR': ('Euro', 'European Union'),
        'FJD': ('Fiji Dollar', 'Fiji'),
        'FKP': ('Falkland Islands Pound', 'Falkland Islands'),
        'FOK': ('Faroese Króna', 'Faroe Islands'),
        'GBP': ('Pound Sterling', 'United Kingdom'),
        'GEL': ('Georgian Lari', 'Georgia'),
        'GGP': ('Guernsey Pound', 'Guernsey'),
        'GHS': ('Ghanaian Cedi', 'Ghana'),
        'GIP': ('Gibraltar Pound', 'Gibraltar'),
        'GMD': ('Gambian Dalasi', 'The Gambia'),
        'GNF': ('Guinean Franc', 'Guinea'),
        'GTQ': ('Guatemalan Quetzal', 'Guatemala'),
        'GYD': ('Guyanese Dollar', 'Guyana'),
        'HKD': ('Hong Kong Dollar', 'Hong Kong'),
        'HNL': ('Honduran Lempira', 'Honduras'),
        'HRK': ('Croatian Kuna', 'Croatia'),
        'HTG': ('Haitian Gourde', 'Haiti'),
        'HUF': ('Hungarian Forint', 'Hungary'),
        'IDR': ('Indonesian Rupiah', 'Indonesia'),
        'ILS': ('Israeli New Shekel', 'Israel'),
        'IMP': ('Manx Pound', 'Isle of Man'),
        'INR': ('Indian Rupee', 'India'),
        'IQD': ('Iraqi Dinar', 'Iraq'),
        'ISK': ('Icelandic Króna', 'Iceland'),
        'JEP': ('Jersey Pound', 'Jersey'),
        'JMD': ('Jamaican Dollar', 'Jamaica'),
        'JOD': ('Jordanian Dinar', 'Jordan'),
        'JPY': ('Japanese Yen', 'Japan'),
        'KES': ('Kenyan Shilling', 'Kenya'),
        'KGS': ('Kyrgyzstani Som', 'Kyrgyzstan'),
        'KHR': ('Cambodian Riel', 'Cambodia'),
        'KID': ('Kiribati Dollar', 'Kiribati'),
        'KMF': ('Comorian Franc', 'Comoros'),
        'KRW': ('South Korean Won', 'South Korea'),
        'KWD': ('Kuwaiti Dinar', 'Kuwait'),
        'KYD': ('Cayman Islands Dollar', 'Cayman Islands'),
        'KZT': ('Kazakhstani Tenge', 'Kazakhstan'),
        'LAK': ('Lao Kip', 'Laos'),
        'LBP': ('Lebanese Pound', 'Lebanon'),
        'LKR': ('Sri Lanka Rupee', 'Sri Lanka'),
        'LRD': ('Liberian Dollar', 'Liberia'),
        'LSL': ('Lesotho Loti', 'Lesotho'),
        'LYD': ('Libyan Dinar', 'Libya'),
        'MAD': ('Moroccan Dirham', 'Morocco'),
        'MDL': ('Moldovan Leu', 'Moldova'),
        'MGA': ('Malagasy Ariary', 'Madagascar'),
        'MKD': ('Macedonian Denar', 'North Macedonia'),
        'MMK': ('Burmese Kyat', 'Myanmar'),
        'MNT': ('Mongolian Tögrög', 'Mongolia'),
        'MOP': ('Macanese Pataca', 'Macau'),
        'MRU': ('Mauritanian Ouguiya', 'Mauritania'),
        'MUR': ('Mauritian Rupee', 'Mauritius'),
        'MVR': ('Maldivian Rufiyaa', 'Maldives'),
        'MWK': ('Malawian Kwacha', 'Malawi'),
        'MXN': ('Mexican Peso', 'Mexico'),
        'MYR': ('Malaysian Ringgit', 'Malaysia'),
        'MZN': ('Mozambican Metical', 'Mozambique'),
        'NAD': ('Namibian Dollar', 'Namibia'),
        'NGN': ('Nigerian Naira', 'Nigeria'),
        'NIO': ('Nicaraguan Córdoba', 'Nicaragua'),
        'NOK': ('Norwegian Krone', 'Norway'),
        'NPR': ('Nepalese Rupee', 'Nepal'),
        'NZD': ('New Zealand Dollar', 'New Zealand'),
        'OMR': ('Omani Rial', 'Oman'),
        'PAB': ('Panamanian Balboa', 'Panama'),
        'PEN': ('Peruvian Sol', 'Peru'),
        'PGK': ('Papua New Guinean Kina', 'Papua New Guinea'),
        'PHP': ('Philippine Peso', 'Philippines'),
        'PKR': ('Pakistani Rupee', 'Pakistan'),
        'PLN': ('Polish Złoty', 'Poland'),
        'PYG': ('Paraguayan Guaraní', 'Paraguay'),
        'QAR': ('Qatari Riyal', 'Qatar'),
        'RON': ('Romanian Leu', 'Romania'),
        'RSD': ('Serbian Dinar', 'Serbia'),
        'RUB': ('Russian Ruble', 'Russia'),
        'RWF': ('Rwandan Franc', 'Rwanda'),
        'SAR': ('Saudi Riyal', 'Saudi Arabia'),
        'SBD': ('Solomon Islands Dollar', 'Solomon Islands'),
        'SCR': ('Seychellois Rupee', 'Seychelles'),
        'SDG': ('Sudanese Pound', 'Sudan'),
        'SEK': ('Swedish Krona', 'Sweden'),
        'SGD': ('Singapore Dollar', 'Singapore'),
        'SHP': ('Saint Helena Pound', 'Saint Helena'),
        'SLE': ('Sierra Leonean Leone', 'Sierra Leone'),
        'SOS': ('Somali Shilling', 'Somalia'),
        'SRD': ('Surinamese Dollar', 'Suriname'),
        'SSP': ('South Sudanese Pound', 'South Sudan'),
        'STN': ('São Tomé and Príncipe Dobra', 'São Tomé and Príncipe'),
        'SYP': ('Syrian Pound', 'Syria'),
        'SZL': ('Eswatini Lilangeni', 'Eswatini'),
        'THB': ('Thai Baht', 'Thailand'),
        'TJS': ('Tajikistani Somoni', 'Tajikistan'),
        'TMT': ('Turkmenistan Manat', 'Turkmenistan'),
        'TND': ('Tunisian Dinar', 'Tunisia'),
        'TOP': ('Tongan Paʻanga', 'Tonga'),
        'TRY': ('Turkish Lira', 'Turkey'),
        'TTD': ('Trinidad and Tobago Dollar', 'Trinidad and Tobago'),
        'TVD': ('Tuvaluan Dollar', 'Tuvalu'),
        'TWD': ('New Taiwan Dollar', 'Taiwan'),
        'TZS': ('Tanzanian Shilling', 'Tanzania'),
        'UAH': ('Ukrainian Hryvnia', 'Ukraine'),
        'UGX': ('Ugandan Shilling', 'Uganda'),
        'USD': ('United States Dollar', 'United States'),
        'UYU': ('Uruguayan Peso', 'Uruguay'),
        'UZS': ('Uzbekistani So\'m', 'Uzbekistan'),
        'VES': ('Venezuelan Bolívar Soberano', 'Venezuela'),
        'VND': ('Vietnamese Đồng', 'Vietnam'),
        'VUV': ('Vanuatu Vatu', 'Vanuatu'),
        'WST': ('Samoan Tālā', 'Samoa'),
        'XAF': ('Central African CFA Franc', 'CEMAC'),
        'XCD': ('East Caribbean Dollar', 'Organisation of Eastern Caribbean States'),
        'XDR': ('Special Drawing Rights', 'International Monetary Fund'),
        'XOF': ('West African CFA franc', 'CFA'),
        'XPF': ('CFP Franc', 'Collectivités d\'Outre-Mer'),
        'YER': ('Yemeni Rial', 'Yemen'),
        'ZAR': ('South African Rand', 'South Africa'),
        'ZMW': ('Zambian Kwacha', 'Zambia'),
        'ZWL': ('Zimbabwean Dollar', 'Zimbabwe')
    }
    
    pair_mode = False
    
    while True:
        print("\n" + "="*20)
        print(f"PAIR MODE: {'ON' if pair_mode else 'OFF'}")
        print("="*20)
        choice = input("1. Convert a value\n2. Change pair mode\n3. Show supported codes\n4. Search a code\n5. Help\n6. Exit\n\nSelection: ").strip()
        
        match choice:
            case "1":
                try:
                    amount = float(input("\nHow much do you want to convert? "))
                    first_base_code = input("Enter the base code (e.g. USD): ").strip().upper()
                    if pair_mode:
                        first_target_code = input("Enter the target code (e.g. EUR): ").strip().upper()
                        exchange_currency(amount, pair_mode, first_base_code, first_target_code)
                    else:
                        exchange_currency(amount, pair_mode, first_base_code)
                except ValueError:
                    print("\nInvalid amount! Please enter a number.")
            case "2":
                pair_mode = not pair_mode
                print(f"\nChanged Pairing-Mode to: {pair_mode}")
            case "3":
                print("\nFetching currency codes...")
                for code, (name, country) in CURRENCY_DATA.items():
                    print(f"{code}: {name} – {country}")
            case "4":
                query = input("\nEnter the country name or currency name: ").strip().lower()
                matches = []
                for code, (name, country) in CURRENCY_DATA.items():
                    if query in name.lower() or query in country.lower() or query == code.lower():
                        matches.append(f"Code: {code} - Name: {name} – Country: {country}")
                
                if matches:
                    print(f"\nFound {len(matches)} match(es):")
                    for m in matches:
                        print(m)
                else:
                    print("\nNo matching codes found.")
            case "5":
                print(help_msg)
            case "6":
                print("Exiting...")
                break
            case _:
                print("\nInvalid choice, please select 1-6.")

if __name__ == "__main__":
    main_function()