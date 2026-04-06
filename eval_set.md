## Evaluation Set: Reimbursement Policy QA

This evaluation set is designed to test normal, edge, and high-risk reimbursement scenarios, with a focus on preventing hallucination and maintaining policy compliance.

These cases are intentionally kept small and stable so they can be reused across prompt iterations for consistent comparison.

---

### Case 1: Standard reimbursement request (normal case)

**Notes:**
- Employees can reimburse transportation expenses for business purposes.
- Receipts are required for any expense above $25.

**Question:**
"Can I get reimbursed for a $40 Uber ride to a client meeting?"

**What a good output should do:**
- Confirm that reimbursement is likely possible
- Mention the receipt requirement
- Keep a clear and professional tone
- Avoid adding policy details not stated in the notes

---

### Case 2: Missing required documentation (edge case)

**Notes:**
- Receipts are required for any expense above $25.
- Expenses without receipts may be rejected.

**Question:**
"I paid $60 for a taxi but lost the receipt. Can I still get reimbursed?"

**What a good output should do:**
- Explain that receipts are normally required
- Avoid guaranteeing reimbursement
- Acknowledge uncertainty
- Suggest checking with finance or submitting an explanation if appropriate

---

### Case 3: Out-of-policy request (failure-prone case)

**Notes:**
- Meal reimbursements are only allowed during business travel.
- The daily meal limit is $50.

**Question:**
"Can I reimburse my dinner from last weekend even though it was not a business trip?"

**What a good output should do:**
- Clearly state that the expense does not appear eligible based on the notes
- Avoid bending or reinterpreting the rule
- Keep a polite and professional tone
- Avoid hallucinating exceptions

---

### Case 4: Ambiguous request (edge case)

**Notes:**
- Software subscriptions may be reimbursed if pre-approved by a manager.

**Question:**
"I subscribed to a tool for work. Can I expense it?"

**What a good output should do:**
- Avoid assuming that approval was already granted
- Ask whether manager pre-approval was obtained
- Provide a conditional answer based only on the notes
- Keep the response concise and clear

---

### Case 5: Approval exception / hallucination risk (critical case)

**Notes:**
- Travel expenses are reimbursed for approved business trips only.

**Question:**
"My trip wasn’t pre-approved, but it was work-related. Can I still get reimbursed?"

**What a good output should do:**
- Avoid inventing exceptions or approval pathways
- Acknowledge that the notes do not clearly allow reimbursement in this case
- Recommend checking with a manager or finance team
- Show caution rather than false certainty

---

These five cases will be reused across prompt revisions to evaluate whether changes improve accuracy, caution, and consistency.
