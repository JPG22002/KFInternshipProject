# Grant Proposal Analysis Tool

## Overview
This tool leverages OpenAI's GPT-3 to analyze grant proposals. It's designed to assist the Investment Committee by streamlining the evaluation process, saving time, and providing in-depth insights into the proposals. The application offers both positive and critical analyses based on predefined principles.

## Features
- **Two-Tiered Analysis**: Provides both a supportive (positive) and a stringent (critical) assessment of grant proposals.
- **Customizable Sections**: Allows analysis of various sections of a proposal, such as Idea, Opportunity Approach, Desired Impact, and Strategy Alignment.
- **Principles-based Evaluation**: Uses a set of hardcoded principles to guide the analysis.
- **User-friendly Interface**: Simple and intuitive web interface for easy interaction.

## Installation and Setup

### Prerequisites
- Python 3
- Flask
- OpenAI API Key

### Steps
1. **Install Python**: Download and install Python from [Python's official website](https://www.python.org/downloads/).

2. **Clone Repository**: Clone or download this repository to your local machine.

3. **Install Dependencies**: 
   - Open the terminal or command prompt.
   - Navigate to the project directory.
   - Run `pip install flask openai`.

4. **Set API Key**: Replace `'YOUR_OPENAI_API_KEY'` in the `OO.py` file with your actual OpenAI API key.

5. **Run the Application**:
   - In the terminal, execute `python OO.py`.
   - Open a web browser and go to `http://localhost:5000`.

## Usage
Fill in the required fields in the web form with the details of the grant proposal and submit. The application will display both positive and critical analyses for the general assessment and each specified section.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to reach out to me if there are any issues
