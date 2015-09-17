##Dockchat 
Dockchat is a simple Python+Mongo app built to demonstrate various Docker features. Dockchat-interlock showcases dockchat with Interlock+ HAproxy/NGINX running on swarm.  If you don't have docker-compose, install it with
`pip install -U docker-compose`

To run this app, manually add the Engine or Swarm Master IP or DNS name in the docker-compose.yml. If you're using Engine, make sure to also add 
Engine's IP/DNS to the PROXY_BACKEND_OVERRIDE_ADDRESS env variables.

Then run the following to run the app:

`docker-compose up -d`

To see the app, ensure that your laptop can resolve `docker-training.com` to the IP of the node running the Interloack container. To do so, add an entry in your /etc/hosts pointing to that IP. 

To see HAProxy stats, go to https://<IP_OR_DNS_OF_INTERLOCK>/haproxy?stats 
e.g: http://ec2-xx-xx-xx-.amazoneaws.com/haproxy?stats and user stats/interlock to login.






