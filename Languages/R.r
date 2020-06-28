#######################################
#
#   R CHEAT SHEET
#
#######################################


#**************************************
#   Table of Contents
#**************************************

# 1. Basic Commands
# 2. File Reading Commands


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
#   Basic Commands 
#**************************************

#Commands                               #Description

#Reading Flat Files


#Reading Excel


#Reading XML


#Reading JSON