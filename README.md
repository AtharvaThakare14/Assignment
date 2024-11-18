
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

---

## usage
Clone this repository:
```bash
git clone https://github.com/your-username/web-scraping-app.git

## Run the application:
```bash
streamlit run app.py





