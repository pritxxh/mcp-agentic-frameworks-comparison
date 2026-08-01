# Contract Analysis Test Suite

## Overview

Complete test suite with 6 diverse contracts covering different scenarios, risk levels, and edge cases.

## Test Contracts

### 1. Standard Service Agreement (LOW-MEDIUM Risk)
**File:** `sample-contract-1.txt`  
**Type:** Professional services  
**Parties:** TechCorp Inc. (Provider) / StartupCo LLC (Client)  
**Key Terms:**
- Payment: $10,000/month, NET 30
- Liability: LIMITED to 2x monthly fees
- Insurance: $1M required
- Term: 12 months with auto-renewal
- Termination: 60 days notice

**Expected Risk:** LOW (15-25 points)  
**Should Notify:** No  
**Use For:** Baseline comparison, standard contract patterns

---

### 2. High-Risk Consulting Agreement (CRITICAL Risk) ✅ TESTED
**File:** `sample-contract-2-high-risk.txt`  
**Type:** Consulting  
**Parties:** BigCorp International (Company) / John Doe (Consultant)  
**Key Terms:**
- Payment: $200/hour, NET 90
- Liability: UNLIMITED
- Insurance: None
- Term: Indefinite
- Termination: Company only, no notice required

**Expected Risk:** CRITICAL (70-80 points)  
**Should Notify:** YES  
**Use For:** Testing risk detection, notification triggers

---

### 3. Balanced Independent Contractor (LOW Risk)
**File:** `sample-contract-3-balanced.txt`  
**Type:** Data analytics consulting  
**Parties:** DataTech Solutions LLC (Client) / Maria Rodriguez (Contractor)  
**Key Terms:**
- Payment: $150/hour, NET 15
- Liability: Limited to 6 months fees, mutual protection
- Insurance: $500K/$1M required
- Term: 6 months
- Termination: 30 days notice (either party)
- IP: Balanced (client owns deliverables, contractor keeps tools)

**Expected Risk:** LOW (10-20 points)  
**Should Notify:** No  
**Use For:** Testing balanced contract recognition, IP analysis

---

### 4. Software License Agreement (MEDIUM Risk)
**File:** `sample-contract-4-software-license.txt`  
**Type:** SaaS/Software licensing  
**Parties:** CloudSoft Inc. (Licensor) / Enterprise Corp. (Licensee)  
**Key Terms:**
- Payment: $50K annually + $10K maintenance, NET 45
- Liability: Limited to 12 months fees
- Warranties: DISCLAIMED (except 90-day conformance)
- Term: 2 years auto-renew
- Termination: 30 days cure for breach, immediate for non-payment

**Expected Risk:** MEDIUM (30-40 points)  
**Should Notify:** No  
**Use For:** Testing warranty disclaimers, SaaS-specific terms

---

### 5. Mutual NDA (LOW Risk)
**File:** `sample-contract-5-nda.txt`  
**Type:** Non-disclosure agreement  
**Parties:** InnovateTech Inc. / Strategic Partners LLC  
**Key Terms:**
- Mutual confidentiality obligations
- Term: 3 years active + 2 years survival
- Exceptions: standard (public, prior knowledge, independent)
- Remedies: Injunctive relief available

**Expected Risk:** LOW (5-10 points)  
**Should Notify:** No  
**Use For:** Testing non-standard contract types, mutual obligations

---

### 6. Minimal Freelance Contract (HIGH Risk - Edge Case)
**File:** `sample-contract-6-minimal.txt`  
**Type:** Freelance web development  
**Parties:** WebDesignCo (Developer) / Local Restaurant Group (Client)  
**Key Terms:**
- Payment: $5,000 flat fee (no payment terms specified)
- NO liability provisions
- NO insurance requirements
- NO termination clause
- NO dispute resolution
- NO confidentiality
- Minimal IP language ("keeps code samples")

**Expected Risk:** MEDIUM-HIGH (40-55 points)  
**Should Notify:** Possibly (if >= 50)  
**Use For:** Testing detection of MISSING clauses, incomplete contracts

---

## Risk Score Reference

- **0-20:** LOW - Well-balanced, standard protections
- **20-40:** MEDIUM - Some concerns, review recommended  
- **40-60:** HIGH - Significant issues, legal review needed
- **60+:** CRITICAL - Do not sign, major red flags

## Testing Strategy

### Phase 1: Individual Contract Testing
Test each contract through:
1. Claude Desktop (baseline - you've done 2 already)
2. LangGraph workflow
3. CrewAI multi-agent
4. Custom orchestrator

### Phase 2: Comparison Metrics
For each framework, measure:
- Execution time
- Tool call count
- Risk score accuracy
- Notification accuracy
- Consistency across runs

### Phase 3: Edge Case Validation
Focus on Contract #6 (minimal):
- Does it detect MISSING clauses?
- Does it flag incomplete protection?
- Does it handle short/informal contracts?

### Phase 4: Stress Testing
- Very long contracts (5000+ words)
- Contracts with unusual structures
- Multiple similar contracts in sequence

## Expected Outcomes

### All Frameworks Should:
1. ✅ Detect unlimited liability in Contract #2
2. ✅ Flag missing clauses in Contract #6
3. ✅ Recognize balanced terms in Contract #3
4. ✅ Properly score each risk level
5. ✅ Trigger notification only for high-risk contracts

### Framework Differences Expected:
- **LangGraph:** Most deterministic, consistent scores
- **CrewAI:** More autonomous, may provide deeper analysis
- **Custom:** Fastest, most transparent execution

## Test Data Summary

| Contract | Type | Risk Level | Notify? | Key Test Focus |
|----------|------|------------|---------|----------------|
| #1 | Service | LOW-MED | No | Baseline |
| #2 | Consulting | CRITICAL | YES | High risk detection |
| #3 | Contractor | LOW | No | Balanced terms |
| #4 | License | MEDIUM | No | SaaS/disclaimers |
| #5 | NDA | LOW | No | Mutual obligations |
| #6 | Freelance | MED-HIGH | Maybe | Missing clauses |

## Usage

```bash
# Test single contract
python test_runner.py --contract sample-contract-2-high-risk.txt --framework langgraph

# Test all contracts with one framework
python test_runner.py --all-contracts --framework langgraph

# Run full comparison
python compare_all.py
```

## Success Criteria

✅ All 6 contracts analyzed successfully  
✅ Risk scores consistent with expectations (±10 points)  
✅ Notification triggered for Contract #2 only  
✅ All frameworks complete without errors  
✅ Execution times reasonable (< 30 seconds per contract)  
✅ Metrics collected for comparison
