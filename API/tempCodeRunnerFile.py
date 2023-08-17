from flask import Flask, request, jsonify
from flask_cors import CORS
from srujan import analyze_Description,load_and_preprocess_article, analyze_sentiment, analyze_keywords, analyze_summary

app = Flask(__name__)
CORS(app)
@app.route('/analyze', methods=['POST'])
def analyze_article():
    try:
        data = request.json
        article_url = data['url']
        analysis_type = data['analysisType']
        final_article = load_and_preprocess_article(article_url)

        if analysis_type == 'sentiment':
            result = analyze_sentiment(final_article)
        elif analysis_type == 'keywords':
            result = analyze_keywords(article_url)
        elif analysis_type == 'summary':
            result = analyze_summary(article_url)
        elif analysis_type == 'description':
            result = analyze_Description(final_article)  
        else:
            result = {'error': 'Invalid analysis type'}

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
