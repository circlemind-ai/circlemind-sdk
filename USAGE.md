<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.get_configuration(graph_id="<id>")

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from circlemind_sdk import CirclemindSDK
import os

async def main():
    s = CirclemindSDK(
        api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
    )
    res = await s.get_configuration_async(graph_id="<id>")
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->