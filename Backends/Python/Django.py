#######################################
#
#   DJANGO CHEAT SHEET
#
#######################################


#**************************************
#   Table of Contents
#**************************************

# 1. Python Commands
# 2. Python Shell Commands


#**************************************
#   Pyhon Commands (in Project)
#**************************************

python manage.py startapp <App Name>                        # Create a new app within dir
python manage.py createsuperuser                            # Creates a user for admin
pyhton manage.py migrate                                    # Performs sync of app models with db
pyhton manage.py makemigrations <App Name>                  # Detect changes in specified App & create a migration
python manage.py sqlmigrate <App Name> <Migration id>       # View Migration Details

#**************************************
#   Python Shell Command 
#**************************************

pyhton manage.py shell                                          # Boots up shell
from <App Name>.models import <modelName>,<modelName1>,...      # Display contents of models from database
<modelName>.objects.all()                                       # Display all insatnces of Model from database
<modelName>.objects.filter(<search params>)                     # Display all instacnces of Model from database filterd. search params e.g (id = 1, arrib__startswith = 'anyText')
exit()                                                          # Quit shell





