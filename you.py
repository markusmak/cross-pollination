import requests

def get_ai_snippets_for_query(query):
    headers = {"X-API-Key": ''}
    params = {"query": query}
    return requests.get(
        f"https://api.ydc-index.io/search?query={query}",
        params=params,
        headers=headers,
    ).json()
results = get_ai_snippets_for_query("reasons to smile")
for res in results['hits']:
    print('=======================')
    print(f"Title: {res['title']}")
    print(f"Description: {res['description']}")
    print(f"Description: {res['snippets']}")