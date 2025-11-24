#!/bin/bash

response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000)

if [ "$response" -eq 200 ]; then
    echo "Application disponible"
else
    echo "Application indisponible"
    exit 1
fi
