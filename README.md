# ties4911-task06
University of jyväskylä course Ties4911 task 6

## Discovery News

### Setup

1. Login to IBM bluemix (https://console.bluemix.net/dashboard/apps/) and find your service credentials.
2. Open ibm_settings.py file. 
3. Remove raise exceptions and uncomment the return lines. 
4. Place your credentials.

### matching_results

Returns a count of all hits.

### aggregation_summary

Returns and list of json objects in following format:
```json
{
    "key" : "string",
    "positives" : "number",
    "neutral" : "number",
    "negatives" : "number",
    "result_count" : "number"
}
```

Key is an reference to all keywords found in news articles. For example IBM aggregation_summary is:
```json
[
    {"key": "IBM", "neutral": 231, "negatives": 953, "positives": 3013, "result_count": 4197}, 
    {"key": "Microsoft", "neutral": 28, "negatives": 284, "positives": 640, "result_count": 952}, 
    {"key": "International Business Machines Corp.", "neutral": 1, "negatives": 5, "positives": 604, "result_count": 610}, 
    {"key": "Apple", "neutral": 13, "negatives": 198, "positives": 224, "result_count": 435}, 
    {"key": "Google", "neutral": 12, "negatives": 82, "positives": 297, "result_count": 391}, 
    {"key": "Oracle", "neutral": 6, "negatives": 30, "positives": 335, "result_count": 371}, 
    {"key": "Amazon", "neutral": 5, "negatives": 59, "positives": 261, "result_count": 325}, 
    {"key": "Intel", "neutral": 16, "negatives": 120, "positives": 171, "result_count": 307}, 
    {"key": "CEO", "neutral": 7, "negatives": 56, "positives": 150, "result_count": 213}, 
    {"key": "AI", "neutral": 0, "negatives": 15, "positives": 174, "result_count": 189}
]
```
### results_summary

Returns a list of all news references to the company. Example for IBM:
```json
[
    {
        "url": "https://www.freelancer.de/projects/graphic-design/design-logo-16321812/", 
        "title": "Design a logo by COREnglish", 
        "date": "2018-02-18T13:56:00Z", 
        "title_sentiment": {"score": 0, "label": "neutral"}, 
        "enriched_text": 
            [
                {
                    "sentiment": {"score": 0.635624, "label": "positive"}, 
                    "count": 2, 
                    "relevance": 0.975108, 
                    "text": "Mehr"
                }, 
                {
                    "sentiment": {"score": 0, "label": "neutral"}, 
                    "count": 1, 
                    "relevance": 0.69245, 
                    "text": "Tagen Offen"
                }, 
                {
                    "sentiment": {"score": 0.684175, "label": "positive"}, 
                    "count": 2, 
                    "relevance": 0.637626, "text": "Dasha"}, 
                    {
                        "sentiment": {"score": 0, "label": "neutral"}, 
                        "count": 1, 
                        "relevance": 0.483074, 
                        "text": "Durchschnitt"
                    }, 
                    {
                        "sentiment": {"score": 0, "label": "neutral"}, 
                        "count": 1, 
                        "relevance": 0.483074, 
                        "text": "$15"
                    }, 
                    {
                        "sentiment": {"score": 0, "label": "neutral"}, 
                        "count": 1, 
                        "relevance": 0.483074, 
                        "text": "$19"
                    }, 
                    {
                        "sentiment": {"score": 0, "label": "neutral"}, 
                        "count": 1, 
                        "relevance": 0.483074, 
                        "text": "$20"
                    }, 
                    {
                        "sentiment": {"score": 0, "label": "neutral"}, 
                        "count": 1, 
                        "relevance": 0.483074, 
                        "text": "$25"
                    }
            ],
        "host": "freelancer.de"
    }
]
```