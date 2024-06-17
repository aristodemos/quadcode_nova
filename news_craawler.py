import requests
from article_summary import get_article_content
from article_summary import summarize_text
from transformers import pipeline


model_name = "ProsusAI/finbert"  # https://huggingface.co/ProsusAI/finbert Medium Post: https://medium.com/prosus-ai-tech-blog/finbert-financial-sentiment-analysis-with-bert-b277a3607101
sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)


def google_search(query, api_key, search_engine_id):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}"
    response = requests.get(url)
    results = response.json()
    return results


def google_search_ext(query, start=1, sort_by_date=True):
    params = {
        'q': query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'start': start
    }
    if sort_by_date:
        params['sort'] = 'date'

    url = "https://www.googleapis.com/customsearch/v1"
    response = requests.get(url, params=params)
    results = response.json()
    return results


def parse_results(results):
    links = []
    for item in results.get('items', []):
        title = item['title']
        link = item['link']
        snippet = item['snippet']
        print(f"Title: {title}\nLink: {link}\nSnippet: {snippet}")
        links.append(link)
    return links


query_terms = ["oil latest news", "crypto latest"]
for query in query_terms:
    # Request the first page of results sorted by date
    results = google_search_ext(query, start=1, sort_by_date=True)
    links = parse_results(results)
    for link in links:
        summary = summarize_text(get_article_content(link))
        sentiment = sentiment_pipeline(summary)
        print(f"Summary:\n{summary}\nSentiment:{sentiment}")


    print(f"\n\n--------------------------------------------------------------------------\n\n")

# Request the second page of results
results = google_search_ext(query, start=1, sort_by_date=True)
parse_results(results)
