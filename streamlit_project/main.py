import streamlit as st
from functions.retreiver import retreiver

def main():
    st.title('Web Scraper App')
    st.write("Enter the URL of the website you want to scrape:")

    # Input field for user to enter URL
    url = st.text_input("URL:")
    
    if st.button("Scrape"):
        if url:
            # Call scrape_website function from scrape.py
            result = retreiver(url)
            
            # Display the scraped text content
            st.subheader("Scraped Text:")
            st.write(result if result else "No text scraped. Check the URL or try again.")

if __name__ == "__main__":
    main()
