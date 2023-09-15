Dataset can be pulled from here, data schema available as well:
Brazilian E-Commerce Public Dataset by Olist | Kaggle
Task:
We want to forecast for each item, what are the sales going to be next week.
Expected output is repository that has the following:
1.	Code to load relevant tables for the task (minimum tables needed), and prepare efficient ETL that builds a dataset on which Data Scientist can continue the work (use pandas) 
1.	The output should be in parquet, well partitioned by product
2.	The format of output is a single table that can be used for modelling (no need to extract features).
2.	python script to run code, that you can pass arguments to
3.	A couple of simple pytest tests, and run them in github actions at every PR.
4.	Configuration files in yml
5.	Think about the following: 
1.	Which features would you extract and how from the tables? How would you use the remaining tables?
2.	How would you turn it into an application in production?
3.	How would you design an application if you knew that you would have to build a similar solution for a couple other countries, and the data schema might be different for them, however, you can get the same underlying data?
