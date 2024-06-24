# Market Analysis with Association Rules

This repository contains a Python script (market.py) for performing market analysis using association rule mining techniques. The analysis is applied to transaction data (market_data.csv) to discover patterns and associations among purchased items.
# Overview
Association rule mining is a data mining technique used to identify relationships between items purchased together in transactional data. This script uses the Apriori algorithm to find frequent itemsets and generate association rules based on user-defined support and confidence thresholds.

# Requirements
Python 3.x
pandas
mlxtend
Install the required Python packages using pip:
pip install pandas mlxtend
# Usage
# Running the Script
To analyze the market data and generate association rules, follow these steps:
# Clone the Repository:
git clone https://github.com/mechimaher/data-mining

cd data-mining
# Prepare Data:
Ensure market_data.csv is placed in the project directory.
# Run the Script:
Execute market.py with Python, specifying optional parameters for minimum support and confidence:
