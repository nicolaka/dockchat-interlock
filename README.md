##Dockchat 
Dockchat is a simple Python+Mongo app built to demonstrate various Docker features. Dockchat-interlock showcases dockchat with Interlock+ HAproxy/NGINX running on Swarm or standalone Engine.  If you don't have docker-compose, install it with
`pip install -U docker-compose`

To run this app, manually add the Engine or Swarm Master IP/DNS in the docker-compose.yml. If you're running this against a standalone Engine, make sure to also add 
the Engine's IP/DNS to the (YOUR_PREFERRED_PLUGIN)_PROXY_BACKEND_OVERRIDE_ADDRESS env variable in the docker-compose.yml file. If you're running this on Swarm, make sure to delete (YOUR_PREFERRED_PLUGIN)_PROXY_BACKEND_OVERRIDE_ADDRESS env variable from the compsoe file.

Then run the following to run the app:

`docker-compose up -d`

To see the app, ensure that your laptop can resolve `demo.interlock.com` to the IP of the node running the Interloack container. To do so, add an entry in your /etc/hosts pointing to that IP. 

To see HAProxy stats, go to demo.interlock.com/haproxy?stats and use stats/interlock to login.






