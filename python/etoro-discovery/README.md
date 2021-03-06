# etoro-discovery
The discovery API allows you to discover customers in the eToro network. It is important to note that only customers who have opted-in for discovery will be shown by this API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 0.6.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import etoro_discovery 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import etoro_discovery
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import etoro_discovery
from etoro_discovery.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = etoro_discovery.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_discovery.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_discovery.DefaultApi(etoro_discovery.ApiClient(configuration))

try:
    # MetaData
    api_instance.get_metadata()
except ApiException as e:
    print("Exception when calling DefaultApi->get_metadata: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_discovery.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_discovery.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_discovery.DefaultApi(etoro_discovery.ApiClient(configuration))
period = 'SixMonthsAgo' # str | The requested period (default to SixMonthsAgo)
page = 1.2 # float | The requested page number. Defaults to 1 (optional)
page_size = 1.2 # float | The requested page size (optional)
sort = 'sort_example' # str | The requested sort. Sorting may be applied to multiple columns. For descending order a '-' prefix should be used. (optional)
fields = 'fields_example' # str | A comma delimited list of fields which should be returned (optional)

try:
    # Search
    api_instance.get_search(period, page=page, page_size=page_size, sort=sort, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_search: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.etoro.com/Discover/V1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_metadata**](docs/DefaultApi.md#get_metadata) | **GET** /MetaData | MetaData
*DefaultApi* | [**get_search**](docs/DefaultApi.md#get_search) | **GET** /Search | Search

## Documentation For Models


## Documentation For Authorization


## apiKeyHeader

- **Type**: API key
- **API key parameter name**: Ocp-Apim-Subscription-Key
- **Location**: HTTP header

## apiKeyQuery

- **Type**: API key
- **API key parameter name**: subscription-key
- **Location**: URL query string


## Author


