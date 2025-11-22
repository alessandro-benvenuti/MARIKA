# HealthcareMAS AI Coding Instructions

## Project Overview
This is a **Multi-Agent System (MAS) for healthcare assistance** - an early-stage Python project focused on building intelligent agents for healthcare applications. The project is licensed under Apache 2.0.

## Project Structure & Conventions

### Environment Setup
- **Environment variables**: Configuration stored in `.env` (includes `OPEN_AI_KEY`)
- **Python environment**: Standard Python project with comprehensive `.gitignore` for Python ecosystems
- **Dependencies**: Project appears to use OpenAI API (based on env var)

### Development Patterns
- **Language**: Python-focused development
- **Licensing**: Apache 2.0 - ensure any new code maintains compatibility
- **Version control**: Git with standard Python `.gitignore` patterns

## Key Development Considerations

### Healthcare Domain Context
- This is a healthcare-focused multi-agent system - consider:
  - Patient data privacy and HIPAA compliance implications
  - Medical terminology and healthcare workflows
  - Multi-agent coordination patterns for healthcare scenarios
  - Potential integration with healthcare APIs or systems

### Multi-Agent System Architecture
When developing agent components, consider:
- **Agent communication protocols**: How agents will interact and share information
- **Agent specialization**: Different agents for different healthcare functions (diagnosis, scheduling, monitoring, etc.)
- **Coordination mechanisms**: How agents collaborate on complex healthcare tasks
- **State management**: How agent states and patient context are maintained

### AI Integration Patterns
- **OpenAI Integration**: Project includes OpenAI API key setup
- **LLM Usage**: Consider healthcare-specific prompt engineering and safety measures
- **Agent Intelligence**: Balance between different AI capabilities for various healthcare agents

## Getting Started
Since this is an early-stage project:
1. Ensure Python environment is properly configured
2. Set up `.env` file with required API keys (OpenAI key template provided)
3. Consider creating initial project structure for:
   - Agent definitions and classes
   - Healthcare domain models
   - Communication protocols
   - Configuration management

## Security & Compliance Notes
- **API Keys**: Never commit `.env` file (already properly gitignored)
- **Healthcare Data**: Implement appropriate data handling for patient information
- **Privacy**: Consider HIPAA compliance requirements for any patient data handling

## Future Development Areas
Based on project name and context, anticipate developing:
- Agent base classes and interfaces
- Healthcare domain-specific data models
- Inter-agent communication systems
- Integration with healthcare APIs or databases
- Testing frameworks for multi-agent scenarios