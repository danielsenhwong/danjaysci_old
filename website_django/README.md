danjaysci
==========

[20140808]
- Using SQlite3 database for now
- Initiated 'primers' application
- Installed 'South' for database migrations (pip install South), however
  this will not be needed once Django 1.7 is released. The upgrade documen-
  tation for this transition is here: 
  https://docs.djangoproject.com/en/dev/topics/migrations/#upgrading-from-south
- Using a github clone on the hosting server. Run command 'git pull' to fetch
  the newest version and merge it to make it live.
* Remember that the 'settings.py' and database (*.sqlite3) files are excluded
  from github, so these must be uploaded separately.
* Additionally, remember to 'touch /var/www/danjaysci/index.fcgi' after
  updating.
