#!/usr/bin/env bash

export CGO_ENABLED=0
# darwin linux windows
export GOOS=linux
export GOARCH=amd64

go build