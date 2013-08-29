#!/usr/bin/env python
#coding=utf-8
#
#Script to generate TCP lab in netkit

import os
import sys
import getopt

tcp_abc=0
tcp_abort_on_overflow= False
tcp_adv_win_scale=2
#tcp_allowed_congestion_control="reno"
#tcp_available_congestion_control
tcp_app_win=31
tcp_base_mss=512
tcp_bic=False
tcp_bic_low_window=14
tcp_bic_fast_convergence=True
#tcp_congestion_control="reno"
tcp_dma_copybreak=4096
tcp_dsack=True
tcp_ecn=False
tcp_fack=True
tcp_fin_timeout=60
tcp_frto=0
tcp_frto_response=0
tcp_keepalive_intvl=75
tcp_keepalive_probes=9
tcp_keepalive_time=7200
tcp_low_latency=False
#tcp_max_orphans=
#tcp_max_syn_backlog
#tcp_max_tw_buckets
#tcp_moderate_rcvbuf
#tcp_mem=
tcp_mtu_probing=0
tcp_no_metrics_save=False
tcp_orphan_retries=8
tcp_reordering=3
tcp_retrans_collapse=True
tcp_retries1=3
tcp_retries2=15
#tcp_rfc1337
tcp_rmem='default'
tcp_sack=True
tcp_slow_start_after_idle=True
tcp_stdurg=False
tcp_syn_retries=5
tcp_synack_retries=5
#tcp_syncookies
tcp_timestamps=True
tcp_tso_win_divisor=3
tcp_tw_recycle=False
tcp_tw_reuse=False
tcp_vegas_cong_avoid=False
tcp_westwood=False
tcp_window_scaling=True
#tcp_wmem=
tcp_workaround_signed_windows=False



def create_basic_topology():
    f=open('client1.startup','w')
    f.write('ifconfig eth0 2001:db8:0b0:15:da:b055::2/96 up\nroute -A inet6 add default gw 2001:DB8:0b0:15:da:b055::1')
    f.close()
    f=open('client2.startup','w')
    f.write('ifconfig eth0 2001:db8:0b0:15:da:b055::3/96 up\nroute -A inet6 add default gw 2001:DB8:0b0:15:da:b055::1')
    f.close()
    f=open('server.startup','w')
    f.write('ifconfig eth0 2001:db8:be:600d::2\n/etc/init.d/apache2 start\nroute -A inet6 add default gw 2001:DB8:be:600d::1')
    f.close()
    f=open('r.startup','w')
    f.write('ifconfig eth0 2001:db8:0b0:15:da:b055::1/96 up\nifconfig eth1 2001:db8:be:600d::1/64 up\nsysctl -w net.ipv6.conf.all.forwarding=1\n')
    f.close()
    f=open('lab.conf','w')
    f.write('LAB_DESCRIPTION="A lab showing problems that can occurs when using tcp protocol to download files on a webserver"\n LAB_VERSION=1\n LAB_AUTHOR="O. Bonaventure, J. Vellemans, F. Rochet"')
    f.write('client1[0]=A\nClient2[0]=A\nr[0]=A\nr[1]=B\nserver[0]=B')
    f.close()

#main function
def main(argv):
    create_basic_topology()
    
if __name__=="__main__":
    main(sys.argv[1:])

