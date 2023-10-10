# CRUD_ENDPOINT

Get All Products
HTTP Method: GET

Endpoint: /api/v1/products/

Description: Retrieve a list of all products.

Response: [
    {
        "id": 1,
        "title": "First Product",
        "price": "0.00"
    },


HTTP Method: POST

Endpoint: /api/v1/products/

request_body : 
{
    "title": "Second Product",
    "price": 8000
}



HTTP Method: DELETE
Endpoint: /api/v1/products/{product_id}/
Response: 
{
  "message": "Deleted Successfully"
}
