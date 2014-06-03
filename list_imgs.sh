#!/bin/bash

wget 'http://image.baidu.com/channel/imgs?c=%E7%BE%8E%E5%A5%B3&t=%E5%85%A8%E9%83%A8&s=0&pn=$1&rn=6000&fr=channel' -O $[$1+6000].list
