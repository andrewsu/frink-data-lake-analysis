import requests
import sys

def query_wikidata_for_judges(title):
    """
    Query Wikidata for items with a title that matches the input string and has an occupation of "judge".
    """
    sparql_query = """
    SELECT ?item ?itemLabel WHERE {
      SERVICE wikibase:mwapi {
        bd:serviceParam wikibase:endpoint "www.wikidata.org";
                        wikibase:api "EntitySearch";
                        mwapi:search "%s";
                        mwapi:language "en".
        ?item wikibase:apiOutputItem mwapi:item.
      }
      ?item wdt:P106 wd:Q16533.  # P106 is the property for occupation, Q16533 for "judge"
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    """ % (title.replace('"', '\\"'))

    url = "https://query.wikidata.org/sparql"
    response = requests.get(url, params={'query': sparql_query, 'format': 'json'})
    if response.status_code == 200:
        results = response.json().get("results", {}).get("bindings", [])
        return results
    else:
        print("Failed to query Wikidata.", file=sys.stderr)
        return []

def process_file(file_path):
    """
    Read a text file line by line, query Wikidata for each line for items with an occupation of "judge", and output results.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()  # Remove any leading/trailing whitespace
        if line:  # Check if line is not empty
            results = query_wikidata_for_judges(line)
            if results:
                for result in results:
                    item_id = result["item"]["value"].split("/")[-1]  # Extracting QID from the full URI
                    print(f"{line}\t{item_id}")
            else:
                print(f"{line}\tNone")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py path_to_your_file.txt", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    process_file(file_path)

