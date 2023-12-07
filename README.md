## Documentation
### About
Simple application for manage products build with Django. This application have some features:
1. Create product.
2. Show list and detail products.
3. Update product.
4. Delete product.
5. list category.
6. list status.
7. Collecting data product from 3rd-party API.

For all features we provide API and also Web based.

### API
This application implement RESTfull API architecture and using PostgreSql database. There are some endpoints we provide.

##### Create product
- Endpoint:
```sh
[POST] {base_url}/api/product
```
- Request Body:
```json
{
  "nama_produk": "ThinkPad T470s",
  "harga": "23250000",
  "kategori_id" : 1,
  "status_id": 1
}
```
- Response Body:
```json
{
  "id_produk": 1,
  "nama_produk": "ThinkPad T470s",
  "harga": "23250000",
  "kategori": "Laptop",
  "status": "bisa dijual"
}
```
##### Show list and detail products
###### List
- Endpoint:
```sh
[GET] {base_url}/api/product
```
- Response Body:
```json
[
  {
    "id_produk": 1,
    "nama_produk": "ThinkPad T470s",
    "harga": "23250000",
    "kategori": "Laptop",
    "status": "bisa dijual"
  },
  {
    "id_produk": 2,
    "nama_produk": "ThinkPad T470",
    "harga": "21250000",
    "kategori": "Laptop",
    "status": "bisa dijual"
  }
]
```
###### Detail
- Endpoint:
```sh
[GET] {base_url}/api/product/1
```
- Response Body:
```json
{
  "id_produk": 1,
  "nama_produk": "ThinkPad T470s",
  "harga": "23250000",
  "kategori": "Laptop",
  "status": "bisa dijual"
}
```
##### Update product
- Endpoint:
```sh
[PUT] {base_url}/api/product/1
```
- Request Body:
```json
{
  "nama_produk": "ThinkPad T470s",
  "harga": "23250000",
  "kategori_id" : 1,
  "status_id": 2
}
```
- Response Body:
```json
{
  "id_produk": 1,
  "nama_produk": "ThinkPad T470s",
  "harga": "23250000",
  "kategori": "Laptop",
  "status": "tidak bisa dijual"
}
```
##### Delete product
- Endpoint:
```sh
[DELETE] {base_url}/api/product/1
```
##### List Category
- Endpoint:
```sh
[GET] {base_url}/api/category
```
- Response Body:
```json
[
  {
    "id_kategori": 1,
    "nama_kategori": "Laptop",
  },
  {
    "id_kategori": 2,
    "nama_kategori": "Printer",
  }
]
```
##### List Status
- Endpoint:
```sh
[GET] {base_url}/api/status
```
- Response Body:
```json
[
  {
    "id_status": 1,
    "nama_Status": "bisa dijual",
  },
  {
    "id_kategori": 2,
    "nama_kategori": "tidak bisa dijual",
  }
]
```
##### Collecting data product from 3rd-party API.
- Endpoint:
```sh
[POST] {base_url}/api/collect
```
- Request Body:
```json
{
  "username": "username",
  "password": "password"
}
```
- Response Body:
```json
{
  "success": "Data collected and saved successfully"
}
```
### Admin Dashboard
This application implement Django admin for build admin dashboard. In admin dashboard you can manage all products, category and status easier.

This is preview of admin dashboard [watch now](https://drive.google.com/file/d/11wwLYIvpBx-6aL-Ud-JhArQPqdt2RIzk/view?usp=sharing)

### Installation
We assume you already have python3, pip3, venv installed. And dont forget to prepare database (we use postgresql to store data in the database).

We recommand using linux for better development and installation, and this installation we assume you already familiar using terminal. 

Open terminal and follow this step:

- clone the repository
```sh
git clone https://github.com/m-hari16/fast-print-product-service.git
```
- go to directory project and create vitual environment then activate
```sh
cd fast-print-product-service
```
```sh
python3 -m venv venv
```

```sh
source venv/bin/activate
```
- install requirements pacakge
```sh
pip3 install -r requirements.tx
```
- setup database in .env file
```sh
cp .env.example .env
```
open the .env file and adjust based on your database credentials

- run migration
```sh
python3 manage.py migrate
```
- cretae superuser for access in admin dashboard
```sh
python3 manage.py createsuperuser
```
fill username, email and password for admin credentials

- run project
```sh
python3 manage.py runserver
```
finally installation success and you can open web browser to this link 'http://localhost:8000/admin' to access admin dashboard

Please refer to API docs, we provide endpoint to collect data from 3rd-party API. it easy to use.