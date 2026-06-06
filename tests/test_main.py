import pytest
import main

def test_agent_instantiation():
    # Verify that the class Agent is inspectable and loadable
    assert hasattr(main, 'Agent')

def test_statefulorchestrator_instantiation():
    # Verify that the class StatefulOrchestrator is inspectable and loadable
    assert hasattr(main, 'StatefulOrchestrator')

