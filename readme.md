## Task requirements. 
Dataset can be pulled from here, data schema available as well: 

[Brazilian E-Commerce Public Dataset by Olist | Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?select=olist_orders_dataset.csv) 

We want to forecast for each item, what are the sales going to be next week.
Expected output is repository that has the following:
1.  Code to load relevant tables for the task (minimum tables needed), and prepare efficient ETL that builds a dataset on which Data Scientist can continue the work (use pandas) 
1.  The output should be in parquet, well partitioned by product
2.  The format of output is a single table that can be used for modelling (no need to extract features).
2.  python script to run code, that you can pass arguments to
3.  A couple of simple pytest tests, and run them in github actions at every PR.
4.  Configuration files in yml
5.  [Think about the following:](#Things-to-think-about)
- Which features would you extract and how from the tables? How would you use the remaining tables?
- How would you turn it into an application in production?
- How would you design an application if you knew that you would have to build a similar solution for a couple of other countries, and the data schema might be different for them, however, you can get the same underlying data?


  ## Things to think about
   ***Which features would you extract and how from the tables? How would you use the remaining tables?*** \
    In my current implementation, I've extracted only a minimal subset of attributes from orders and order_items tables, 
    and, as a granularity attribute, I use [project_id] (for some reason we do not have product name in source data) and "date of the week begins". \
    For slicing by the date we can use whatever of date attributes from orders entity (order_purchase_timestamp',
  'order_approved_at','order_delivered_customer_date'), - kind of role-playing dimension, we can choose either of them in the application command line parameter.\
    Depending on the question we want to have an answer to, we can easily add here any new dimension attribute for slicing,    like "product.category (translates to English or not)", "Seller.City" or some numeric measure for aggregation (Like "AVG(review_score) from reviews). \
We can also use geolocation data to build spatial diagrams.. \
Speaking about modern AI models, we can use them for recommendation systems.\
Or we can leverage language models to analyze review_comment_message from review.
    
  ***How would you turn it into an application in production?*** \
       - Add additional steps to download source files from Web\
       - Implement incremental processing \
       - Implement consistent exception handling and logging \
       - Leverage some orchestration tools, that would allow scheduling, notifications, and retry logic. \
         For example, [Prefect](https://www.prefect.io/) or [Airflow](https://airflow.apache.org/) 

  ***How would you design an application if you knew that you would have to build a similar solution for a couple of other countries*** \
    Assuming that for other countries we will get another structure of source files, we should:
  - somehow bring all the necessary possible attributes to the common denominator (work for business analysis),
  - build some "master metadata store" (yaml file or table),
  - keep metadata for each of the sources,
  -  maintain some mapping structure (yaml config file or sql table) to map column names from entities from different countries to common schema.

## Implementation
### Initial assumptions
Taking as an assumption, that in the initial requirements in the " forecast for each item," the word "item" stands for "Product" entity. \
But, as in the existing dataset we do not have anything like "product name", we are including only "product_id" in the granularity of the output dataset. \
As we are not able to split payments by order_items, we are taking as an assumption that all the orders, regardless of their status (delivered, shipped, invoiced) and the existence of the items in orders_item, are paid or supposed to be paid soon.  \
And for aggregation, we are taking [price] column from [order_items] table.
So, we just joined data from 2 dataframes, [orders] and [order_items].\
As we are not sure,  which of the date attributes from [orders] entity a user might want  to leverage for "group by",  we implement this as an application command line argument, the default is "order_purchase_timestamp".\
	   _python main.py --date_column order_approved_at_


### Project structure
 - _/Main.py_ :  Entry point for the application, parses command line arguments and calls methods for ETL
- _/Config.yml_ : contains all environment-specific configuration data. Also contains links to the entity-specific config yml files with metadata
- _/config_modules_: contains pydantic (kind of data-classes) classes, related to configuration files and config_reader.py model with ConfigReader class (wanted to make it a singleton instance, but then decided to keep it a bit simpler) \
- _/config_modules/metadate/<enity_type**>metadata.yaml_ :
configuration files for source metadata, list of columns to read and types of column (trying to do pandas dataframes as narrow as possible)
- _/etl_modules_ : main workers of ETL:\
  --_load_source_data.py_ : extracts data from .csv to data frame,\
  --_transform_data.py_ : makes joins and aggregations,\
  --_save_output_data.py_ : is responsible for saving to parquet, using "chunk" logic.
- /tests: some code for manual development testing
- _/tests/input_data_ : subset of kaggle datasets data for testing
- _/test.py _:  tests for automated testing using GitHub actions
- _/.githu/workflows/check.yml_ : config for git hub actions
### External libraries, worth mentioning about
- [pydantic](https://docs.pydantic.dev) - data classes, that for my implementation used to make the work with config files more convenient, and to provide validation for config data
- [Dask](www.dask.org),  some extension of pandas,  gives chunking logic. As the number of product_id in our case is more than 50K, standard pandas.save_to_parquet(..) is failing, it can't cope with more than 1024 partitions





