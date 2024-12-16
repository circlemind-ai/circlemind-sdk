# CirclemindSDK

## Overview

### Available Operations

* [get_user_plan_plan_get](#get_user_plan_plan_get) - User plan
* [get_graph_configuration](#get_graph_configuration) - Graph configuration (get)
* [set_graph_configuration](#set_graph_configuration) - Graph configuration (set)
* [list_graphs](#list_graphs) - List graphs
* [create_graph](#create_graph) - Create new graph
* [delete_graph](#delete_graph) - Delete existing graph
* [download_graphml](#download_graphml) - Download graphml
* [query](#query) - Query memory
* [get_query_status](#get_query_status) - Check query request status
* [add](#add) - Add memory
* [add_from_files](#add_from_files) - Add memory (from files)
* [get_add_status](#get_add_status) - Check add request status

## get_user_plan_plan_get

Return the active plan for the current user and its usage metrics.

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

with CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
) as circlemind_sdk:

    res = circlemind_sdk.get_user_plan_plan_get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlanResponse](../../models/planresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_graph_configuration

Retrieve the configuration details of a specific graph by its name.

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

with CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
) as circlemind_sdk:

    res = circlemind_sdk.get_graph_configuration(graph_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConfigureResponse](../../models/configureresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## set_graph_configuration

Update the configuration details of a specific graph by its name.

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

with CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
) as circlemind_sdk:

    res = circlemind_sdk.set_graph_configuration(graph_name="<value>", configure_request={
        "domain": "agitated-cod.name",
        "example_queries": "<value>",
        "entity_types": [
            "<value>",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

Return the list of all existing graphs for the current user.

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

with CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
) as circlemind_sdk:

    res = circlemind_sdk.list_graphs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GraphListResponse](../../models/graphlistresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## create_graph

Create a new graph

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

with CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
) as circlemind_sdk:

    res = circlemind_sdk.create_graph(graph_name="<value>", configure_request={
        "domain": "liquid-godfather.org",
        "example_queries": "<value>",
        "entity_types": [
            "<value>",
            "<value>",
            "<value>",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `configure_request`                                                 | [models.ConfigureRequest](../../models/configurerequest.md)         | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ConfigureResponse](../../models/configureresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## delete_graph

Delete the selected graph.

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

with CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
) as circlemind_sdk:

    res = circlemind_sdk.delete_graph(graph_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## download_graphml

Generate a download URL for the graph in graphml format.

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

with CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
) as circlemind_sdk:

    res = circlemind_sdk.download_graphml(graph_name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DownloadGraphResponse](../../models/downloadgraphresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## query

Send a query request to the graph.

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

with CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
) as circlemind_sdk:

    res = circlemind_sdk.query(graph_name="<value>", query_request={
        "query": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `query_request`                                                     | [models.QueryRequest](../../models/queryrequest.md)                 | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.QueryResponse](../../models/queryresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_query_status

Return the status of an existing query request.

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

with CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
) as circlemind_sdk:

    res = circlemind_sdk.get_query_status(graph_name="<value>", request_id="<id>", request_time=816039)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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

## add

Create a new memory in the graph using raw text.

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

with CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
) as circlemind_sdk:

    res = circlemind_sdk.add(graph_name="<value>", insert_request={
        "memory": "<value>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `insert_request`                                                    | [models.InsertRequest](../../models/insertrequest.md)               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.InsertResponse](../../models/insertresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## add_from_files

Create a new memory in the graph from files.

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

with CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
) as circlemind_sdk:

    res = circlemind_sdk.add_from_files(graph_name="<value>", body_post_insert_files_graph_graph_name_files_post={
        "files": [
            {
                "file_name": "example.file",
                "content": open("example.file", "rb"),
            },
            {
                "file_name": "example.file",
                "content": open("example.file", "rb"),
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `graph_name`                                                                                                    | *str*                                                                                                           | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `body_post_insert_files_graph_graph_name_files_post`                                                            | [models.BodyPostInsertFilesGraphGraphNameFilesPost](../../models/bodypostinsertfilesgraphgraphnamefilespost.md) | :heavy_check_mark:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.InsertResponse](../../models/insertresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## get_add_status

Return the status of an existing add request.

### Example Usage

```python
from circlemind_sdk import CirclemindSDK
import os

with CirclemindSDK(
    api_key_header=os.getenv("CIRCLEMINDSDK_API_KEY_HEADER", ""),
) as circlemind_sdk:

    res = circlemind_sdk.get_add_status(graph_name="<value>", request_id="<id>", request_time=877284)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `graph_name`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
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