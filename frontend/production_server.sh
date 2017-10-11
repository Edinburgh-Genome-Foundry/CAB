#!/bin/sh
npm run build
cd dist
http-server -p 8080 --push-state
