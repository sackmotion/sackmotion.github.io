#!/bin/bash
ps auwx|grep http-server-tail2.py|grep -v grep|awk '{print $2}'|xargs kill -15
