# VDK SQL Validation

Versatile Data Kit is more than just an orchestrator 

it is data engineering framework that allows end-to-end data path visibility  and ability to plug at each stage of the development cycle.

In the example we will show how we intercept query in order to apply good practices and contribute to ensuring stability of the infrastructure


![validate](https://user-images.githubusercontent.com/2536458/193760318-e8f47d3f-0267-4056-96d7-63f62c9b47c7.jpg)


## Usage

```
pip install vdk-my-validation 
```

### Configuration

(`vdk config-help` is useful command to browse all config options of your installation of vdk)

| Name | Description | (example)  Value |
|---|---|---|
| max_query_size | The maximum query size in bytes allowed to be executed. | 10000


## Build and testing

```
pytest
```
