
# AI Agent for Web Scraping with Groq and LangChain

This project is a web scraping application that leverages the power of **LangChain** and **Streamlit** to extract data like page titles, emails, and addresses from websites. It also integrates with Groq AI for enhanced AI capabilities.

---

## Features
- **Upload CSV Files**: Input a CSV file containing URLs for scraping.
- **Select Columns**: Choose columns for URLs and specify scraping tasks directly in the Streamlit app.
- **Scraping Tasks**:
  - **Page Titles**: Extract the title of the webpage.
  - **Emails**: Extract email addresses from the webpage (custom logic needed for implementation).
  - **Addresses**: Extract addresses from the webpage (custom logic needed for implementation).
- **Download Results**: Save the scraping results as a CSV file.
- **AI Agent**: Uses LangChain's agent framework for a dynamic and intelligent scraping process.

---

## Requirements
### Python Libraries
- `os`
- `pandas`
- `streamlit`
- `langchain`
- `requests`
- `beautifulsoup4`

Install the required libraries using:
```bash
pip install os pandas streamlit langchain requests beautifulsoup4
```

---

## Usage
### 1. Clone this repository:
```bash
git clone https://github.com/your-username/web-scraping-app.git
cd web-scraping-app
```

### 2. Run the application:
```bash
streamlit run app.py
```

### 3. Use the application:
- **Upload a CSV File**: Use the file uploader in the Streamlit UI to upload a CSV containing URLs.
- **Select URL Column**: Choose the column in your CSV file that contains the URLs to be scraped.
- **Choose a Scraping Task**:
  - Select one of the tasks: **Page Title**, **Emails**, or **Addresses**.
- **Scrape Data**: Click the "Scrape Data" button to start the scraping process.
  - The application will process each URL, perform the selected scraping task, and display the results in a table.
- **Download Results**:
  - After the scraping process completes, download the results as a CSV file by clicking the "Download Scraped Results" button.

---

## File Descriptions
- **`app.py`**: Main application script that runs the Streamlit UI and handles scraping logic.
- **`requirements.txt`**: List of Python dependencies for the project.

---

## Code Breakdown
### Key Components
1. **CSV Loading**:
   - Handles potential encoding issues and ensures the CSV is valid.
   - Provides a preview of the CSV content in Streamlit.

2. **Web Scraping Functions**:
   - Functions for scraping page titles, emails, and addresses using `BeautifulSoup`.

3. **LangChain Agent**:
   - Defines an agent with tools to execute scraping tasks dynamically.

4. **Streamlit UI**:
   - Allows users to upload files, select columns, and view/download results.

---

## Customization
### To Implement Email and Address Scraping:
- Update the `scrape_emails` and `scrape_addresses` functions with appropriate logic to extract email and address data from the webpage content.

### Groq API Integration:
- Replace `"your-groq-api-key"` with your actual Groq API key for enhanced AI integration.

---

## Example CSV File Format
```csv
URL
https://example.com
https://anotherexample.com
```

---

## Future Enhancements
- Add regex-based logic for email and address extraction.
- Implement logging for better error tracking.
- Support more scraping tasks (e.g., phone numbers, metadata).

---

## License
This project is licensed under the MIT License. See `LICENSE` for more information.

Happy Scraping! 🚀
