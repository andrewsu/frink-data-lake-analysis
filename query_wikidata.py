import requests
import sys

def query_wikidata(title):
    """
    Query Wikidata for items with a title that exactly matches the input string.
    """
    url = "https://www.wikidata.org/w/api.php"
    params = {
        "action": "wbsearchentities",
        "format": "json",
        "language": "en",
        "type": "item",
        "search": title,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get("search", [])
        exact_matches = [item for item in results if item.get("label").lower() == title.lower()]
        return exact_matches
    else:
        print("Failed to query Wikidata.", file=sys.stderr)
        return []

def process_file(file_path):
    """
    Read a text file line by line, query Wikidata for each line, and output results.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()  # Remove any leading/trailing whitespace
        if line:  # Check if line is not empty
            matches = query_wikidata(line)
            if matches:
                for match in matches:
                    print(f"{line}\tQ{match.get('id')}")
            else:
                print(f"{line}\tNone")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py path_to_your_file.txt", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    process_file(file_path)

