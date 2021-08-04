# eSamudaay
eSamudaay take home assignment.

# Steps to run.

### Clone the repo
```
git clone https://github.com/Naveen-chava/eSamudaay.git
```
### Install virtualenv
```
pip3 install virtualenv
```
or
```
sudo apt install virtualenv
```
### Create and Activate the virtualenv
```
virtualenv env_name
sourve env_name/bin/activate
```
### Install the requirements
```
pip3 install -r requirements.txt
```
### Start the Server
```
python3 manage.py runserver
```

### API Endpoint
```
http://127.0.0.1:8000/api/order-value
```

### Sample Request
```
{
  "order_items": [
    {
      "name": "bread",
      "quantity": 2,
      "price": 2200
    },
    {
      "name": "butter",
      "quantity": 1,
      "price": 5900
    }
  ],
  "distance": 1200,
  "offer": {
    "offer_type": "FLAT",
    "offer_val": 1000
  }
}
```
### Sample Response
```
{
    "order_value": 14300
}
```

Screenshots of working examples tested using postman are in the screenshots folder.
