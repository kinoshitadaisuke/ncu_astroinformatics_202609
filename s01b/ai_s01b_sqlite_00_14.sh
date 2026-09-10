#!/bin/sh

#
# Time-stamp: <2026/09/10 16:38:11 (UT+08:00) daisuke>
#

# SQL query
sqlite3 -list -header planet0.db "select * from planet;"
