#!/usr/bin/env bash

set -u

# 设置颜色常量
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
WHITE='\033[1;37m'
END_COLOR='\033[0m'

# 版本信息
LOCAL_VERSION="v0.0.2"
VERSION_INFO="${WHITE}{${RED}${LOCAL_VERSION} #dev${WHITE}}"

# 脚本信息
SCRIPT_FUNCTION="--修改此处进行设定功能说明--"
SCRIPT_NAME="--修改此处为脚本名称--"
AUTHOR="--修改此处为作者名称--"

# 打印标题信息
function generate_titles {
    echo -e "${YELLOW}"
    echo " ____             _ __        ___ _   _         ___ ____      "
    echo "|  _ \  ___  __ _| |\ \      / (_) |_| |__     |_ _|  _ \ ___ "
    echo "| | | |/ _ \/ _\` | | \ \ /\ / /| | __| '_ \     | || |_) / __|"
    echo -e "| |_| |  __/ (_| | |  \ V  V / | | |_| | | |    | ||  __/\__ \\${GREEN}"
    echo -e "|____/ \___|\__,_|_|___\_/\_/  |_|\__|_| |_|___|___|_|   |___/ ${WHITE}"
    echo "                  |_____|                 |_____|     By ${VERSION_INFO}"
    echo "作者：${AUTHOR}"
    echo "脚本名称：${SCRIPT_NAME}"
    echo -e "${BLUE}${SCRIPT_FUNCTION}${END_COLOR}"
}

# 打印状态信息
function print_status {
    local MESSAGE=$1
    local STATUS_TYPE=$2

    if [[ "$STATUS_TYPE" == "info" ]]; then
        PREFIX="[ + ]"
        COLOR=$GREEN
    elif [[ "$STATUS_TYPE" == "warning" ]]; then
        PREFIX="[ ! ]"
        COLOR=$YELLOW
    elif [[ "$STATUS_TYPE" == "error" ]]; then
        PREFIX="[ - ]"
        COLOR=$RED
    else
        PREFIX="[ * ]"
        COLOR=$WHITE
    fi

    echo -e "${COLOR}${PREFIX} ${MESSAGE}${END_COLOR}"
}

# 主函数
function main {
    print_status "脚本运行中，请稍候..." 'info'
    print_status "脚本运行结束。" 'info'
}

# 脚本执行开始
generate_titles
main
