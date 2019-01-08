# Locust Production Load Testing 

- REF:: https://www.promptworks.com/blog/load-testing-with-locust

## Install locust 
```
pip install locustio
```

## Run locust in EC2
MAIN_URL = The main url thats the root URL that should be tested
- RUN: locust --host=MAIN_URL
- GOTO: http://localhost:8089/
- SLAVE: locust --host=MAIN_URL --slave --master-host=http://localhost:8089/