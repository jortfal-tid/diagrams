FROM python:3.12.7-slim-bullseye

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y --no-install-recomends install apt-utils

RUN \
  apt-get -y --no-install-recommends install \
  sudo \
  bash \
  curl \
  wget \
  unzip \
  vim \
  git \
  python3-pip

RUN pip3 install diagrams
