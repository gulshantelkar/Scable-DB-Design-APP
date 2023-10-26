# Scable-DB-Design-APP

## Database Design
You can find the database design at this URL: [Database Design](https://dbdiagram.io/d/653a0decffbf5169f07cf1bc)

## Tech Stack
- Language: Python
- Framework: FastAPI (Python)
- Database: PostgreSQL
- ORM: Peewee ORM

## How to Start the App
1. Activate the virtual environment: `source venv/bin/activate`
2. Run the app using Uvicorn: `uvicorn uvicorn_conf:app --reload`

## My Approach
I have primarily focused on scalability and speed in retrieving data from the database. Additionally, we can implement caching using Redis to further optimize performance.

### Data Source
I have used Kopari JSON data because all the JSON files follow the same pattern, making it easier to work with.

### Schema Design
I have created various schemas in the database design, each corresponding to different data structures. You can explore the detailed database design on [dbdiagram.io](https://dbdiagram.io/d/653a0decffbf5169f07cf1bc).

### Active Status
I introduced an "active" status for both vendors and product types, providing a way to manage and filter data.

### Data Retrieval
I populate the required data into the database and retrieve it using normal and join queries to ensure efficient data retrieval.

### Filtering and Pagination
The app supports direct filtering by title, vendor name, handle, product type, and tags. We have implemented pagination to optimize response times.

### Available APIs
The README includes sample response JSON from the list API, which returns product data.

### Handling Duplicates
To address duplicate key issues in the variants, I introduced UUIDs as primary keys.

Feel free to explore the database design and utilize the provided APIs for your frontend needs.

### Get API
<img width="1011" alt="Screenshot 2023-10-26 at 1 05 25 PM" src="https://github.com/gulshantelkar/Scable-DB-Design-APP/assets/99161604/038da86e-675e-4ae4-82e6-31f1dca3d6e8">


### List API
<img width="1011" alt="Screenshot 2023-10-26 at 1 05 45 PM" src="https://github.com/gulshantelkar/Scable-DB-Design-APP/assets/99161604/3d2d5f1c-1c63-47ae-ac43-16f91a0c5810">



## Sample Response JSON (List API)
```json
{
     "products": [
        {
            "id": "6912539623511",
            "title": "Hydration Heaven Body Set",
            "handle": "mini-bb-mini-gabo-fs-gabo",
            "body_html": "<p data-pm-slice=\"1 1 []\">Perfect your on-the-go hydration routine by adding a travel-friendly Golden Aura Body Oil to an already heavenly duo! Our clinically proven solutions, featuring our best-selling body butter and body oil (in both sizes), expertly lock in moisture and protect against moisture loss with their luxurious, seamless, and skin-loving formulations.</p>\n<p> </p>",
            "published_at": "2023-10-19 00:30:37",
            "created_at": "2023-10-25 22:42:37.146919",
            "updated_at": "2023-10-25 22:42:37.146921",
            "vendor": "Kopari Beauty",
            "product_type": "Bundles",
            "tags": [
                "body care",
                "body care dbl points",
                "certifications-global",
                "cleanser",
                "collection-callout: sold out",
                "collection-callout:save $11",
                "F&F-Promo",
                "gluten free",
                "kit-value::6600",
                "landing-product",
                "month:2",
                "not deo",
                "personal care",
                "WEAREFAMILY"
            ],
            "variants": [
                {
                    "id": "19f3caa2-ff9f-4c55-9d37-d5717e190262",
                    "title": "Default Title",
                    "option1": "Default Title",
                    "option2": null,
                    "option3": null,
                    "sku": "RBB-R060-CBO-0020-CBO-0100",
                    "requires_shipping": true,
                    "taxable": true,
                    "featured_image": null,
                    "available": true,
                    "price": 55.0,
                    "grams": 142,
                    "compare_at_price": 66.0,
                    "position": 1,
                    "created_at": "2023-10-25 23:13:07.485673",
                    "updated_at": "2023-10-25 23:13:07.485676"
                }
            ],
            "images": [
                {
                    "id": "30823913390167",
                    "position": 1,
                    "src": "https://cdn.shopify.com/s/files/1/0777/7633/files/PDPImages_29.png?v=1697592562",
                    "width": 1480,
                    "height": 1480,
                    "created_at": "2023-10-25 23:14:06.299263",
                    "updated_at": "2023-10-25 23:14:06.299269"
                },
                {
                    "id": "30823913357399",
                    "position": 2,
                    "src": "https://cdn.shopify.com/s/files/1/0777/7633/files/PDPImages_28.png?v=1697592562",
                    "width": 1480,
                    "height": 1480,
                    "created_at": "2023-10-25 23:14:06.309869",
                    "updated_at": "2023-10-25 23:14:06.309871"
                },
                {
                    "id": "30823929544791",
                    "position": 3,
                    "src": "https://cdn.shopify.com/s/files/1/0777/7633/files/Untitleddesign_77.png?v=1697592562",
                    "width": 1480,
                    "height": 1480,
                    "created_at": "2023-10-25 23:14:06.310356",
                    "updated_at": "2023-10-25 23:14:06.310358"
                },
                {
                    "id": "30823939047511",
                    "position": 4,
                    "src": "https://cdn.shopify.com/s/files/1/0777/7633/files/GoldenAuraBodyOil_Hero.jpg?v=1697592562",
                    "width": 1480,
                    "height": 1480,
                    "created_at": "2023-10-25 23:14:06.310793",
                    "updated_at": "2023-10-25 23:14:06.310794"
                },
                {
                    "id": "30823938916439",
                    "position": 5,
                    "src": "https://cdn.shopify.com/s/files/1/0777/7633/files/BodyOil_B_A.png?v=1697592562",
                    "width": 1480,
                    "height": 1480,
                    "created_at": "2023-10-25 23:14:06.311205",
                    "updated_at": "2023-10-25 23:14:06.311206"
                },
                {
                    "id": "30823939014743",
                    "position": 6,
                    "src": "https://cdn.shopify.com/s/files/1/0777/7633/files/BodyOil_ApplicationImage.png?v=1697592562",
                    "width": 1480,
                    "height": 1480,
                    "created_at": "2023-10-25 23:14:06.311614",
                    "updated_at": "2023-10-25 23:14:06.311615"
                },
                {
                    "id": "30823938981975",
                    "position": 7,
                    "src": "https://cdn.shopify.com/s/files/1/0777/7633/files/BodyButter_B_A.png?v=1697592562",
                    "width": 1480,
                    "height": 1480,
                    "created_at": "2023-10-25 23:14:06.312213",
                    "updated_at": "2023-10-25 23:14:06.312214"
                },
                {
                    "id": "30823938949207",
                    "position": 8,
                    "src": "https://cdn.shopify.com/s/files/1/0777/7633/files/BodyButter_ApplicationImage.jpg?v=1697592562",
                    "width": 1480,
                    "height": 1480,
                    "created_at": "2023-10-25 23:14:06.312600",
                    "updated_at": "2023-10-25 23:14:06.312601"
                },
                {
                    "id": "30823931183191",
                    "position": 9,
                    "src": "https://cdn.shopify.com/s/files/1/0777/7633/files/Untitleddesign_78.png?v=1697592562",
                    "width": 1480,
                    "height": 1480,
                    "created_at": "2023-10-25 23:14:06.312968",
                    "updated_at": "2023-10-25 23:14:06.312969"
                }
            ],
            "options": [
                {
                    "id": "23cf0b6f-31a7-4419-875f-7d7f208afa4f",
                    "name": "Title",
                    "position": 1,
                    "values": [
                        "Default Title"
                    ]
                }
            ]
        },
}
