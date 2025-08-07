from semantic_search import build_index, search
from decision_engine import rule_based_decision
import json

# Step 1: Define policy clauses
clauses = [
    "Procedures after 90 days are covered.",
    "Orthopedic surgeries allowed in Maharashtra.",
    "No coverage for pre-existing conditions within first year."
]

# Step 2: Define your input query
query = "46M, knee surgery, Pune, 3-month policy"

# Step 3: Use semantic search to find the best clause
index, db = build_index(clauses)
top_clause = search(query, index, db)[0]

# Step 4: Create structured data manually (we’ll automate this later)
structured_data = {
    "procedure": "knee surgery",
    "location": "Pune",
    "policy_age_months": 3,
    "age": 46
}

# Step 5: Get a decision from your rule engine
result = rule_based_decision(structured_data, matched_clause=top_clause)

# Step 6: Print the result as clean JSON
print(json.dumps(result, indent=2))
