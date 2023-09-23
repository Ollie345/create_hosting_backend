# Slack Information Endpoint
This is a Flask application that creates an endpoint at */api* to provide specific information in JSON format based on query parameters.

## How it Works

### Endpoint
The application sets up a Flask endpoint at /api. When a GET request is made to this endpoint, it expects two query parameters: slack_name and track.

### Functionality
1. Importing Libraries:
    * The necessary libraries Flask, request, and datetime are imported.

2. Initializing Flask App:
    * A Flask application is created and named app.

3. Setting Up Endpoint:
    * **`@app.route('/api', methods=['GET'])`** defines the route for accessing the API.

4. get_info Function:
    * The function get_info is defined to handle the GET request.
    * It retrieves slack_name and track from the request's query parameters.

5. Current Day and UTC Time:
    * The current day of the week and UTC time are determined using the **`datetime`** module.

6. GitHub URLs:
    * The GitHub repository URL and a specific file URL are predefined.

7. Creating Response:
    * The gathered information, including **`slack_name`**, **`current_day`**, **`utc_time`**, **`track`**, and the GitHub URLs, is assembled into a dictionary.

8. Returning JSON Response:
    * The response is converted to JSON format using **`jsonify()`** and sent back as the API's output.

9. Running the Application:
    * If the script is run directly (not imported), the Flask application is started in debug mode.

## How to Use
1. Install Flask using **`pip install Flask`**.

2. Run the script.

3. Make a GET request to **`http://localhost:5000/api`** with the required query parameters (**`slack_name`** and **`track`**).
  Example: **`http://localhost:5000/api?slack_name=example_name&track=backend`**

The API will respond with a JSON containing the specified information.

## Endpoint Output Format
```json
{
  "slack_name": "example_name",
  "current_day": "Monday",
  "utc_time": "2023-08-21T15:04:05Z",
  "track": "backend",
  "github_file_url": "https://github.com/Ollie345/create_hosting_backend/blob/main/app.py",
  "github_repo_url": "https://github.com/Ollie345/create_hosting_backend",
  "status_code": 200
}
```
## Dependencies
* Flask
* datetime
