# geospark-emr-setup
Repository for Boilerplate Scripts for running GeoSpark on AWS EMR

This repository is intended to store the basic scripts for running GeoSpark on AWS EMR cluster.

1. emr_bootstrap_script.sh --> This script is used as a bootstrap script to install GeoSpark in EMR Cluster and copying the respective JAR files required for this spark application to appropiate SPARK_HOME folder

2. geospark-test-appl_upload_version.py --> Spark Application Script, to be supplied as a "STEP" to EMR Cluster
