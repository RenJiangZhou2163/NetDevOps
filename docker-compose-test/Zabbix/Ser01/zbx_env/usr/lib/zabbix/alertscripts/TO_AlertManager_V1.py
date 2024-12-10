#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# renjiangzhou
# 2024.01.15

import datetime
import json
import sys

import pytz
import requests
from alertmanager import Alert, AlertManager
from loguru import logger

logger.add(
    f"./alertscripts.log",
    enqueue=True,
    rotation="10 MB",
    retention="10 days",
    compression="zip",
)


def rfc3339_time(time_str):
    try:
        time_format = "%Y.%m.%d %H:%M:%S%z"
        
        # Convert string to datetime object
        local_datetime = datetime.datetime.strptime(time_str, time_format)
        
        # Convert local datetime to UTC datetime
        utc_datetime = local_datetime.astimezone(pytz.utc)
        
        # Convert datetime object to RFC3339-formatted string
        rfc3339_time = utc_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")

    except Exception as e:
        logger.error(e.args)
    return rfc3339_time  # Output: 2023-11-22T03:22:23Z


def parse_zabbix_parameters():
    params = {}
    # sys.argv[0] 被执行的脚本
    # sys.argv[1] 字符串

    alarm_str = sys.argv[3]
    alarm_lst = alarm_str.splitlines()

    params["eventId"] = alarm_lst[0]
    params["trigger_hostgroup_name"] = alarm_lst[1]
    params["trigger_name"] = alarm_lst[2]
    params["trigger_severity"] = alarm_lst[3]
    params["trigger_status"] = alarm_lst[4]
    params["host_ip"] = alarm_lst[5]
    params["host_name"] = alarm_lst[6]
    params["currentValue"] = alarm_lst[7]
    params["alertName"] = alarm_lst[8]
    if params["trigger_status"] == "OK":
        params["event_recovery_date"] = alarm_lst[9]
        params["event_recovery_time"] = alarm_lst[10]
    else:
        params["event_date"] = alarm_lst[9]
        params["event_time"] = alarm_lst[10]
    params["source"] = alarm_lst[11]
    params["netType"] = alarm_lst[12]
    params["trigger_url"] = ""
    return params


def build_alert(params):
    alert = {}
    
    if params["trigger_status"] == "OK":
        alert["endsAt"] = rfc3339_time(
            params["event_recovery_date"]
            + " "
            + params["event_recovery_time"]
            + "+0800"
        )
        # alert["status"] = "firing"
    elif params["trigger_status"] == "PROBLEM":
        alert["startsAt"] = rfc3339_time(
            params["event_date"]
            + " "
            + params["event_time"]
            + "+0800"
        )
        # alert["status"] = "firing"

    alert["labels"] = {}
    alert["labels"]["eventId"] = params["eventId"]
    alert["labels"]["alertName"] = params["alertName"]
    alert["labels"]["source"] = params["source"]
    # alert["labels"]["severity"] = params["trigger_severity"]

    if params["trigger_severity"] == "Disaster":
        alert["labels"]["severity"] = "1"
    elif params["trigger_severity"] == "High":
        alert["labels"]["severity"] = "2"
    elif params["trigger_severity"] == "Average":
        alert["labels"]["severity"] = "3"
    elif params["trigger_severity"] == "Warning":
        alert["labels"]["severity"] = "4"
    elif params["trigger_severity"] == "Information":
        alert["labels"]["severity"] = "5"
    else:
        alert["labels"]["severity"] = "6"
	
    alert["annotations"] = {}
    alert["annotations"]["description"] = "Zabbix alert for " + params["trigger_name"]
    alert["annotations"]["currentValue"] = params["currentValue"]
    alert["annotations"]["host"] = params["host_ip"]
    alert["annotations"]["hostName"] = params["host_name"]
    alert["annotations"]["netType"] = params["netType"]
    alert["generatorURL"] = params["trigger_url"]

    return alert

try:
    params = parse_zabbix_parameters()
    alert = build_alert(params)
    logger.info(alert)

    # Specify an Alert Manager host to connect to.
    a_host = "http://alertmanager01.xfusion.com"
    b_host = "http://alertmanager02.xfusion.com"
    a_manager = AlertManager(host=a_host)
    b_manager = AlertManager(host=b_host)
    
    # Post an alert to our Alert Manager.
    a_manager.post_alerts(alert)
    b_manager.post_alerts(alert)
	
    logger.info("Success")
except Exception as e:
    logger.error(e.args)