#!/usr/bin/env bash
echo 'Checking version of webdriver-manager'
webdriver-manager update
echo 'Starting webdriver-manager'
webdriver-manager start &
