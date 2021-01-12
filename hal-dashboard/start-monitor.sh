#!/bin/bash
cd ~/GIT/hal
nohup ~/GIT/hal/http-server-tail2.py 12880 > /dev/null 2>&1 &
