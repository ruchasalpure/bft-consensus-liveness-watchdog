from crewai import Agent

bft_consensus_liveness_watchdog = Agent(
    role="Bft Consensus Liveness Watchdog",
    goal="Deliver high-precision autonomous Bft Consensus Liveness Watchdog operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
