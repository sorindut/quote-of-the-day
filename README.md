This is a doodle based on ❌ No-as-a-Service

**Method:** `GET`  
**Rate Limit:** `120 requests per minute per IP`

### 🔄 Example Request
```http
GET /tp
```

### ✅ Example Response
```json
{
"quote":"\"... Percy the Pup here with a cold nose, bright eyes, glossy coat and the brains of a stunned herring.\" -- Gaspode the wonder dog on 'Laddie' (Terry Pratchett, Moving Pictures)"
}
```

I'm running this in a Docker container:
```sh
docker build -t quote-service:latest -f Dockerfile .
docker compose -f docker-compose.quotes.yml up -d
```


For everything else, see the [original repo](https://github.com/hotheadhacker/no-as-a-service)