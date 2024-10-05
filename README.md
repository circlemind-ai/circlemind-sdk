# Circlemind SDK

## Installation
The SDK is published on PyPI. So simply run `pip install circlemind` in your preferred environment (python version >= 3.11).

## Usage
The interface is straightforward. Consider the following snippet:

```python
import circlemind

API_KEY = "xxx"
API_URL = "yyy"

cm = circlemind.Circlemind(API_KEY, API_URL)

# TODO: Set task prompt and example queries
task = "...task description goes here..."
example_queries = "...example queries go here..."

cm.set_task(task, example_queries)

# Add an artifact to memory
artifact = "...artifact content here..."
cm.add_memory(artifact)

# Retrieve artifacts from memory given a query
query = "...query to be answered here..."
artifacts = cm.get_memories(query, max_items=25)

for artifact in artifacts:
    print(artifact["content"])
```