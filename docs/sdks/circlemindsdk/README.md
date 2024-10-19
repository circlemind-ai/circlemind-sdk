# CirclemindSDK

## Overview

### Available Operations

* [get_configuration](#get_configuration) - Get Graph Configuration
* [configure](#configure) - Change Graph Configuration
* [list_graphs](#list_graphs) - List Graphs
* [create_graph](#create_graph) - Create Graph
* [query](#query) - Start Reasoning
* [get_reasoning](#get_reasoning) - Get Reasoning
* [add](#add) - Post Memory

## get_configuration

Get Graph Configuration

### Example Usage

```python
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

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConfigureResponse](../../models/configureresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## configure

Change Graph Configuration

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.configure(graph_id="<id>", configure_request={
    "domain": "ambitious-ceramics.com",
    "example_queries": "<value>",
    "entity_types": [
        "<value>",
        "<value>",
        "<value>",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `configure_request`                                                 | [models.ConfigureRequest](../../models/configurerequest.md)         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConfigureResponse](../../models/configureresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## list_graphs

List Graphs

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.list_graphs()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_graph

Create Graph

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.create_graph(graph_id="<id>", configure_request={
    "domain": "liquid-godfather.org",
    "example_queries": "<value>",
    "entity_types": [
        "<value>",
        "<value>",
        "<value>",
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `configure_request`                                                 | [models.ConfigureRequest](../../models/configurerequest.md)         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## query

Start Reasoning

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.query(graph_id="<id>", reasoning_request={
    "query": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `reasoning_request`                                                 | [models.ReasoningRequest](../../models/reasoningrequest.md)         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ReasoningResponse](../../models/reasoningresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_reasoning

Get Reasoning

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.get_reasoning(graph_id="<id>", request_id="<id>", request_time=982149)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `request_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `request_time`                                                      | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ReasoningStatusResponse](../../models/reasoningstatusresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## add

Post Memory

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.add(graph_id="<id>", memory_request={
    "memory": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `memory_request`                                                    | [models.MemoryRequest](../../models/memoryrequest.md)               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MemoryResponse](../../models/memoryresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |