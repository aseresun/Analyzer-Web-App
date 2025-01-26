# Analyzer Web App

## Assumptions

The limited amount of time suggests using a tool that already exists as the basis for processing.

- First option: [Template-Analyzer](https://github.com/Azure/template-analyzer) can analyze ARM files for security issues and provide a report containing details, suggestions, and a summary.
- Second option: [Azure Resource Manager Template Toolkit (arm-ttk)](https://github.com/Azure/arm-ttk) can analyze and test ARM files. This requires Powershell which would adjust the deployment.
- The web app is running inside a devcontainer for fast development and portability.

## Expected Outcomes

- Users can upload a JSON file.
- The web app will process the uploaded file and return the output.

## Findings

- Tested Template-Analyzer, but output did not produce the desired report structure.
- Tested ARM-TTK, but the output did not produce the desired security elements.
- Provided `Resource` data contained errors which broke Template-Analyzer, specifically `resource.open_ports`. ARM-TTK succeeded but only showed minor syntax errors.
- Testing with an ARM sample template file succeded
- Using both tools would provide a better status of ARM security, best practices, and viabiltity.
- The tools are flexible enough to add custom/3rd party templates
- I didnt have enough time to properly handle the variations in report output

## Required Packages

- Docker
- Visual Studio
  - Dev Containers

- Template-Analyzer (via Dockerfile)
  - Python
  - Flask

- ARM-TTK (via Dockerfile)
  - Powershell
  - Python
  - Flask

## Steps to Start and Test the App

1. **Build and Start the DevContainer**:
    - Open the project in Visual Studio Code.
    - Reopen in Container (using the Remote - Containers extension).

2. **Run the Web App**:
    ```sh
    python src/app.py
    ```

3. **Test the App**:
    - Use a web browser to `http://localhost:5000` OR a tool like Postman or curl to upload a file to `http://localhost:5000/upload`.
    - Example using curl:

    ```sh
    curl -F 'file=@test/sample.json' http://localhost:5000/upload
    ```

4. **Expected Response**:
    - The response will contain the output from the `TemplateAnalyzer` execution.
