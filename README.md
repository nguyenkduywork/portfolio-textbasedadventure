<h1>Text Adventure Game</h1>

<p>This project is a simple text-based adventure game built with Python and Flask.
The game allows users to navigate through different locations and pick up items as
they progress. The project uses Redis as a database to store the game state and the user's progress.</p>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>

<p>Before you can run the project, you will need to have the following installed on your machine:</p>

<ul><li>Python 3</li><li>Flask</li><li>Docker</li></ul>

<h3>Installation</h3>

<p>To get started, clone the project from GitHub:</p>

<pre><code>git clone https://github.com/nguyenkduywork/portfolio-textbasedadventure.git </code>
<code>cd [this project]</code></pre>

<p>Next, install the required dependencies:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<h3>Running the Project - Docker version</h3>

<p> First, you will need to have Docker Desktop up and running.
Afterwards, open a terminal, type these commands:</p>

<ol>
    <li>
        <code>
            docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
        </code>
    </li>
    <li>
        <code>
            docker exec -it redis-stack redis-cli
        </code>
    </li>
</ol>

<p> You should have a port opened up for you, type "ping"
, if it sends back "PONG", it means the installation is working.</p>

<p> <b> The 6379 is the REDIS_DOCKER_PORT that you need to fill the value in the .env file</b></p>

<p> Example: REDIS_DOCKER_PORT = 6379</p>

<p> <b>Next: define a password for the flask app in the .env file </b></p>

<p> Example: FLASK_SECRET = "mysecretkey"</p>

<p><b> Lastly: define the host_ip in the .env file</b></p>

<p> Example: HOST_IP = "127.0.0.1"</p>

<p><b> cd back to the project location if you are not already inside,
type this in a terminal: </b></p>

<code>flask run </code>

<h3>How to Play</h3>

<p>The game is a simple text-based adventure where you can navigate through different locations and pick up items as you progress. To play the game, enter a command into the input field and click "Submit". The available commands are:</p>

<ul>
    <li>
        <code>move north</code>
    </li>
    <li>
        <code>move south</code>
    </li>
    <li>
        <code>move east</code>
    </li>
    <li>
        <code>move west</code>
    </li>
</ul>

<p>As you play the game, your progress will be stored in Redis. This means that you can close the browser window and come back to the game later, and your progress will still be saved.</p>

<h2>Redis</h2>

<p>This project uses Redis as a database to store the game state and the user's progress. Redis is an in-memory data structure store that can be used as a database, cache, and message broker. It is lightweight and fast, making it an ideal choice for real-time applications like this game.</p>

<p>To run the game with Redis, you will need to have Redis installed on your machine. You can download Redis from the <a href="https://redis.io/download" target="_new">official website</a>.</p>

<h2>Conclusion</h2>

<p>This project is a simple text-based adventure game that demonstrates how to use Redis as a database to store user data. It is a fun and interactive way to learn how to use Redis in a real-world application. If you have any questions or feedback, please feel free to contact me at [your-email-address]. Thank you for playing the game!</p>