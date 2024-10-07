# Circlemind SDK

## Installation
The SDK is published on PyPI. So simply run `pip install circlemind` in your preferred environment (python version >= 3.11).

## Usage
The interface is straightforward. Consider the following snippet:

```python
import circlemind

API_KEY = "xxx"
cm = circlemind.Circlemind(API_KEY)

# Optionally update the task prompt and queries associated with your API_KEY
TASK = "...task description goes here..."
PROMPT = "...example queries go here..."
cm.configure(TASK, PROMPT)


# Add an artifact to memory
artifact = "...artifact content here..."
cm.add(artifact)

# Retrieve artifacts from memory given a query
query = "...query to be answered here..."
artifacts = cm.query(query, max_items=25)

for artifact in artifacts:
    print(artifact["content"])
```