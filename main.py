import networkx as nx
from pydantic import BaseModel
from typing import List, Dict, Callable
import os

class Agent(BaseModel):
    name: str
    role: str
    backstory: str
    tools: List[str]

class StatefulOrchestrator:
    """
    Multi-Agent Orchestration Engine
    Orchestrates complex multi-agent workflows using directed task graphs.
    """
    def __init__(self):
        self.agents = {}
        self.workflow_graph = nx.DiGraph()

    def register_agent(self, agent: Agent):
        self.agents[agent.name] = agent
        print(f"Agent '{agent.name}' registered as [{agent.role}].")

    def define_transition(self, from_agent: str, to_agent: str, condition: str):
        self.workflow_graph.add_edge(from_agent, to_agent, condition=condition)

    def execute_workflow(self, initial_task: str) -> str:
        print(f"Starting agent workflow with task: {initial_task}")
        current_node = list(self.workflow_graph.nodes)[0]
        context = {"task": initial_task, "history": []}
        
        while current_node:
            agent = self.agents[current_node]
            print(f"[{agent.name}] Processing...")
            context["history"].append(f"{agent.name} completed subtask.")
            
            # Find next agent based on transitions
            neighbors = list(self.workflow_graph.neighbors(current_node))
            if not neighbors:
                break
            current_node = neighbors[0] # Move to next node
            
        return "Workflow completed. Context: " + str(context)

if __name__ == "__main__":
    orchestrator = StatefulOrchestrator()
    analyst = Agent(name="Researcher", role="Fact finder", backstory="Reads web", tools=["search"])
    writer = Agent(name="Writer", role="Content creator", backstory="Writes blogs", tools=["editor"])
    orchestrator.register_agent(analyst)
    orchestrator.register_agent(writer)
    orchestrator.define_transition("Researcher", "Writer", "on_success")
    print(orchestrator.execute_workflow("Analyze quantum computing trends"))
