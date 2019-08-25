# Data for exploratory analysis only 

Notes: data here is only a small portion of the original dataset.

**Data Source**    
ftp://ftp.nhtsa.dot.gov/fars/   

Analytical User Guide      
ftp://ftp.nhtsa.dot.gov/FARS/FARS-Doc/Analytical%20User%20Guide/    
Auxiliary Analytical User Manual   
ftp://ftp.nhtsa.dot.gov/FARS/FARS-Doc/Auxiliary%20Analytical%20User%20Manual/  

```
The Fatality Analysis Reporting System (FARS), which became operational in 1975, 
contains data on a census of fatal traffic crashes within the 50 States, the 
District of Columbia, and Puerto Rico. To be included in FARS, a crash must 
involve a motor vehicle traveling on a trafficway customarily open to the public, 
and must result in the death of an occupant of a vehicle or a non-occupant 
within 30 days (720 hours) of the crash.
```
```
FARS data are obtained from various States’ documents, such as:
• Police Crash Reports
• Death Certificates
• State Vehicle Registration Files
• Coroner/Medical Examiner Reports
• State Driver Licensing Files
• State Highway Department Data
• Emergency Medical Service Reports
• Vital Statistics and other State Records
```
```
From these documents, the analysts code more than 140 FARS data elements. 
Annual FARS data files are available for 1975 through 2017.
FARS data are made available to the public in Statistical Analysis 
System (SAS) data files as well as Database Files (DBF) and comma-separated 
values (CSV) files.
```
(Note: from FTP server only CSV and SAS files are available.)
`
This manual describes the 20 current data files as well as previously discontinued data files. The 20 current data files are: Accident, Vehicle, Person, Parkwork, Pbtype, Cevent, Vevent, Vsoe, Damage, Distract, Drimpair, Factor, Maneuver, Nmimpair, Nmprior, Nmcrash, Safetyeq, Violatn, Vindecode, and Vision data files. Eleven of these data files contain one data element each in which the analyst could code multiple responses: Damage, Distract, Drimpair, Factor, Maneuver, Nmimpair, Nmprior, Nmcrash, Safetyeq, Violatn, and Vision. That is, the FARS/CRSS Coding and Validation Manual instructs coders to “select all that apply” for these data elements. Therefore, there is a record for each response. Discontinued data files are included after the current data files. The Vehnit data file was replaced by the Parkwork data file and its data element history can be found in the Parkwork data file.
`
(Note: Page 10, `2017 FARS Analytical User's Manual`)

**Accident** - (1975-current): This data file contains information about crash characteristics and environmental conditions at the time of the crash. There is one record per crash.

<img src="https://github.com/Nov05/pictures/blob/master/pic001/2019-08-25%2000_53_18-.jpg">

Page 14, `FARS Analytical Users Manual 1975-2017-812602.pdf`  
<img src="https://github.com/Nov05/pictures/blob/master/pic001/2019-08-25%2000_59_42-Microsoft%20Store.png">  

Page 27, STATE    
<img src="https://github.com/Nov05/pictures/blob/master/pic001/2019-08-25%2001_20_05-2017%20FARS%20Analytical%20User's%20Manual%20-%20Adobe%20Acrobat%20Reader%20DC.png">









