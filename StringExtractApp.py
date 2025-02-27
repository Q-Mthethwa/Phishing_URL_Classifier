import requests
import pandas as pd

def get_classification(url):
    # Prepare data to send to the API
    testing_data = url
    api_url = "the_models_api_key"
    try:
        response = requests.post(api_url, json={"input": testing_data})
        response.raise_for_status()
        predictions = response.json()  # Assuming the API returns a JSON response
        return predictions.get('prediction', [])
    except requests.RequestException as e:
        print(f"Error calling the API: {e}")
        return []

def get_test_Data():
    df = pd.read_csv("verified_online.csv")
    urlList = []
    for count, i in enumerate(df['url']):
        if df['verified'][count] == 'yes': #Load URL if verified as phishing
            urlList.append(i)
        if count == 19:
            urlList.extend([#Legit URLs
                "https://www.youtube.com/watch?v=tHb-A1SvkxY",
                "https://www.wix.com/blog/what-is-a-subdomain",
                "https://web.dev/articles/url-parts",
                "https://conferences.ieee.org/conferences_events/conferences/conferencedetails/59968",
                "https://www.oculus.com/casting/"
            ])
            break
    return urlList

def test_predictions(): #Test model performance
    testData = get_test_Data()
    results = []
    for url in testData:
        prediction = get_classification(url)
        classification = "Legit" if prediction == [0] else "Suspicious"
        results.append(f"The URL ({url}) is classified as: {classification}")
    return results
