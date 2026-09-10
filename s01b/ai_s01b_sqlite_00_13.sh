#!/bin/sh

#
# Time-stamp: <2026/09/10 16:37:41 (UT+08:00) daisuke>
#

# SQL query
sqlite3 -list planet0.db "select * from planet;"
