from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

# Define the hardcoded principles for positive and critical analysis
PRINCIPLES_POSITIVE = """
Does the proposal demonstrate a clear market need or demand?
Does the proposal offer a unique value proposition?
Is there a viable business model?
Is there a clear understanding of the target audience?
Does the proposal demonstrate a competitive advantage?
Is there a clear plan for execution?
Does the proposal demonstrate the team's skills and expertise?
Is there an understanding of the market and potential market failures?
Does the proposal consider the potential for catalytic funding?
"""

PRINCIPLES_CRITICAL = """
Why is the proposal not demonstrating a clear market need or demand?
Why is the proposal not offering a unique value proposition?
Why the proposal is not a viable business model?
Why there is not a clear understanding of the target audience?
Why is the proposal not demonstrating a competitive advantage?
Why there is no clear plan for execution?
Why is the proposal not demonstrating the team's skills and expertise?
Why is the proposal not showing an understanding of the market and potential market failures?
How is the proposal considering the potential for catalytic funding?
"""

def generate_principles_recommendation(principles, texts):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Given the principles of social investing that {principles}, analyze the following texts critically and objectively, give me a summary of what you thought as a long paragraph: '{', '.join(texts)}'",
        max_tokens=1000
    )
    return response.choices[0].text.strip()

def generate_recommendations_and_scores(text, section_type, analysis_type):
    if analysis_type == "positive":
        prompt_text = f"Given the understanding of 'Outcomes over Outputs' where outcomes are changes in human or institutional behaviour that drive business results or public impact, and outputs are the tangible results of a project, coupled with the principles of experimentation and continuous improvement, analyze the following {section_type.lower()} and provide a brief summary on how well it focuses on outcomes and embraces the principles of experimentation and continuous improvement: '{text}'"
    else:  # For critical analysis
        prompt_text = f"Given the understanding of 'Outcomes over Outputs', critically analyze the following {section_type.lower()} and provide a brief summary highlighting areas where it falls short in focusing on outcomes, and where it might not fully embrace the principles of experimentation and continuous improvement: '{text}'"
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        max_tokens=1000
    )
    return response.choices[0].text.strip()

def analyze_whole_proposal_against_principles(principles, texts):
    principle_questions = principles.strip().split('\n')
    analysis = ""
    for i, question in enumerate(principle_questions):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{question} Analyze the whole grant proposal and provide a brief but substantive answer: '{' '.join(texts)}'",
            max_tokens=1000
        )
        analysis += f"{i+1}. {question} <br>Answer: {response.choices[0].text.strip()}<br><br>"
    return analysis

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract data from the form
        sections = ['Idea', 'Opportunity Approach', 'Desired Impact', 'Strategy Alignment']
        texts = [request.form[s.replace(' ', '_').lower()] for s in sections]

        # Generate the analysis results for both the positive and critical perspectives
        principles_recommendation_positive = generate_principles_recommendation(PRINCIPLES_POSITIVE, texts)
        principles_recommendation_critical = generate_principles_recommendation(PRINCIPLES_CRITICAL, texts)

        section_recommendations = {}
        for section, text in zip(sections, texts):
            recommendation_positive = generate_recommendations_and_scores(text, section, "positive")
            recommendation_critical = generate_recommendations_and_scores(text, section, "critical")
            section_recommendations[section] = (recommendation_positive, recommendation_critical)

        principle_analysis_positive = analyze_whole_proposal_against_principles(PRINCIPLES_POSITIVE, texts)
        principle_analysis_critical = analyze_whole_proposal_against_principles(PRINCIPLES_CRITICAL, texts)

        return render_template('results.html', 
            principles_recommendation_positive=principles_recommendation_positive,
            principles_recommendation_critical=principles_recommendation_critical,
            section_recommendations=section_recommendations,
            principle_analysis_positive=principle_analysis_positive,
            principle_analysis_critical=principle_analysis_critical
        )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
