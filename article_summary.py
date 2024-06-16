import requests
from bs4 import BeautifulSoup
import ollama

def get_article_content(url):
    """Fetch the content of the article from the given URL."""
    try:
        # Sending a request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parsing the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Assuming that the main text of the article is within <article> tags
        article_content = soup.find('article')
        if article_content:
            return article_content.get_text()
        else:
            return "No article content found."
    except requests.RequestException as e:
        return str(e)


def summarize_text(text):
    """Generate a summary of the provided text using the ollama summarizer."""
    # Assuming ollama summarizer is set up locally and works with this function call
    # summary = summarizer.summarize(text, max_length=500)
    ollama_response = ollama.chat(model='llama3', messages=[
        {
            'role': 'system',
            'content': 'You are a helpful assistant with sound financial and investing knowledge.',
        },
        {
            'role': 'user',
            'content': f'Summarize the following text in less than 500 words:\n{text}',
        },
    ])
    return ollama_response['message']['content']


# # URL of the news page to be summarized (replace this with the actual URL)
# news_url = "https://example.com/news-article"
#
# # Extract the article text from the URL
# article_text = get_article_content(news_url)
# print("Original Text Extracted:", article_text[:500], "...")  # Print the first 500 characters of the original text
#
# # Summarize the article
# summary = summarize_text(article_text)
# print("\nSummary:", summary)
