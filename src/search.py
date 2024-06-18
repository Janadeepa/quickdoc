# src/search.py

def search_documentation(query, documentation):
    results = []
    for section in documentation:
        if query in section.lower():  # Perform case-insensitive search
            results.append(section)
    return results

# Example usage:
if __name__ == "__main__":
    documentation = [
        "### Function A\n\nDescription of Function A",
        "### Function B\n\nDescription of Function B",
        "### Function C\n\nDescription of Function C"
    ]
    query = "function"
    search_results = search_documentation(query, documentation)
    print("Search results:")
    for result in search_results:
        print(result)
