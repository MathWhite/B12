# B12 Application Submission

This repository contains an automated submission script for my application to B12.

## Overview

- **Applicant**: Matheus Francisco Garcia de Carvalho
- **Email**: matheusfgc99@gmail.com
- **Resume**: https://mc-dev.tech/

## How It Works

The GitHub Action automatically submits my application to B12's API endpoint with:
- A cryptographically signed request (HMAC-SHA256)
- ISO 8601 timestamp
- Links to this repository and the action run

## Files

- `submit.py` - Python script that POSTs the application
- `.github/workflows/submit.yml` - GitHub Action workflow
- `requirements.txt` - Python dependencies (requests)

## Running

The action runs automatically on push to main, or can be triggered manually via GitHub Actions.
