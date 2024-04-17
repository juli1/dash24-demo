# dash24-demo

This repository is a demo for the DASH24 workshop. It contains a sample application
with an API written in Python/Flask. We use this application to show how we can find
security issues in projects and fix them.

## Part 0: Getting started

Bootstrap the project

0. If not installed, install the `venv` module: `apt-get install python3-venv`
1. Install `sqlite3`: `apt-get install sqlite3`
2. Create a virtual environment `python -mvenv venv`
3. Use the virtual environment `source venv/bin/activate`
4. Install all dependencies `pip install -r requirements.txt`
5. Init the database `rm -f db.sqlite ;  sqlite3 db.sqlite < init.sql`

Start the project, invoke

```shell
python service.py
```

## Part 1: Use the API


### List all products

To list all products from the API, use

```shell
curl http://127.0.0.1:5000/api/product/list
```


### Add a product

To add a product via the API< use

```shell
curl -H "Content-Type: application/json" -X POST --data '{"name": "<product-name>"}' http://localhost:5000/api/product/add
```

### Use the web interface

Navigate to <ENTER-URL>


## Part 2: onboard the project on Datadog

1. Navigate to your repository settings
2. Add a secrets for `DD_API_KEY` and `DD_APP_KEY`
  - You can find the value in your terminal by clicking
3. Navigate to https://app.datadoghq.com/ci/setup/code-analysis
4. Create a GitHub App
5. Create `.github/workflows/datadog-sca.yml` with the content from the onboarding page
6. Create `.github/workflows/datadog-static-analysis.yml` with the content from the onboarding page
7. Commit your changes and the YML files
8. Check the actions are correctly running in your GitHub Actions
9. You should see resutls on the Datadog page
10. Inspect the static analysis violations and dependencies violations

## Part 3: IDE and static analysis

1. Open the IDE
2. Open the folder that contains the code
3. Open the `service.py` file and fix the violation
4. Open the `database.py` and fix the violation, including the SQL violation
5. Once all issues fixed, commit your results: `git commit -m"update flask" && git push`
6. No violation should be found in Datadog for the static analysis

## Part 4: Software Composition Analysis

1. Open the datadog interface and see the violation
2. See the new version that fixes the issue
3. Open `requirements.txt` in your IDE
4. Update the `flask` dependency to `3.0.3`
5. Commit your result: `git commit -m"update flask" && git push`
6. See the result in your Datadog code analysis page