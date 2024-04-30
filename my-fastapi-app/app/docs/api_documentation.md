# API Documentation

## Buffer Processing

Endpoint: `/buffer`

### Description

This endpoint allows you to perform a buffer geoprocessing operation using arcpy.

### Request

- Method: POST
- Content-Type: application/json

#### Parameters

| Name     | Type   | Description                           |
|----------|--------|---------------------------------------|
| input    | string | The path to the input feature class.   |
| output   | string | The path to the output feature class.  |
| distance | number | The buffer distance in the input units.|

### Response

- Status Code: 200 OK
- Content-Type: application/json

#### Body

The response body will contain a JSON object with the following properties:

| Name     | Type   | Description                           |
|----------|--------|---------------------------------------|
| success  | bool   | Indicates if the buffer operation was successful. |
| message  | string | A message describing the result of the buffer operation. |

### Example

#### Request

```json
POST /buffer
Content-Type: application/json

{
  "input": "path/to/input/feature_class",
  "output": "path/to/output/feature_class",
  "distance": 1000
}
```

#### Response

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
  "success": true,
  "message": "Buffer operation completed successfully."
}
```
```

This file provides documentation for the API, specifically for the `/buffer` endpoint that allows users to perform a buffer geoprocessing operation using arcpy. It includes information about the request parameters, response format, and an example request and response.