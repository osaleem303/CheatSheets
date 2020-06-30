#######################################
#
#   R CHEAT SHEET
#
#######################################


#**************************************
#   Table of Contents
#**************************************

# 1. Basic Commands
# 2. Basic DataTypes
# 3. File Reading Commands
# 4. Data Frames
# 5. Plotting


#**************************************
#   Basic Commands 
#**************************************

#Commands                               #Description

#Working Directory
setwd(stringPath)                       #Set Working Directory
                                        #Params: string 
                                        #Info: Can be Absolute or relative path e.g "./data" or "User/R/data"

getwd()                                 #Get Working Directory
                                        #RetunType: string

#File Manipulation
file.exists(stringName)                 #Check if file exist in Current Working Directory
                                        #RetunType: bool

file.create(stringName)                 #Creates a file in Current Working Directory
                                        #Params: string

file.remove(stringName)					#Removes a file from Current Working Directory (if exists)
										#Params: string

download.file(URL, dest, method)		#Download file from URL and saves in dest
										#Params: string, string, string
										#Note: If the url starts with https on Mac you may need to set method=“curl”

#**************************************
#   Basic DataTypes 
#**************************************

#DataTypes                               #Description


#**************************************
#   File Reading Commands 
#**************************************

#Commands                               #Description

#Reading Flat Files
read.table(stringPath)					#Read contents from stringPath into DataFrame
read.table(stringPath, sep, header)		#Params: string, string (opt), bool (opt)
										#Note: 'sep' divides the content based on provided character
										#	   'header' to omit out header contents of file

#Reading Excel
#Required Lib: 'xlsx'
read.xlsx(stringPath, sheet, header) 	#Reads content from excel file
										#Params: string, int, bool
										#Note: 'sheet' is index of excel sheet to be read
										#	   'header' to omit out header contents of sheet

#Reading XML
#Required Lib: 'XML'
xmlTreeParse(stringPath, useInternal) 	#Reads XML file from proivided source
										#Params: string, bool

#Reading JSON
#Required Lib: 'jsonlite'
fromJSON(stringPath)					#Reads JSON from stringPath


#**************************************
#   Data Frames
#**************************************

#Required Lib: 'data.table'
#Commands                               #Description
data.frame(x, y, z)						#Creates a data frame provided by data in x, y, z

#Subsetting
#Rows
<FrameVariable>[<Condition>, ]			#Splits data of 'FrameVariable' by applying 'Condition'
#Columns
<FrameVariable>[ ,<Condition>]

#Adding new Column
<FrameVariable>[ ,<ColName>:= <data>] 	#Adds Column by 'ColName' with data in 'data'

#Merge
merge(DataFrame1, DataFrame2)			#Merges DataFrame1 & DataFrame 2 into single DataFrame

#Sort
sort(dataFrame$var)						#Sort dataframe on basis of variable passed
sort(dataFrame$var, descending)			#params DataFrame, bool(opt)
sort(dataFrame$var, na.last)			#Note: descending: If True, sorts in descending order
										# 	   na.last:		Pushes all NAs at end of list

#**************************************
#   Plotting
#**************************************

#Commands                               #Description

#Required Lib: 'ggplot2'
#Basics of qplot
qplot(xLabel, yLabel, dataFrame)		#Plots a graph of provided dataFrame
qplot(xLabel, yLabel, dataFrame, color) #params: string, string, dataFrame, color (opt), geom (opt)
qplot(xLabel, yLabel, dataFrame, geom)	#Note: 'color' is colour asthetics of plot
										#		'geom' collection object to draw path


#Required Lib: 'lattice'
#Basics of lattice plot
xyplot(xVar ~ yVar, dataFrame)			#Plots a simple scatter plot of dataFrame
										#params: string ~ string, dataFrame
										