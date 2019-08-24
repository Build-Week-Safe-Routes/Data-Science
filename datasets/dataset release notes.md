

### Release Notes 1975-2000 
```
-----------------------------------  
FARS National and Puerto Rico Files  
-----------------------------------  

The FARS Files directory structure has been modified and made consistent across all years, beginning with 1975.    
DBF format has been replaced with CSV format.  
There are two folders, one for national and one for Puerto Rico.    
In each folder, there are two zip files, one in SAS format and one in CSV format.   

Auxiliary files are included in the SAS and CSV sets instead of as independent zip files.   

--------------------      
FARS Auxiliary Files    
--------------------     
The FARS Auxiliary files are datasets that are derived from the standard FARS datasets:   
1. Accident -> Acc_Aux  
2. Vehicle -> Veh_Aux  
3. Person -> Per_Aux  
These files are joined by the standard key variables.   
Please read the following document for additional details: http://www-nrd.nhtsa.dot.gov/Pubs/811364.pdf   
For User Manuals, please go to: ftp://ftp.nhtsa.dot.gov/FARS/FARS-Doc/FARS_Auxiliary_Analytical_User_Manuals.zip    
For SAS Format Catalog, please go to: ftp://ftp.nhtsa.dot.gov/FARS/Auxiliary_FARS_Files_Formats    
```


### Release Notes 2001-2011
```
===================================
FARS National and Puerto Rico Files
-----------------------------------

The FARS Files directory structure has been modified and made consistent across all years, beginning with 1975.  
DBF format has been replaced with CSV format.
There are two folders, one for national and one for Puerto Rico. 
In each folder, there are two zip files, one in SAS format and one in CSV format.

Auxiliary files are included in the SAS and CSV sets instead of as independent zip files.

====================
FARS Auxiliary Files
--------------------
The FARS Auxiliary files are datasets that are derived from the standard FARS datasets: 
1. Accident -> Acc_Aux
2. Vehicle -> Veh_Aux
3. Person -> Per_Aux
These files are joined by the standard key variables.
Please read the following document for additional details: http://www-nrd.nhtsa.dot.gov/Pubs/811364.pdf
For User Manuals, please go to: ftp://ftp.nhtsa.dot.gov/FARS/FARS-Doc/FARS_Auxiliary_Analytical_User_Manuals.zip
For SAS Format Catalog, please go to: ftp://ftp.nhtsa.dot.gov/FARS/Auxiliary_FARS_Files_Formats

Updates for Auxiliary Files
---------------------------
9/22/2017: Derived Indian Reservation data elements have been added to the Accident level auxiliary file – ACC_AUX.*. 
	The first data year of availability for the following new Indian Reservation related data elements is 2001:
	BIA – 1 indicates that the crash occurred on Tribal lands. The geographic location data collected in FARS was used in conjunction with spatial data on the Bureau of Indian Affairs (BIA) land boundaries to identify Tribal lands.
	SPJ_INDIAN – derived from FARS special jurisdiction (SP_JUR=3) element. 1 indicates that the crash occurred on an Indian Reservation.
	*INDIAN_RES – 1 indicates either BIA=1 or SPJ_INDIAN=1. This provides a more accurate representation of fatal crashes occurring on Tribal lands.
	*Use the INDIAN_RES data element to obtain the most complete data.

	ACC_AUX.* datasets can be merged with other FARS datasets by ST_CASE to obtain additional information on the crash.
```

### Release Notes 2012
```
This version of 2012 FARS update only applies to Puerto Rico files. 
The Puerto Rico files were regnerated to correct issues with alcohol results.
The alcohol files for Puerto Rico were regenerated on 5/18/2016. 

There are two folders, one for national and one for Puerto Rico. 
In each folder, there are two zip files, one in SAS format and one in CSV format.

Auxiliary files are included in the SAS and CSV sets instead of as independent zip files.
==========================
FARS Auxiliary Files
--------------------
The FARS Auxiliary files are datasets that are derived from the standard FARS datasets: 
1. Accident -> Acc_Aux
2. Vehicle -> Veh_Aux
3. Person -> Per_Aux
These files are joined by the standard key variables.
Please read the following document for additional details: http://www-nrd.nhtsa.dot.gov/Pubs/811364.pdf
For User Manuals, please go to: ftp://ftp.nhtsa.dot.gov/FARS/FARS-Doc/FARS_Auxiliary_Analytical_User_Manuals.zip
For SAS Format Catalog, please go to: ftp://ftp.nhtsa.dot.gov/FARS/Auxiliary_FARS_Files_Formats
```
