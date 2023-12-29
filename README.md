# Cryptocurrency Investment Analyzer

## Disclaimer

This repo is missing a file — data.py — because that file includes private information about the CoinMarketCap API key and Forbes data that is locked behind a subscription wall. This repo only includes the driver.py file which runs the program in the command line, and the prices.py file which makes the REST API call. 

## Description

This project is created using Python and the CoinMarketCap API, which allows users to collect real-time prices of speciic cryptocurrency assets recommended by Forbes. Users can view the recommended core and accelerator portfolios in the command line, and then choose how much they want to invest using one of the specific portfolios. The program then computes the recommended allocation for each asset with the desired investment amount.

## Why

Every month I invest into my cryptocurrency portfolio using the same recommendations as shown in this project. I wondered if there was a way to use Python to automate the amount to invest into each asset, as opposed to calculating them each by hand. I wanted to create this project to work on my Python skills, while at the same time learning about how to use an API. This project taught me about the requests library in Python, as well as working with and parsing JSON files in the command line. A future iteration of this project may be one that utilizes a Coinbase API to actually make the cryptocurrency purchases via the program.
