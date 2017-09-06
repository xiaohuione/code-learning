#!/bin/bash
#########################################################################
# File Name: net_ping.sh
# Created Time: 日  5/22 23:49:26 2016
#########################################################################

router_mgr_ip="192.168.1.253"
dns="211.162.66.66"

function log()
{
    echo "[$(date +"%F %T")] Info: ${*}" 
}

function reboot_router()
{

    local ip=$1
    local reboot_url="http://${ip}/userRpm/SysRebootRpm.htm?Reboot=%D6%D8%C6%F4%C2%B7%D3%C9%C6%F7"

    log "reboot router..."

    curl "${reboot_url}" --user admin:admin | head -n 5
}

function wait_ping_ok()
{
    local ip=$1
    while true; do
        ping -W 1 -c 1 ${ip} >/dev/null 2>&1
        if [ $? -eq 0 ];then
            log "ping $ip ok"
            break
        else
            log "ping $ip failed, wait ..."
            sleep 10
        fi
   done 
}

function get_status()
{
    local status="unkown"

    ping -W 2 -c 1 ${dns} >/dev/null 2>&1
    if [ $? -eq 0 ];then
        status="dns_service_ok"
    else
        ping -W 1 -c 1 ${router_mgr_ip} >/dev/null 2>&1
        if [ $? -eq 0 ];then
            status="dns_service_failed"
        else
            status="router_offline"
        fi
    fi
    echo $status
}

function main()
{
    log "start monitor the router"
    # ok router_offline  router_online  reboot affter_reboot
    # router_offline -> router_online -> ok -> reboot -> router_offline -> router_online
    status="unkown"
    while true; do
        status=$(get_status)
        case $status in 
            "router_offline")
                wait_ping_ok ${router_mgr_ip}
                ;;
            "dns_service_failed")
                log "dns ${dns} failed"
                reboot_router ${router_mgr_ip}
                wait_ping_ok ${dns}
                ;;
            "dns_service_ok")
                log "dns ${dns} ok"
                sleep 10
                ;;
            *)
                log "status was wrong [status=$status]"
                sleep 1
        esac
    done
}

main "$@"
