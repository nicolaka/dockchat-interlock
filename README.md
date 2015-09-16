##Dockchat is a simple Python+Mongo app built to demonstrate various Docker features.Dockchat-interlock showcases dockchat with interloack+haproxy running on swarm.You need Docker Compose to run this app( 'pip install -U docker-compose')

To run this app,manually plug in the Swarm Master IP or DNS name in the docker-compose.yml,

Then run the following to run the app:

('dockchat-interlock# docker-compose up -d')

To see the app, go to the hostname of the instances that is running Interloack
http://ec2-xx-xx-xx-.amazoneaws.com

To see HAProxy stats, go to 
http://ec2-xx-xx-xx-.amazoneaws.com/haproxy?stats and user stats/interlock to login.






