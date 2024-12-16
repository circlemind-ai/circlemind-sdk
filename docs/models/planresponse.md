# PlanResponse

Data model for plan response.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `requests_count`                                     | *float*                                              | :heavy_check_mark:                                   | Total number of requests used for the current period |
| `requests_max`                                       | *int*                                                | :heavy_check_mark:                                   | Number of available requests for the active plan     |
| `plan_id`                                            | *str*                                                | :heavy_check_mark:                                   | N/A                                                  |
| `plan_ttl`                                           | *int*                                                | :heavy_check_mark:                                   | N/A                                                  |