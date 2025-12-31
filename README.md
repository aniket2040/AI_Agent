# AI Search Agent

A powerful AI-powered search agent built with Streamlit and Pydantic AI, utilizing the Tavily search API to provide intelligent, context-aware search results.

## Features

- **Intelligent Search**: Leverages advanced AI models to perform contextual searches using the Tavily search engine.
- **Real-time Results**: Provides instant search results with detailed information from reliable sources.
- **User-friendly Interface**: Clean and intuitive Streamlit-based web interface for easy interaction.
- **API Integration**: Seamlessly integrates with Tavily's search API for comprehensive web search capabilities.
- **Customizable Agent**: Built with Pydantic AI for flexible agent configuration and tool usage.

## Prerequisites

- Python 3.8 or higher
- A Tavily API key (obtain from [Tavily](https://tavily.com/))
- A Groq API key (obtain from [Groq](https://groq.com/))

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Searching_AI_Agent
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     .\.venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:

   ```bash
   pip install streamlit pydantic-ai-slim[tavily]
   ```

## Configuration

1. Obtain API keys:

   - Tavily API key: Sign up at [Tavily](https://tavily.com/) and get your API key.
   - Groq API key: Sign up at [Groq](https://groq.com/) and get your API key.

2. For local development, create a `.env` file in the project root:

   ```
   TAVILY_API_KEY=your-tavily-api-key-here
   GROQ_API_KEY=your-groq-api-key-here
   ```

   For Streamlit Community Cloud deployment, set these as secrets in your Streamlit app settings.

## Usage

1. Ensure the virtual environment is activated.

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

4. Enter your search query in the input field and press Enter.

5. The AI agent will process your query and return relevant search results.

## Deployment on Streamlit Community Cloud

1. Push your code to a GitHub repository.

2. Go to [Streamlit Community Cloud](https://share.streamlit.io/) and sign in with your GitHub account.

3. Click "New app" and select your repository.

4. Set the main file path to `app.py`.

5. In the app settings, add your API keys as secrets:

   - `TAVILY_API_KEY`: Your Tavily API key
   - `GROQ_API_KEY`: Your Groq API key

6. Deploy the app.

## Project Structure

```
Searching_AI_Agent/
├── app.py                 # Main Streamlit application
├── agent_utils.py         # AI agent configuration and search functionality
├── .venv/                 # Virtual environment (created during installation)
├── requirements.txt       # Python dependencies (if present)
└── README.md             # This file
```

## Dependencies

- **Streamlit**: Web app framework for the user interface
- **Pydantic AI**: AI agent framework with tool integration
- **Tavily Python SDK**: Official Python client for Tavily search API

## API Keys

This project requires two API keys:

1. **Tavily API Key**: Used for web search functionality
2. **Groq API Key**: Used for AI model inference (Llama 3.1)

Ensure these are set correctly before running the application.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web app framework
- [Pydantic AI](https://pydantic-ai.readthedocs.io/) for the AI agent framework
- [Tavily](https://tavily.com/) for the search API
- [Groq](https://groq.com/) for the AI model hosting

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

## Version History

- v1.0.0: Initial release with basic AI search functionality
