def rule_based_decision(data, matched_clause=None):
    result = {
        "decision": None,
        "amount": 0,
        "justification": {
            "rules_triggered": [],
            "matched_clause": matched_clause or "No clause matched"
        }
    }

    if (
        data.get("policy_age_months") is not None
        and data.get("procedure") == "knee surgery"
        and data["policy_age_months"] < 6
    ):
        result["decision"] = "reject"
        result["justification"]["rules_triggered"].append({
            "rule": "Policy must be active for more than 6 months before knee surgery",
            "clause": matched_clause
        })
    else:
        result["decision"] = "approve"
        result["amount"] = 25000
        result["justification"]["rules_triggered"].append({
            "rule": "Procedure eligible based on policy age and coverage",
            "clause": matched_clause
        })

    return result