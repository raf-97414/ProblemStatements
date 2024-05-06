FROM ubuntu:latest

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y &&\
    apt-get install -y fortune-mod cowsay

# Copy the wisecow.sh script to the image
COPY wisecow.sh /usr/local/bin/

# Set the working directory
WORKDIR /usr/local/bin/

# Expose the default port
EXPOSE 4499

CMD ["sh","./wisecow.sh"]
