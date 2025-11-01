FROM r-base:4.3.2

WORKDIR /app

# Install caret only (optional)
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev libssl-dev libxml2-dev \
    && rm -rf /var/lib/apt/lists/*

RUN R -e "install.packages('caret', repos='https://cloud.r-project.org')"

COPY src/r_app/titanic_model.R .
COPY src/data ./data

CMD ["Rscript", "titanic_model.R"]

