
# IPO Analysis & Market Research Tool

🤖 **IPO Analysis & Market Research** is a Streamlit-based application designed to help users analyze Initial Public Offerings (IPOs) and market trends using advanced AI tools. It integrates **CrewAI** agents, **YouTube channel analysis**, and web search tools to provide comprehensive insights.

---

## Features

- 📊 **IPO Analysis**: Generate detailed research and recommendations for specific IPOs in the Indian market.
- 🎥 **YouTube Video Analysis**: Extract and summarize market trends and IPO-related content from YouTube channels.
- 🔍 **AI-Powered Research**: Use advanced natural language models to analyze and present market insights.
- 🖋️ **Content Creation**: Produce well-structured blog posts and market sentiment reports with actionable insights.

---

## Code Overview

### Import Statements

The code includes the following libraries and tools:
- `os`: To manage environment variables.
- `streamlit`: To build the web app interface.
- `crewAI`: For orchestrating tasks and agents.
- `dotenv`: To load environment variables.
- `crewai_tools`: To leverage tools like `SerperDevTool` and YouTube tools for video and channel analysis.

### Core Functionalities

- **Page Configuration**: Sets up the Streamlit page with titles, icons, and layouts.
- **User Input**: Collects IPO name and YouTube channel information.
- **Agent Framework**:
  - **Research Agent**: Gathers detailed IPO data and market sentiment.
  - **Content Writing Agent**: Converts research into readable and engaging content.
  - **YouTube Analysis Agent**: Extracts insights from relevant videos.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the project directory.
   - Add your API keys and credentials for tools like `CrewAI` and `SerperDevTool`.

4. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. **Enter IPO Details**: In the sidebar, input the IPO name you want to analyze.
2. **Generate Content**: Click the "Generate Content" button to create a detailed report.
3. **YouTube Analysis**: Provide a YouTube channel link and click "Generate Analysis from YouTube Video" for video-based insights.
4. **View Results**: The generated content will appear in the main section of the app.

---

## Example Outputs

### IPO Analysis Report
- **Executive Summary**: Key findings and insights.
- **Market Sentiment**: Strengths and risks of the IPO.
- **Company Data**: Year-wise revenue, profit, and asset information.
- **IPO Objectives**: Fund-raising purpose and objectives.

### YouTube Video Summary
- **Detailed Insights**: Extracted information from videos.
- **Blog Post**: Comprehensive and engaging markdown content.

---

## File Structure

```plaintext
├── app.py               # Main application script
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not included in repo)
├── README.md            # Documentation
└── data/                # Folder for saved analysis files (optional)
```

---

## Technical Details

- **Core Libraries**:
  - `streamlit`: For building the web app interface.
  - `CrewAI`: For task delegation and agent orchestration.
  - `dotenv`: For managing environment variables.
- **Agents**:
  - **Senior Market Research Analyst**: Conducts comprehensive IPO analysis.
  - **Content Writer**: Crafts engaging and informative blog posts.
  - **YouTube Researcher**: Extracts and summarizes relevant video content.

---

## Requirements

- Python 3.7 or later
- API keys for:
  - `CrewAI` tools
  - `SerperDevTool`

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request for any changes or enhancements.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- Built with ❤️ using [Streamlit](https://streamlit.io) and [CrewAI](https://crewai.io).
- Powered by [Cohere](https://cohere.ai) and `command-r` model.
