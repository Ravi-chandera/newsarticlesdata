import requests
import streamlit as st
from bs4 import BeautifulSoup


# API Key for News API (Replace 'YOUR_API_KEY' with your actual API key)
API_KEY = 'f19f20641485460d81e4ca953abf54f3'

def fetch_articles(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


def scrape_website_content(url):
    # Send a GET request to the website
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the text content within the parsed HTML
        text_content = soup.get_text()

        # Print the extracted content
        print(text_content)
        return text_content


def main():
    st.title("Website Content Scraper")
    
    # Get user input
    keyword = st.text_input("Enter a keyword")

    if st.button("Fetch Articles"):
        # Check if keyword is provided
        if keyword:
            # Fetch news articles
            data = fetch_articles(keyword)

            # Display the articles
            st.subheader(f"Showing articles for '{keyword}':")
            i = 1
            for item in data["articles"]:
                if i > 10:
                    break
                st.write(f"**Article {i}**")
                st.write(f"Title: {item['title']}")
                st.write(f"Source: {item['source']['name']}")
                st.write(f"Published At: {item['publishedAt']}")
                st.write(f"URL: {item['url']}")

                # Scrape and display the main content
                content = scrape_website_content(item["url"])
                st.write("Main Content:")
                st.write(content)

                st.markdown("---")
                i += 1

if __name__ == "__main__":
    main()
