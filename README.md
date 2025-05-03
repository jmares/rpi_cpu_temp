# RPi CPU Temperature Logger

The purpose of this script is to log the temperature of the CPU of a Raspberry Pi to a SQLite database. Why? I installed [BirdNET-PI](https://github.com/Nachtzuster/BirdNET-Pi) on a Raspberry Pi 4 B and want to keep an eye on the temperature especially when the RPi gets exposed to the sun.

Accidentaly, I noticed that the script also works on my desktop mini pc with Linux Mint.

Version: v0.1

## Installation

- Log in to your Raspberry PI
- In the home directory `/home/birder`, create a folder for python projects

```
mkdir python
```

- Change to the python directory

```
cd python
```

- Create the project folder and the database folder

```
mkdir -p rpi_cpu_temp/db
```
- Or copy the project from your desktop or laptop to the RPi via SSH or SFTP

## Execution

I want the script to automatically start after booting and run every 5 minutes.

Open the crontab:

```
crontab -e
```

and add the following line

```
*/5 * * * * /usr/bin/python3 /home/birder/python/rpi_cpu_temp/log_cpu_temp.py
```

## Notes

I have added 2 lines to the `.gitignore` file to prevent my test database from being added to the repository. 

```
# Test database
*.db
```

Don't forget to add the `db` folder to the project directory, otherwise the script won't run.

## Next steps 

Find a way to visualize it