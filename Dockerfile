# Build the base image from redhat ubi8 python-39
FROM registry.access.redhat.com/ubi8/python-39:1

# Install requirements
# Copy files to the /app folder in the container
COPY ./ /app/
COPY ./requirements.txt /app/requirements.txt

# Set the working directory in the container to be /app
WORKDIR /app

# Upgrade pip to latest version
RUN pip3 install --upgrade pip

# Install the packages from requirements.txt in the container
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
ENV PORT=8000
EXPOSE 8000

ENV HOST="0.0.0.0"
ENV MONITOR="https://monitor.statnipokladna.cz/api/monitorws"
ENV STORE_SERVICE="https://pilarmi2-store-service.azurewebsites.net"
ENV ARES="https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty"

# Start service
CMD ["python", "main.py"]
