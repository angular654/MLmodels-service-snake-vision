# MLmodels-service-snake-vision
  
## Development
    docker run -d --name some-rabbit -p 5672:5672 -p 5673:5673 -p 15672:15672 rabbitmq:3-management
    uvicorn main:app --reload
