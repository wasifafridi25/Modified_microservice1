# Modified_microservice1
Here I have modified my first microservice. It first makes a third-party API call to get the zip code for the entered city and state same like Microservice 1.
But after that it makes a call to microservice 2. So, in order for this to work make sure you first start microservice 2 and then start this modified_microservice 1.
Run the python file of microservice 2 like this:

![Screenshot (282)](https://user-images.githubusercontent.com/122373939/217372420-f67925b5-331f-411b-9f01-bc17ba8d78a6.png)
Listen on port 8001. So, use this address: localhost:8001/weather/94539

Now run the modified_microservice1 python file like this:
![Screenshot (283)](https://user-images.githubusercontent.com/122373939/217372963-55ed6c02-3234-411a-bf11-8cc528c77477.png)
View it on the address: http://localhost:8000/cityweather?city=Fremont&state=CA

Now to containerize them we have to use networking so that they are able to communicate with each.
We can build a docker-compose.yaml file and run all the containers together or manually run them in the same network.
Here's how you can achieve this:
Build the image first:
![Screenshot (284)](https://user-images.githubusercontent.com/122373939/217374375-3c5d29a2-9c9e-45cf-b101-98d15b3488e8.png)
Create a common network using this command: docker network create microservice
I named my network microservices, you can name whatever you want.
And then run the two containers in the same network using these commands:
docker run -dp 8001:8001 --network microservices microservice2:1.0
docker run -dp 5000:5000 --network microservices microservice1:2.0

![Screenshot (290)](https://user-images.githubusercontent.com/122373939/217375148-26061d0d-ec7b-47ea-a124-bba4f60c3462.png)

![Screenshot (291)](https://user-images.githubusercontent.com/122373939/217375179-9422905e-5048-4ab4-8354-3edc8231ee73.png)
![Screenshot (279)](https://user-images.githubusercontent.com/122373939/217375317-5f97733b-8716-45c3-b6b9-b3c686a94d83.png)
Then tag the docker image: docker tag microservice1:2.0 wasifafridi25/modified_microservice1
Then push it into docker hub: docker push wasifafridi25/modified_microservice1

![Screenshot (295)](https://user-images.githubusercontent.com/122373939/217375667-92fa5199-a545-481d-b591-e58dae66bb96.png)
using this link you can find the docker image: https://hub.docker.com/r/wasifafridi25/modified_microservice1
Pull the docker image using this command: docker pull wasifafridi25/modified_microservice1
And run it as a container. Don't forget to pull microservice2 and run it first. As this modified microservice1 makes a call to microservice 2, so it's essential 
you run micrservice 2 first.
