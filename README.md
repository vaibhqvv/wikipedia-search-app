
# Wikipedia Search Flask Application

This is a simple Flask web application that allows users to search for summaries of Wikipedia articles. The application uses the `wikipedia-api` library to fetch data from Wikipedia.

## Features

- Simple search form to query Wikipedia articles
- Displays the first 10000 characters of the Wikipedia summary for the searched term
- Handles cases where the search term might refer to multiple topics or the page does not exist

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/wikipedia-search-app.git
   cd wikipedia-search-app
   ```

2. Create a virtual environment:

   ```bash
   python -m venv env
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```

   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Create `requirements.txt`

Add the following content to a `requirements.txt` file in your project directory:

   ```txt
   Flask
   wikipedia-api
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Use the search form to enter a term and view the Wikipedia summary.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.