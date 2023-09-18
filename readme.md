## Task requirements. 
Dataset can be pulled from here, data schema available as well: 

[Brazilian E-Commerce Public Dataset by Olist | Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?select=olist_orders_dataset.csv) 

We want to forecast for each item, what are the sales going to be next week.
Expected output is repository that has the following:
1.	Code to load relevant tables for the task (minimum tables needed), and prepare efficient ETL that builds a dataset on which Data Scientist can continue the work (use pandas) 
1.	The output should be in parquet, well partitioned by product
2.	The format of output is a single table that can be used for modelling (no need to extract features).
2.	python script to run code, that you can pass arguments to
3.	A couple of simple pytest tests, and run them in github actions at every PR.
4.	Configuration files in yml
5.	[Think about the following:](#Things-to-think-about)
- Which features would you extract and how from the tables? How would you use the remaining tables?
- How would you turn it into an application in production?
- How would you design an application if you knew that you would have to build a similar solution for a couple other countries, and the data schema might be different for them, however, you can get the same underlying data?


  ## Things to think about
   ***Which features would you extract and how from the tables? How would you use the remaining tables?*** \
    In my current implementation I've extacted only minumal subset of attrubutes from orders and order_items tables.\
    As a granulation attribute we are using project_id (for some reason we do not have product name in source data) and "date of week begin". \
    For slicing by date we can use whatever of date attributes from ordes enitity (order_purchase_timestamp',
  'order_approved_at','order_delivered_customer_date'), - kind of role-playing dimension, we can choose either of them in application command line parameter.\
    Depending of the question we want to have answer to, we can easily add here any new dimension attribute for slicing,    like "Product.category (translates to English or not)", "Seller.City" or some numeric measure for aggregation (Like "AVG(review_score) from reviews). We can also use geolcation data to build spatial diagrams.. \
Speaking about modern AI models, we can use them for recommendation sistems.\
Or we can leverage language models to analyze review_comment_message from review.
    
  ***How would you turn it into an application in production?*** \
        &nbsp;Add additonal steps to download source data from site \
        &nbsp;Think about incremental processing \
        &nbsp;Think about consistent exeption handling and logging \
        &nbsp;Leverage some orchestration tool, that would allow to have scheduling, notifications, retry logic. \
  
  ***How would you design an application if you knew that you would have to build a similar solution for a couple other countries*** \
    Assuming that for other coutries we will get another structure of source files, we should somehow bring all the necessary possible attributes to common denominator, keep some "master metadata store" (yaml file or table), keep metadata fore each of the sources, and maintain some mapping structure (yaml config file or sql table) to to map column names from entities from diffrent countries to common schema.

## Implementation
### Project structure


