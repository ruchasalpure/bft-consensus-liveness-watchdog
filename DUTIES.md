# Duties and Responsibilities for BFT Consensus Liveness Watchdog Agent

## Dual-Control Architecture
Maker:
view-change-monitor

Checker:
byzantine-fault-checker

## Operational Workflow
1. The Maker (view-change-monitor) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (byzantine-fault-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
