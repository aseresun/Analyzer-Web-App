FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install dependencies
RUN apt-get update && apt-get install -y unzip

# Install Flink
RUN pip install Flink

# Download and install Template Analyzer
RUN wget https://github.com/Azure/template-analyzer/releases/download/0.8.1/TemplateAnalyzer-linux-x64.zip -O /tmp/template-analyzer.zip && \
    unzip /tmp/template-analyzer.zip -d /usr/local/bin/TemplateAnalyzer && \
    chmod +x /usr/local/bin/TemplateAnalyzer/TemplateAnalyzer

# Download and install Azure Resource Manager Template Toolkit (ARM-TTK)
#RUN wget https://github.com/Azure/arm-ttk/releases/download/20240328/arm-ttk.zip -O /tmp/arm-ttk.zip && \
#    unzip /tmp/arm-ttk.zip -d /usr/local/bin && \
#    chmod +x /usr/local/bin/arm-ttk/arm-ttk/Test-AzTemplate.sh
