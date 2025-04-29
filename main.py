from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.team import Team
from agno.tools.reasoning import ReasoningTools
from agno.tools.duckduckgo import DuckDuckGoTools

# Define the worker agents that will handle specific tasks
def create_thinker_agent():
    """Creates an agent that shows its thinking process."""
    return Agent(
        name="Thinker",
        role="Think through complex questions step by step",
        model=Ollama(id="qwen3:4b"),
        tools=[ReasoningTools(add_instructions=True)],
        instructions=[
            "Analyze the user's query step by step",
            "Think deeply about all aspects of the question",
            "Consider multiple angles before giving your final answer"
        ],
        show_tool_calls=True,
        markdown=True
    )

def create_researcher_agent():
    """Creates an agent that researches information from the web."""
    return Agent(
        name="Researcher",
        role="Search for factual information from the web",
        model=Ollama(id="qwen3:4b"),
        tools=[DuckDuckGoTools()],
        instructions=[
            "Use DuckDuckGo to search for accurate information",
            "Include sources in your response",
            "Summarize findings clearly"
        ],
        show_tool_calls=True,
        markdown=True
    )

def create_responder_agent():
    """Creates an agent that focuses on generating clear responses."""
    return Agent(
        name="Responder",
        role="Provide clear and concise responses",
        model=Ollama(id="qwen3:4b"),
        instructions=[
            "Based on the information provided, create a well-formatted response",
            "Be direct and helpful",
            "Format your response appropriately with markdown"
        ],
        markdown=True
    )

# Create the supervisor team with all worker agents
def create_supervisor_team():
    """Creates a supervisor team that delegates tasks to appropriate worker agents."""
    thinker = create_thinker_agent()
    researcher = create_researcher_agent()
    responder = create_responder_agent()
    
    return Team(
        mode="coordinate",  # Use coordinate mode for sequential processing
        members=[thinker, researcher, responder],
        model=Ollama(id="qwen3:4b"),
        success_criteria="A well-researched, well-reasoned and clear response to the user's query",
        instructions=[
            "Analyze the query to determine which agents need to be involved",
            "For factual questions, use the Researcher agent first to gather information",
            "For complex reasoning questions, use the Thinker agent to reason through the problem",
            "Always use the Responder agent last to generate the final response",
            "Not all agents need to be used for every query - choose the most appropriate workflow"
        ],
        markdown=True
    )

def main():
    """Main function to handle CLI chat."""
    print("\n=== Agno Reasoning Agents ===")
    print("Using Qwen3:4b model")
    print("Features:")
    print("- Thinker Agent: Deep reasoning for complex questions")
    print("- Researcher Agent: Web search for factual information")
    print("- Responder Agent: Clear responses based on thinking and research")
    print("\nType 'exit' or 'quit' to end the conversation\n")
    
    team = create_supervisor_team()
    
    while True:
        # Get user input
        user_input = input("\n> ")
        
        # Check for exit command
        if user_input.lower() in ["exit", "quit"]:
            print("\nGoodbye!")
            break
        
        # Empty input check
        if not user_input.strip():
            print("Please enter a message.")
            continue
        
        print("\nProcessing... (complex queries with research may take longer)")
        print("=" * 80)
        
        # Stream the response with full reasoning
        team.print_response(
            message=user_input,
            stream=True,
            stream_intermediate_steps=True,
            show_full_reasoning=True
        )
        
        print("=" * 80)

if __name__ == "__main__":
    main() 
