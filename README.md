<!--
title: 'Serverless Framework Python Flask API on AWS'
description: 'This template demonstrates how to develop and deploy a simple Python Flask API running on AWS Lambda using the traditional Serverless Framework.'
layout: Doc
framework: v3
platform: AWS
language: Python
priority: 2
authorLink: 'https://github.com/serverless'
authorName: 'Serverless, inc.'
authorAvatar: 'https://avatars1.githubusercontent.com/u/13742415?s=200&v=4'
-->

# Doggo Serverless Service

# Overview

The Doggo IoT API is a Python Flask application designed to handle the ingestion of IoT device payloads for the Doggo IoT project. Leveraging the Serverless Framework, this API is deployed on AWS Lambda using CloudFormation for infrastructure management and CloudWatch for monitoring.


# How to set up this project

Please make sure that you have a working knowledge of docker and have access to a running PostgreSQL instance. In your docker-compose file, set your environment parameters and in your serverless.yml file, set your DATABASE_URL with a connection string to your running PostgreSQL instance.


