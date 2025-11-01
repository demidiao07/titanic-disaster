# Use the R image that includes tidyverse preinstalled
FROM --platform=linux/amd64 rocker/tidyverse:4.3.2

# Set working directory
WORKDIR /app

# Copy your R scripts into the container
COPY . .

# Install caret (tidyverse already included)
RUN Rscript -e "install.packages('caret', repos='https://cloud.r-project.org')"

# Run your Titanic R script
CMD ["Rscript", "run.R"]
