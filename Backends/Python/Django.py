#######################################
#
#   DJANGO CHEAT SHEET
#
#######################################


#**************************************
#   Pyhon Commands (in Project)
#**************************************

python manage.py startapp <App Name>			            # Create a new app within dir
pyhton manage.py migrate			                        # Performs sync of app models with db
pyhton manage.py makemigrations <App Name>		            # Detect changes in specified App & create a migration
python manage.py sqlmigrate <App Name> <Migration id>	    # View Migration Details
