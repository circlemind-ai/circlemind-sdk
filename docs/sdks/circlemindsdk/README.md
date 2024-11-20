# CirclemindSDK

## Overview

### Available Operations

* [get_graph_configuration](#get_graph_configuration) - Get Graph Configuration
* [create_graph_configuration](#create_graph_configuration) - Post Graph Configuration
* [get_graph_list](#get_graph_list) - Get Graph List
* [create_graph](#create_graph) - Create Graph
* [create_query](#create_query) - Post Query
* [get_query_handler](#get_query_handler) - Get Query Handler
* [create_insert](#create_insert) - Post Insert
* [create_graph_files](#create_graph_files) - Add Files
* [get_insert_handler](#get_insert_handler) - Get Insert Handler

## get_graph_configuration

Get Graph Configuration

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.get_graph_configuration(graph_name="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConfigureResponse](../../models/configureresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_graph_configuration

Post Graph Configuration

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.create_graph_configuration(graph_name="<value>", configure_request={
    "domain": "agitated-cod.name",
    "example_queries": "<value>",
    "entity_types": [
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
| `graph_name`                                                        | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | N/A                                                                 |
| `configure_request`                                                 | [models.ConfigureRequest](../../models/configurerequest.md)         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConfigureResponse](../../models/configureresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_graph_list

Get Graph List

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.get_graph_list()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
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

res = s.create_graph(graph_name="<value>", configure_request={
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
| `graph_name`                                                        | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | N/A                                                                 |
| `configure_request`                                                 | [models.ConfigureRequest](../../models/configurerequest.md)         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_query

Post Query

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.create_query(graph_name="<value>", query_request={
    "query": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | N/A                                                                 |
| `query_request`                                                     | [models.QueryRequest](../../models/queryrequest.md)                 | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.QueryResponse](../../models/queryresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_query_handler

Get Query Handler

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.get_query_handler(graph_name="<value>", request_id="<id>", request_time=362783)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | N/A                                                                 |
| `request_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `request_time`                                                      | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RequestStatus](../../models/requeststatus.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_insert

Post Insert

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.create_insert(graph_name="<value>", memory_request={
    "memory": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | N/A                                                                 |
| `memory_request`                                                    | [models.MemoryRequest](../../models/memoryrequest.md)               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InsertResponse](../../models/insertresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## create_graph_files

Add Files

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.create_graph_files(graph_name="<value>", body_add_files_graph_graph_name_files_post={
    "files": [
        {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `graph_name`                                                                                      | *Nullable[str]*                                                                                   | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `body_add_files_graph_graph_name_files_post`                                                      | [models.BodyAddFilesGraphGraphNameFilesPost](../../models/bodyaddfilesgraphgraphnamefilespost.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_insert_handler

Get Insert Handler

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

s = CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
)

res = s.get_insert_handler(graph_name="<value>", request_id="<id>", request_time=895985)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *Nullable[str]*                                                     | :heavy_check_mark:                                                  | N/A                                                                 |
| `request_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `request_time`                                                      | *int*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RequestStatus](../../models/requeststatus.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |