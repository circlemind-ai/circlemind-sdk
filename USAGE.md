<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from circlemind_sdk import CirclemindSDK
import os

with CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
) as circlemind_sdk:

    res = circlemind_sdk.get_user_plan_plan_get()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from circlemind_sdk import CirclemindSDK
import os

async def main():
    async with CirclemindSDK(
        api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
    ) as circlemind_sdk:

        res = await circlemind_sdk.get_user_plan_plan_get_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->