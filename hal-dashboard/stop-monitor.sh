#!/bin/bash
ps auwx|grep http-server-tail2-ssl.py|grep -v grep|awk '{print $2}'|xargs kill -15
