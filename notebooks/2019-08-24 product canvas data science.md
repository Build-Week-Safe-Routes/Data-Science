2019-08-24   

Product Canvas Form    
https://docs.google.com/document/d/1oGA80zlszkuWQwEnv8FdomVXvNFQVV307uh-Ug2pKIg/   

## For Data Scientists

- Describe the Established data source with at least rough data able to be provided on day 1. 

```
1. dataset name FARS, Fatality Analysis Reporting System  
2. dataset dated from 1975 to 2017, national and Puerto Rico  
3. dataset file format CSV, data of each year has multiple files   
4. so far found the major information is stored in `accident.csv` and
`acc_aux.csv`, details of accident are in other csv files such as 
`veh_aux.csv`, `Damage.csv`, `Maneuver.csv`, `Distract.csv`, 
`vehicle.csv`, `Violatn.csv`, etc.
5. the primary key is `ST_CASE`, "Two Characters for State Code followed 
by Four Characters for Case Number".    
```

- You can gather information about the data set you’ll be working with from the project description. Be sure to collaborate with your PM, and your Backend Architect to chat about the resources you have.

```
2019-08-24 doing data exploratory analysis  
```

- Write a description for what the DS problem is (what uncertainty/prediction are we trying to do here? Sentiment analysis? Why is this a useful solution to a problem?)

```
1. the accident data has information of type, fatal number, time(year/month/day/hour/minute/day of week), location (latitude/longitude/county/city), car model, 
2. `Auxiliary Analytical User Manual` pdf has 619 pages... and data is 
scattered in different CSV files. will need a lot of time to merge data.  
3. use the history data to predict the future accident numbers for 
certain locations with latitude/longitude/county/city/time/etc 
information (to be decided) 
```

- A target (e.g. JSON format or such) for output that DS students can deliver to web/other students for them to ingest and use in the app

```
first assume we will have a map of a small area, a few street blocks? (need to be discussed with the product designers)  
1. history accident summary data for the area, maybe yearly? 
total accident number, total fatal number, numbers for different 
accident types... (to be decided)   
2. if user choose a certain intersection, display some details  
3. predictive view for this area, same elements and layout with 
history data displaying 
```

**Data Source**  
ftp://ftp.nhtsa.dot.gov/fars/  

**Table Headers**  
https://github.com/Nov05/DS-Unit-3-Sprint-4-Build-Week-Safe-Routes/blob/master/datasets/FARS2017NationalCSV_headers.txt

**Auxiliary Analytical User Manual**  
ftp://ftp.nhtsa.dot.gov/fars/FARS-DOC/Auxiliary%20Analytical%20User%20Manual/    



   

