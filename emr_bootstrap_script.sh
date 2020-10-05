#!/bin/bash
sudo pip-3.6 install boto3 pandas findspark shapely py4j attrs
sudo pip-3.6 install geospark --no-dependencies
sudo aws s3 cp s3://nilabja-bootstrap-scripts/geospark-sql_2.3-1.3.0.jar /usr/lib/spark/jars/
sudo aws s3 cp s3://nilabja-bootstrap-scripts/geospark-1.3.0.jar /usr/lib/spark/jars/
sudo aws s3 cp s3://nilabja-bootstrap-scripts/geo_wrapper_2.11-0.3.0.jar /usr/lib/spark/jars/
sudo aws s3 cp s3://nilabja-bootstrap-scripts/postgresql-42.2.16.jar /usr/lib/spark/jars/