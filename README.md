# Gender Classifier API

A REST API that predicts the gender of a name using the Genderize.io API.

## Endpoint

`GET /api/classify?name={name}`

## Example Request
`GET /api/classify?name=John`

## Example Response

```json
{
  "status": "success",
  "data": {
    "name": "John",
    "gender": "male",
    "probability": 1.0,
    "sample_size": 2692560,
    "is_confident": true,
    "processed_at": "2026-04-14T16:00:00Z"
  }
}
```

## Error Responses

| Status Code | Reason |
|-------------|--------|
| 400 | Missing or empty name |
| 422 | Invalid name (non-alphabetic) |
| 502 | Genderize API unreachable |

## Tech Stack

- Python
- FastAPI
- httpx
- Uvicorn