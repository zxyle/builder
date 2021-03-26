#!/usr/bin/env bash

function package() {
    mvn clean package -Dmaven.test.skip=true
}
