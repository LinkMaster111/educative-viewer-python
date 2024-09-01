from flask import Flask, render_template, send_from_directory, jsonify, request
import os
import json

app = Flask(__name__)

# Set the base directory for HTML files
BASE_DIR = ''
# Update this path to your actual HTML files directory


def map_json_to_files(base_dir):
    """Map JSON topics to available offline HTML files within all subdirectories."""
    file_mapping = {}

    # Iterate over all subdirectories in the base directory
    for root, dirs, files in os.walk(base_dir):
        for dir_name in dirs:
            toc_file = os.path.join(base_dir, dir_name, '__toc__.json')
            if os.path.exists(toc_file):
                with open(toc_file, 'r') as file:
                    json_data = json.load(file)

                # Extract the table of contents (toc) from JSON
                toc = json_data.get("toc", [])

                for category in toc:
                    category_name = category['category']
                    file_mapping.setdefault(category_name, [])
                    
                    for topic in category['topics']:
                        topic_title = topic[0]
                        topic_file_name = topic[1]

                        # Construct the path for the corresponding HTML file
                        html_file_path = os.path.join(dir_name, topic_file_name + "/" + topic_file_name + '.html')

                        # Check if the HTML file exists in the current directory
                        if os.path.exists(os.path.join(BASE_DIR, html_file_path)):
                            offline_file = html_file_path
                        else:
                            offline_file = None

                        file_mapping[category_name].append({
                            'title': topic_title,
                            'offline_file': offline_file
                        })
    
    return file_mapping

@app.route('/', methods=['GET', 'POST'])
def index():
    global BASE_DIR
    if request.method == 'POST':
        # Update the base directory from the POST request

        BASE_DIR = request.form.get('baseDir').replace('\\', '/')
    
    # Map JSON data to HTML files using the current base directory
    file_mapping = map_json_to_files(BASE_DIR)
    return render_template('index.html', file_mapping=file_mapping)


# Route for serving HTML files
@app.route('/view/<path:filename>')
def view_file(filename):
    return send_from_directory(BASE_DIR, filename)


if __name__ == '__main__':
    app.run(debug=True)