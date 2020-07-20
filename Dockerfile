# Create common base stage
FROM python:3.6-slim

# Install common libraries
RUN apt-get update -qq \
 && apt-get install -y --no-install-recommends \
    # required by psycopg2 at build and runtime
    libpq-dev \
     # required for health check
    curl \
 && apt-get autoremove -y

# Install all required build libraries
RUN apt-get update -qq \
 && apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    git

WORKDIR /src

# Copy only what we really need
COPY README.md .
COPY setup.py .
COPY requirements.txt .

# Install Rasa and its dependencies
RUN pip install -U pip && pip install --no-cache-dir -r requirements.txt

# Install Rasa as package
COPY cogniwide ./cogniwide
RUN pip install -e .

WORKDIR /app

# Create a volume for temporary data
VOLUME /tmp

ENTRYPOINT ["cogniwide"]
CMD ["--help"]
