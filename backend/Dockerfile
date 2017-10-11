FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV USING_DOCKER 1


RUN apt-get update



RUN mkdir /root/.ssh && chmod 700 /root/.ssh
RUN ssh-keyscan -H -p 10022 git.genomefoundry.org >> /root/.ssh/known_hosts
RUN ssh-keyscan -H -p 10022 178.62.46.213 >> /root/.ssh/known_hosts

# Add a deploy key
# COPY ./.ssh-deploy-keys/id_rsa  /root/.ssh/id_rsa
# COPY ./.ssh-deploy-keys/id_rsa.pub /root/.ssh/id_rsa.pub
# RUN chmod 600 /root/.ssh/id_rsa


RUN mkdir /code
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

# Remove SSH keys
RUN rm -rf /root/.ssh/

ADD . /code/

# For partial build, increment the number below. All subsequent lines will be
# rebuilt without cache, while all lines above will built using cache.
ARG CACHEBUSTER=44
