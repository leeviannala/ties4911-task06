# coding: utf-8
import urllib.request
from ibm_settings import WatsonAccountSettings
import json
from pathlib import Path
import os

class DiscoveryNews():
    _root_url = "https://gateway.watsonplatform.net/discovery/"
    _url = "https://gateway.watsonplatform.net/discovery/api/v1/environments/system/collections/news-en/query?version=2017-11-07&aggregation=filter%28enriched_title.entities.type%3A%3ACompany%29.term%28enriched_title.entities.text%29.timeslice%28crawl_date%2C1day%29.term%28enriched_text.sentiment.document.label%29&filter={0}&highlight=true&passages.count=5&query="

    def __init__(self, username, password):
        password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, self._root_url, username, password)
        self.handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    def query_url(self, company_name):
        return self._url.format(company_name)

    def query(self, company_name, bin_file_path):
        url = self.query_url(company_name)
        opener = urllib.request.build_opener(self.handler)
        opener.open(url)
        # Install the opener.
        # Now all calls to urllib.request.urlopen use our opener.
        urllib.request.install_opener(opener)       

        resource = urllib.request.urlopen(url)
        with open(bin_file_path, 'wb') as f:
            f.write(resource.read())
        return bin_file_path


class QueryResult():
    _jsonObj = None
    
    def __init__(self, bin_file_path):
        with open(bin_file_path, 'r', encoding='utf-8') as f:
            raw_content = ''.join(f.readlines())
            self._jsonObj = json.loads(raw_content)
    
    def matching_results(self):
        return self._jsonObj['matching_results']
    
    def aggregations(self):
        return self._jsonObj['aggregations']

    def aggregation_keys(self):
        return [obj['key'] for obj in self._jsonObj['aggregations'][0]['aggregations'][0]['results']]

    def aggregation_summary(self):
        collection = []
        for obj in self._jsonObj['aggregations'][0]['aggregations'][0]['results']:
            positives = 0
            neutral = 0
            negatives = 0

            for aggr_results in obj['aggregations'][0]['results']:
                for aggr_inner_results in aggr_results['aggregations'][0]['results']:
                    aggr_inn_key = aggr_inner_results['key']
                    aggr_inn_res = aggr_inner_results['matching_results']
                    if aggr_inn_key == 'positive':
                        positives += aggr_inn_res
                    elif aggr_inn_key == 'neutral':
                        neutral += aggr_inn_res
                    elif aggr_inn_key == 'negative':
                        negatives += aggr_inn_res
            
            obj_result = {
                "key" : obj['key'],
                "result_count" : obj['matching_results'],
                "positives" : positives,
                "neutral" : neutral,
                "negatives" : negatives
            }
            collection.append(obj_result)
        return collection  

    def passages(self):
        return self._jsonObj['passages']

    def results(self):
        return self._jsonObj['results']

    def results_summary(self):
        collection = []
        for result in self._jsonObj['results']:
            entities = []
            for entity in result['enriched_text']['entities']:
                entities.append({
                    "sentiment" : entity['sentiment'],
                    "text" : entity['text'],
                    "relevance" : entity['relevance'],
                    "count" : entity['count']
                })

            collection.append({
                "url" : result['url'],
                "host" : result['host'],
                "title" : result['title'],
                "date" : result['publication_date'],
                "title_sentiment" : result['enriched_title']['sentiment']['document'],
                "enriched_text" : entities
            })
            
        return collection

#"https://gateway.watsonplatform.net/discovery/api/v1/environments/system/collections/news-en/query?version=2017-11-07&aggregation=filter%28enriched_title.entities.type%3A%3ACompany%29.term%28enriched_title.entities.text%29.timeslice%28crawl_date%2C1day%29.term%28enriched_text.sentiment.document.label%29&filter=IBM&highlight=true&passages.count=5&query="
def example(company_name):
    bin_file_name = "discovery_{0}.bin".format(company_name)
    directory_name = "queries"
    dir_file_path = os.path.join(os.getcwd(), directory_name)
    bin_file_path = os.path.join(os.getcwd(), directory_name, bin_file_name)

    if not os.path.exists(dir_file_path):
        os.makedirs(dir_file_path)

    query_file = Path(bin_file_path)
    if not query_file.is_file():
        acc = WatsonAccountSettings()
        dn = DiscoveryNews(acc.username(), acc.password())
        dn.query(company_name, bin_file_path)

    q = QueryResult(bin_file_path)
    print(q.matching_results())
    print("")
    print(q.aggregation_summary())
    print("")
    print(q.results_summary())
    print("")

example("IBM")
example("Apple")
example("Nokia")
example("Google")
example("UPM")
example("Tesla")