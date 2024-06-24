"""
Association Rule Mining and Visualization Script

Copyright (c) 2024 MAHER MECHI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

def analyze_association_rules(data_file, min_support=0.05, min_confidence=0.1):
    # Load the dataset
    df = pd.read_csv(data_file)

    # Ensure Quantity is treated as numeric
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce').fillna(0).astype(int)

    # Apply encoding to create a basket of items for each transaction
    basket = df.groupby(['Transaction ID', 'Product Name'])['Quantity'].sum().unstack().reset_index().fillna(0).set_index('Transaction ID')

    # Encode quantities to 1 (presence) or 0 (absence)
    def encode_units(x):
        return x >= 1

    # Apply encoding to all columns in the DataFrame
    basket_encoded = basket.apply(lambda x: x.map(encode_units))

    # Apply the Apriori algorithm with the specified minimum support threshold
    frequent_itemsets = apriori(basket_encoded, min_support=min_support, use_colnames=True)

    # Generate association rules with the specified minimum confidence threshold
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

    # Check if rules DataFrame is empty
    if rules.empty:
        print("No association rules found.")
    else:
        # Display rules with higher confidence for detailed inspection
        high_confidence_rules = rules[rules['confidence'] > 0.5]
        print("High confidence rules:")
        print(high_confidence_rules)
        
        # Print all association rules
        print("All association rules:")
        print(rules)

        # Plotting support for each itemset with annotation for high-confidence rules and advice messages
        plt.figure(figsize=(10, 6))
        support = frequent_itemsets['support']
        itemsets = [', '.join(itemset) for itemset in frequent_itemsets['itemsets']]
        plt.barh(itemsets, support, color='skyblue')
        plt.xlabel('Support')
        plt.title('Support of Itemsets')

        # Add annotations for high-confidence rules and advice messages
        for idx, rule in high_confidence_rules.iterrows():
            antecedents = list(rule['antecedents'])
            consequents = list(rule['consequents'])
            support = rule['support']
            
            # Annotation for rules
            plt.annotate(f'{", ".join(antecedents)} -> {", ".join(consequents)}\nSupport: {support:.2f}',
                         xy=(support, itemsets.index(', '.join(antecedents))), xytext=(5, 5),
                         textcoords='offset points', ha='left', va='center', fontsize=10, color='brown')

            # Generate advice messages based on rules
            if len(antecedents) == 1 and len(consequents) == 1:
                antecedent = antecedents[0]
                consequent = consequents[0]
                message = f"Customers who buy {antecedent} are likely to also purchase {consequent}. Consider bundling these items together or placing them adjacent in displays to increase sales."
                
                # Annotation for advice messages
                plt.annotate(message, xy=(support, itemsets.index(', '.join(antecedents))), xytext=(5, -20),
                             textcoords='offset points', ha='left', va='top', fontsize=8, color='blue')

        plt.gca().invert_yaxis()  # Invert y-axis to have the highest support at the top
        plt.tight_layout()
        plt.show()
        
# Example usage
if __name__ == "__main__":
    data_file = 'market_data.csv'
    analyze_association_rules(data_file, min_support=0.05, min_confidence=0.1)