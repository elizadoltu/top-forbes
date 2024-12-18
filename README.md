# Forbes Billionaires Crawler

A Python-based tool for scraping information about the top 200 billionaires from Forbes, saving the data into a JSON file, processing it, and storing it in a MongoDB database. It also includes a set of scripts for analyzing the data, with results saved in a dedicated folder.

This project is designed to be modular, easy to use, and open for contributions.

## Table of Contents
- [About the project](#about-the-project)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Commands](#commands)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

<a name="about-the-project" />

## About the project

The Forbes Billionaires Crawler (B - 18) scrapes data from [Forbes Billionaires](https://www.forbes.com/billionaires/), processes it, and saves the results to JSON files, text files, and a MongoDB database. It includes scripts to perform the following analyses:

- Count the number of unique industries and their occurrences.
- Determine how many billionaires are U.S. citizens and how many are not.
- Identify the top 10 youngest billionaires.

<a name="features" />

## Features

- Scrape billionaire data and save it to a JSON file.
- Store the data in MongoDB for querying and analysis.
- Analyze billionaire data with pre-built scripts:
  - Count unique industries and their occurrences.
  - Find out how many billionaires are U.S. citizens or not.
  - Get the top 10 youngest billionaires.
- Save results of the analysis into text files for easy reference.

<a name="project-structure" />

## Project Structure

```bash
top-forbes/
│
├── forbes.py                 # Scrapes data from Forbes and saves it as a JSON file
├── billionaires_data.json    # JSON file containing scraped billionaire data
│
├── scripts/                  # Folder containing analysis scripts
│   ├── save-to-database.py           # Saves data to MongoDB
│   ├── count-industries.py           # Counts unique industries and occurrences
│   ├── how-many-us-citizens.py       # Determines how many are U.S. citizens
│   ├── get-top-10-youngest-billionaires.py  # Finds the top 10 youngest billionaires
│
├── auto/                     # Folder for storing the output of analysis scripts
│   ├── industry_counts.txt           # Results of unique industry analysis
│   ├── us_citizens_count.txt         # Results of U.S. citizenship analysis
│   ├── youngest_billionaires.txt     # Results of youngest billionaires analysis
│
├── requirements.txt          # List of Python dependencies
├── commands.txt              # Commands to run the project
├── .env                      # Environment variables for database connection
├── README.md                 # Documentation
├── .gitignore                
└── LICENSE                   # License file
```

<a name="getting-started" />

## Getting Started

<a name="prerequisites" />

### Prerequisites

Before you start, ensure you have the following:
1. **Python 3.8+** installed on your system
2. **MongoDB** installed and running, or access to a MOngoDB Atlas cluster
3. Clone this repository

```bash
git clone https://github.com/your-username/forbes-billionaires-crawler.git
cd forbes-billionaires-crawler
```

<a name="setup" />

### Setup
1. Install dependencies from **`requirements.txt`**:
```bash
pip install -r requirements.txt
```
2. Create an **`env`** file in the root directory and add your MongoDB connection string:
```env
DATABASE_CONNECTION=mongodb+srv://<username>:<password>@<cluster-url>/forbes?retryWrites=true&w=majority
```
3. Or use the **`commands.txt`** file for step-by-step instructions on running the project and install the dependencies:
```bash
cat commands.txt
```

<a name="commands" />

### Commands

Refer to the **`commands.txt`** file for detailed instructions on running the scripts. Here are some examples:
1. Run the **scraper** to collect data and save it to a JSON file:
```bash
python forbes.py
```
2. Save the scraped data into MongoDB:
```bash
python scripts/save-to-database.py
```
3. Run the analysis scripts:
    - **Count industries:**
    ```bash
    python scripts/count-industries.py
    ```
    Output saved to **`auto/count-industries.txt`**
   - **Count U.S. citizens:**
   ```bash
   python scripts/how-many-us-citizens.py
   ```
   Output saved to **`auto/us-citizenship.txt`**
   - **Get the top 10 youngest billionaires**
   ```bash
   python scripts/get-top-10-youngest-billionaires.py
   ```
   Output saved to **`auto/top_10_youngest_billionaires.txt`**

<a name="usage" />

## Usage

### Example: Count U.S. Citizen
The **`how-many-us-citizens.py`** script outputs a count of U.S. citizens and non-citizens among the billionaires:
```javascript
American Citizens: 100
Non-American citizens: 100
```

### Example: Top 10 Youngest Billionaires
The **`get-top-10-youngest-billionaires.py`** script outputs the top 10 youngest billionaires out of first 200:
```javascript
Rank: 31, First Name: None, Last Name: Mateschitz, Age: 31, Source Of Wealth: Red Bull, Net Worth: 39600.0, City: Salzburg, Citizenship: Austria, 
Rank: 25, First Name: None, Last Name: Walton, Age: 38, Source Of Wealth: Walmart, Net Worth: 33900.0, City: Chicago, Citizenship: United States, 
Rank: 122, First Name: None, Last Name: Durov, Age: 39, Source Of Wealth: Messaging app, Net Worth: 15500.0, City: Dubai, Citizenship: United Arab Emirates,
...
```

<a name="constributing" />

## COntributing 
I welcome contributions from the community! To contribute:
1. Fork the repository
2. Create a feature branch
```bash
git checkout -b feature/your-feature-name
```
3. Commit changes:
```bash
git commit -m "Add your feature description"
```
4. Push to your branch
```bash
git push origin feature/your-feature-name
```
5. Open a pull request

Make sure to update the documentation and test your features before submitting

<a name="license" />

## License

This project is distributed under the MIT License. See **`LICENSE`**

<a name="acknowledgements">

## Acknowledgements
- Forbes Billionaires for dataset
- Libraries used
    - Requests
    - PyMongo


  
