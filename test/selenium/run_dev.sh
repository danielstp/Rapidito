#!/usr/bin/env bash
echo 'Running protractor'
protractor conf.js --specs=test_cases/$1
