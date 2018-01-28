#!/bin/bash

remote_location=pi@$1:robohat

scp robot.py server.py camera.py $remote_location

