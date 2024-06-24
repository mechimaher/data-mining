#                                   Market Analysis with Association Rules

This repository contains a Python script (market.py) for performing market analysis using association rule mining techniques. The analysis is applied to transaction data (market_data.csv) to discover patterns and associations among purchased items.
# Overview
Association rule mining is a data mining technique used to identify relationships between items purchased together in transactional data. This script uses the Apriori algorithm to find frequent itemsets and generate association rules based on user-defined support and confidence thresholds.

# Requirements

 Python 3.x
 
 pandas
 
 mlxtend
 
Install the required Python packages using pip:

 => pip install pandas mlxtend
 
# Usage
# Running the Script
To analyze the market data and generate association rules, follow these steps:
# Clone the Repository:
 => git clone https://github.com/mechimaher/data-mining

 => cd data-mining
# Prepare Data:
Ensure market_data.csv is placed in the project directory.
# Run the Script:
Execute market.py with Python, specifying optional parameters for minimum support and confidence:

 => python market.py

Example with custom thresholds:

 => python market.py --min_support 0.05 --min_confidence 0.1

 # Understanding Output
The script will output discovered association rules, including high-confidence rules and their support metrics.
A visualization using matplotlib will display itemset support and annotations for high-confidence rules with advice messages.

# Parameters
--min_support: Minimum support threshold for frequent itemsets (default: 0.05).
--min_confidence: Minimum confidence threshold for association rules (default: 0.1).

# Example Output
After running the script, you will see output similar to:

High confidence rules:
   antecedents consequents  antecedent support  ...      lift  leverage  conviction
0     (Bread)    (Butter)            0.190935  ...  2.593013  0.059835    1.639682

All association rules:
   antecedents consequents  antecedent support  ...      lift  leverage  conviction
0     (Bread)    (Butter)            0.190935  ...  2.593013  0.059835    1.639682
1    (Butter)     (Bread)            0.196721  ...  2.593013  0.059835    1.602419

# Contribution
Contributions are welcome! If you have any suggestions or improvements, please submit a pull request or open an issue.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

