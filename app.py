# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eweWRwgrN8Jro3iUZQpDY5ofM8Ag3Gc0
"""

!pip install streamlit pyngrok pulp altair pandas

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# cat > app.py << 'EOF'
# import os
# import streamlit as st
# import pulp
# import pandas as pd
# import altair as alt
# 
# # -----------------------------------------------------------------------------
# # Simulated LLM Parser Function
# # -----------------------------------------------------------------------------
# def simulate_llm_parser(user_input: str):
#     """
#     Simulate an LLM-based parser that extracts supply chain parameters
#     from a natural language description.
#     """
#     warehouses = ['A', 'B']
#     stores = ['X', 'Y', 'Z']
#     supply = {'A': 100, 'B': 80}
#     demand = {'X': 50, 'Y': 70, 'Z': 40}
#     costs = {
#         ('A', 'X'): 2,
#         ('A', 'Y'): 4,
#         ('A', 'Z'): 5,
#         ('B', 'X'): 3,
#         ('B', 'Y'): 1,
#         ('B', 'Z'): 2,
#     }
#     explanation = (
#         "Simulated parsing: Extracted 2 warehouses (A, B) with supplies 100 and 80, "
#         "and 3 stores (X, Y, Z) with demands 50, 70, and 40 respectively. "
#         "Shipping costs are: A→X:2, A→Y:4, A→Z:5, B→X:3, B→Y:1, B→Z:2."
#     )
#     return warehouses, stores, supply, demand, costs, explanation
# 
# # -----------------------------------------------------------------------------
# # Optimization Function Using PuLP
# # -----------------------------------------------------------------------------
# def solve_optimization(warehouses, stores, supply, demand, costs):
#     """
#     Formulate and solve the transportation problem using linear programming.
#     """
#     prob = pulp.LpProblem("SupplyChainOptimization", pulp.LpMinimize)
#     shipment_vars = pulp.LpVariable.dicts("Ship", (warehouses, stores), lowBound=0, cat='Continuous')
#     prob += pulp.lpSum([costs[(w, s)] * shipment_vars[w][s] for w in warehouses for s in stores]), "Total_Shipping_Cost"
#     for w in warehouses:
#         prob += pulp.lpSum([shipment_vars[w][s] for s in stores]) <= supply[w], f"Supply_{w}"
#     for s in stores:
#         prob += pulp.lpSum([shipment_vars[w][s] for w in warehouses]) >= demand[s], f"Demand_{s}"
#     prob.solve()
#     solution = {}
#     for w in warehouses:
#         for s in stores:
#             solution[(w, s)] = shipment_vars[w][s].varValue
#     total_cost = pulp.value(prob.objective)
#     status = pulp.LpStatus[prob.status]
#     return solution, total_cost, status
# 
# # -----------------------------------------------------------------------------
# # Main Streamlit Application
# # -----------------------------------------------------------------------------
# def main():
#     st.title("LLM-Driven Supply Chain Optimization Assistant")
#     st.write("This application extracts supply chain parameters from a natural language input, then solves the optimization problem using linear programming.")
# 
#     user_input = st.text_area("Enter your supply chain problem description:", height=150,
#                                 placeholder="Example: We have 2 warehouses (A and B) and 3 stores (X, Y, Z). "
#                                             "Warehouse A has 100 units, Warehouse B has 80 units. "
#                                             "Store X requires 50 units, Store Y requires 70 units, and Store Z requires 40 units. "
#                                             "Shipping costs per unit are as follows: A to X: 2, A to Y: 4, A to Z: 5, B to X: 3, B to Y: 1, B to Z: 2. "
#                                             "Please minimize the total shipping cost.")
# 
#     if st.button("Optimize"):
#         if not user_input.strip():
#             st.error("Input cannot be empty. Please describe your supply chain problem.")
#         else:
#             st.info("Parsing the problem description using a simulated LLM parser...")
#             warehouses, stores, supply, demand, costs, explanation = simulate_llm_parser(user_input)
#             st.subheader("Parsed Parameters")
#             st.write("**Warehouses:**", warehouses)
#             st.write("**Stores:**", stores)
#             st.write("**Supply:**", supply)
#             st.write("**Demand:**", demand)
#             st.write("**Shipping Costs:**", costs)
#             st.write("**Parsing Explanation:**", explanation)
# 
#             st.info("Solving the optimization problem...")
#             solution, total_cost, status = solve_optimization(warehouses, stores, supply, demand, costs)
# 
#             st.subheader("Optimization Results")
#             st.write("**Status:**", status)
#             st.write("**Total Shipping Cost:**", total_cost)
#             st.write("**Shipment Plan:**")
#             for (w, s), qty in solution.items():
#                 st.write(f"From Warehouse {w} to Store {s}: {qty} units")
# 
#             st.success("Optimization complete!")
# 
#             data = []
#             for (w, s), qty in solution.items():
#                 data.append({"Warehouse": w, "Store": s, "Quantity": qty})
#             df = pd.DataFrame(data)
#             chart = alt.Chart(df).mark_bar().encode(
#                 x=alt.X("Store:N", title="Store"),
#                 y=alt.Y("Quantity:Q", title="Shipment Quantity"),
#                 color=alt.Color("Warehouse:N", title="Warehouse"),
#                 tooltip=["Warehouse", "Store", "Quantity"]
#             ).properties(width=600, height=400, title="Optimized Shipment Quantities")
#             st.altair_chart(chart, use_container_width=True)
# 
# if __name__ == "__main__":
#     main()
# EOF

!ngrok authtoken 2tLON0iNWTqpZdSkhTXuH1Wj6lR_2mPKyFA3TUWj6NzjnLMpo
from pyngrok import ngrok
import subprocess
import time

# Set the port number for the Streamlit app
port = 8501

# Open a tunnel on the port using ngrok
public_url = ngrok.connect(port)
print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}/\"".format(public_url, port))

# Launch the Streamlit app in the background
# Use subprocess.Popen to run the command and allow the notebook to continue
process = subprocess.Popen(["streamlit", "run", "app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait a few seconds for the app to start
time.sleep(5)

print("Streamlit app should now be running. Click the URL above to view the app.")