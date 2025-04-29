# Agno Reasoning Agents: Your Local AI Research & Reasoning Assistant (Powered by Qwen3 & Agno)

Research complex topics with an AI that thinks, searches, and explains—all running privately on your computer. This assistant harnesses the power of [Agno](https://github.com/agno-ai/agno)'s multi-agent framework to coordinate specialized AI agents with advanced reasoning capabilities. The system leverages Agno's built-in reasoning engine to thoroughly analyze questions, evaluate evidence, and draw logical conclusions. All processing happens locally using Qwen3 through Ollama with 100% privacy—no data sent to external servers.

## Why Use This?

This project gives you a head start if you want to:

- **Build Your Own AI Assistant**: See how multiple AI agents can work together
- **Customize for Your Needs**: Add features specific to your business or problem
- **Learn About AI Agents**: Understand how Agno orchestrates multiple specialized AIs
- **Save Development Time**: Start with working code instead of building from scratch

## How It Works

The project uses a team of specialized AI agents working together:

- **Supervisor**: Coordinates the teamwork between agents
- **Thinker**: Analyzes questions in depth
- **Researcher**: Finds facts and information online via DuckDuckGo
- **Responder**: Creates clear, helpful answers based on thinking and research

## Requirements

- Python 3.8+
- [Agno](https://github.com/agno-ai/agno) - A flexible framework for building AI assistants
- [Ollama](https://ollama.ai/) with qwen3:4b model (or use your preferred model)

## Getting Started

1. Clone this repository:
```bash
git clone https://github.com/lesteroliver911/agno-reasoning-agents-local
cd researchgpt-local
```

2. Install dependencies:
```bash
pip install agno
```

3. Install Ollama and the required model:
```bash
# Install Ollama - follow instructions at https://ollama.ai/
ollama pull qwen3:4b
```

## Using Your Assistant

Run the application:

```bash
python main.py
```

Ask any question, and your assistant will:
1. Understand what you're asking about
2. Look up information when needed
3. Think through the answer carefully
4. Provide a helpful, well-organized response

Type 'exit' or 'quit' to end the conversation.

## Customization Ideas for Your Project

- **Industry-Specific Knowledge**: Train it on your business domain
- **Different AI Models**: Use models that best fit your needs and budget
- **Connect to Your Data**: Link to your databases or knowledge bases
- **Better User Experience**: Add a web, mobile, or chat interface
- **Business Integration**: Connect with your existing systems and tools

## Questions You Can Ask

- "How can AI improve patient outcomes in emergency medicine?"
- "What are the best practices for optimizing hospital supply chain management?"
- "How is machine learning being used to improve last-mile delivery efficiency?"

## Contributing

We welcome contributions! Fork this repository, make your changes, and submit a pull request.

## License

MIT - Feel free to use, modify, and distribute as needed for your startup or project. 
