# TESTAPI

(Very) simple REST API used for testing purposes only. 

- Built with Python 3 and the [FastAPI Framework](https://github.com/tiangolo/fastapi)
- Hosted with Docker / [easypanel.io](https://easypanel.io/) on a Debian 11 VPS

## API Endpoints

| Request method | URL                         | Info  |
| -------------- | --------------------------- | ------ |
| GET            | /                           | Returns Status Code 200 OK and JSON Oneliner |
| POST           | /                           | Returns Status Code 200 OK and JSON Oneliner |
| GET            | /data/                      | Returns fictional  data |
| GET            | /users/                     | Returns even more fictional data |
| POST           | /postdata/                  | Returns data from the POST request |
| GET            | /parameter/{input_string}/  | Returns {input_string} |
| GET            | /queries/?a=foo&b=bar&c=baz | Returns input queries (foo, bar, baz) |