#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Paul Wang'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'admin',
        'password': 'passwd',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}