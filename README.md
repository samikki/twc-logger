# twc-logger
Logs Tesla Wall Connector data to CSV files

Usage: 
- edit runlogger.sh to use directories of your choice (create data directory if needed)
- edit the curl IP number to point to Tesla Wall Connector in your home network
- configure rclone googledrive remote to point to your Google Drive (use rclone config)
- start runlogger.sh regularly using crontab (I do it once a minute)

samik@iki.fi 9/2021
