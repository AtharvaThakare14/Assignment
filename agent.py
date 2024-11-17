import os
import pandas as pd
import streamlit as st
from langchain.agents import initialize_agent, AgentType
from langchain.agents import tool
from langchain.llms import OpenAI
from langchain.tools import Tool
import requests
from bs4 import BeautifulSoup
from io import StringIO



groq_api_key = "your-groq-api-key"

def load_csv(file):
    try:
        # Try reading the CSV file with 'utf-8' encoding
        df = pd.read_csv(file, encoding='utf-8')

        # Check if the DataFrame is empty
        if df.empty:
            st.error("The CSV file is empty or does not contain valid data.")
            return None
        
        # Debug: Show the first few rows
        st.write("CSV Content Preview:")
        st.write(df.head())
        
        return df
    
    except UnicodeDecodeError:
        # If the encoding fails, try 'latin1'
        try:
            df = pd.read_csv(file, encoding='latin1')
            st.write("CSV Content Preview:")
            st.write(df.head())
            return df
        except Exception as e:
            st.error(f"Error reading the CSV file with 'latin1' encoding: {e}")
            return None
    
    except pd.errors.EmptyDataError:
        st.error("The CSV file is empty or does not contain any data.")
        return None
    
    except Exception as e:
        st.error(f"Error loading CSV file: {e}")
        return None

# Scrape page title from URL
def scrape_page_title(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "No Title Found"
        return title
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"

# Scrape emails from webpage
def scrape_emails(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        emails = []  # Implement email scraping logic here
        return ", ".join(emails) if emails else "No Emails Found"
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"

# Scrape addresses from webpage
def scrape_addresses(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        addresses = []  # Implement address scraping logic here
        return ", ".join(addresses) if addresses else "No Addresses Found"
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"

# Define tools for the agent
def scrape_tool(url, task):
    if task == "Page Title":
        return scrape_page_title(url)
    elif task == "Emails":
        return scrape_emails(url)
    elif task == "Addresses":
        return scrape_addresses(url)

# Define the Agent
llm = OpenAI(temperature=0)
tools = [Tool(name="Scraping Tool", func=scrape_tool, description="Tool for scraping page titles, emails, and addresses.")]

agent = initialize_agent(
    tools, 
    llm, 
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True
)

# LangChain prompt to provide context for the agent
def agent_prompt():
    return """
    You are an AI agent tasked with scraping websites based on user instructions. You will use a CSV file of URLs provided by the user to scrape data. 
    The scraping tasks include:
    - Page Title
    - Emails
    - Addresses
    The result should be structured with the URL and the corresponding scraped data.
    """

# Run the agent on a specific task
def run_agent(csv_file, task, url_column, data_column):
    df = load_csv(csv_file)
    if df is None:
        return pd.DataFrame()  # Return an empty DataFrame if there was an error loading the CSV
    
    # Ensure the URL column exists in the uploaded CSV
    if url_column not in df.columns:
        st.error(f'CSV file must contain a "{url_column}" column for URLs.')
        return pd.DataFrame()

    # Ensure the data column exists in the uploaded CSV
    if data_column not in df.columns:
        st.error(f'CSV file must contain a "{data_column}" column for data to scrape.')
        return pd.DataFrame()

    urls = df[url_column].dropna().unique()  # Proceed if the column exists
    results = []

    # Run the agent for each URL
    for url in urls:
        response = agent.run(f"Scrape {task} from the URL: {url}")
        results.append({"URL": url, data_column: response})

    results_df = pd.DataFrame(results)
    return results_df

# Streamlit UI
def main():
    st.title("Web Scraping with Groq and LangChain")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        if df is not None:
            # Allow the user to select the URL column
            url_column = st.selectbox("Select the column that contains the URLs", df.columns)

            # Allow the user to select the column to scrape
            data_column = st.selectbox("Select the column to scrape", ["Page Title", "Emails", "Addresses"])

            if st.button("Scrape Data"):
                # Run the agent to scrape data
                with st.spinner("Scraping data..."):
                    results_df = run_agent(uploaded_file, data_column, url_column, data_column)
                    if not results_df.empty:
                        st.write(f"Scraping Results for {data_column}:")
                        st.dataframe(results_df)

                        # Option to download the results
                        csv = results_df.to_csv(index=False)
                        st.download_button(
                            label="Download Scraped Results", 
                            data=csv, 
                            file_name="scraped_results.csv", 
                            mime="text/csv"
                        )

# This check ensures that `main()` runs only when the script is executed directly
if __name__ == "__main__":
    main()
