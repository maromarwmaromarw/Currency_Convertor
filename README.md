# Currency Converter CLI

A robust Python-based Command Line Interface (CLI) tool for real-time currency conversion and exchange rate tracking. This tool leverages the **ExchangeRate-API** to provide accurate data across 160+ currencies.

## 🚀 Features

  * **Pair Mode (One-to-One):** Directly convert a specific amount from one currency to another (e.g., 100 USD to EUR).
  * **Latest Rates (One-to-Many):** Input a base currency and an amount to see its value across all supported global currencies.
  * **Smart Search:** Search for 3-letter currency codes using country names or currency names (e.g., searching "Japan" returns JPY).
  * **Comprehensive Database:** Built-in dictionary of over 160 currencies, names, and associated countries.
  * **Error Handling:** Robust validation for API keys, network connections, and user input.

-----

## 🛠️ Prerequisites

  * **Python 3.10+** (The script uses `match/case` statements).
  * **API Key:** You will need a free API key from [ExchangeRate-API](https://www.exchangerate-api.com/).

-----

## 📦 Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/currency-converter.git
    cd currency-converter
    ```

2.  **Install dependencies:**

    ```bash
    pip install requests python-dotenv
    ```

3.  **Setup Environment Variables:**

      * Create a folder named `config`.
      * Inside `config`, create a file named `.env`.
      * Add your API key to the file:

    <!-- end list -->

    ```env
    API_KEY=your_actual_api_key_here
    ```

-----

## 🖥️ Usage

Run the script using Python:

```bash
python main.py
```

### Menu Options

| Option | Description |
| :--- | :--- |
| **1. Convert a value** | Performs the conversion based on the current mode. |
| **2. Change pair mode** | Toggles between **Pair Mode** (specific conversion) and **Standard Mode** (all rates). |
| **3. Show supported codes** | Prints a full list of all 160+ supported currency codes. |
| **4. Search a code** | Find a code by typing a country (e.g., "Canada") or name (e.g., "Peso"). |
| **5. Help** | Displays the help menu. |
| **6. Exit** | Closes the application. |

-----

## 📂 Project Structure

```text
.
├── config/
│   └── .env            # Environment variables (API Key)
├── main.py             # Main application logic
└── README.md           # Documentation
```

## ⚠️ Important Notes

  * **API Limits:** Ensure you are aware of the rate limits associated with your ExchangeRate-API tier. Rate limited IPs receive HTTP code 429 responses and must wait 20 minutes.
  * **Formatting:** In "Latest Rates" mode, the tool automatically calculates the result based on your input amount ($Amount \times Rate$) for every currency in the database.

## 🤝 Attribution

[Rates By Exchange Rate API](https://www.exchangerate-api.com)

## 📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).
