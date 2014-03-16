#!/bin/bash
rm -rf build/*
r.js -o build.js
r.js -o cssIn=style/style.css out=build/style.css
