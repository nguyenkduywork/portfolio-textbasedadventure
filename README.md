<h1>Welcome to the Exciting World of Text Adventure Games!</h1>
<p>Buckle up and get ready to embark on a thrilling adventure with our brand new Text Adventure Game, built with Python and Flask! Are you ready to explore different locations and pick up hidden treasures as you go? Then let's get started!</p>
<h2>Getting Started</h2>
<h3>Prerequisites</h3>
<p>Before you dive into this game, make sure you have the following prerequisites installed:</p>
<ul>
    <li>Python 3</li>
    <li>Flask</li>
    <li>Docker</li>
</ul>
<h3>Installation</h3>
<p>To get started, clone the project from our GitHub repository:</p>
<pre><code>git clone https://github.com/nguyenkduywork/portfolio-textbasedadventure.git </code>
<code>cd [this project]</code></pre>
<p>Next, install all the necessary dependencies by running the following command:</p>
<pre><code>pip install -r requirements.txt</code></pre>
<h3>Running the Project with Docker</h3>
<p>We have made running this game super simple with Docker! Just follow these easy steps:</p>
<ol>
    <li>
        <p>Ensure that you have Docker Desktop up and running. Open a terminal and enter the following command to set up Redis:</p>
        <pre><code>
            docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
        </code></pre>
    </li>
    <li>
        <p>Next, access Redis by typing the following command into your terminal:</p>
        <pre><code>
            docker exec -it redis-stack redis-cli
        </code></pre>
    </li>
    <li>
        <p>You should now have access to Redis. Type "ping" and if you receive a response of "PONG", you're good to go!</p>
    </li>
    <li>
        <p>Fill in the required fields in your <code>.env</code> file. For example, set the REDIS_DOCKER_PORT to 6379, define a password for your Flask app in FLASK_SECRET, and set the HOST_IP to 127.0.0.1</p>
    </li>
    <li>
        <p>cd back to the project location if you are not already inside, and type the following command into your terminal to run the game:</p>
        <code>flask run </code>
    </li>
</ol>
<h3>How to Play</h3>
<p>The Text Adventure Game is an exciting way to explore different locations and discover hidden treasures. To play the game, simply enter a command into the input field and click "Submit". The available commands include:</p>
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
<p>Your progress will be stored in Redis, which means you can easily pick up where you left off if you need to take a break.</p>
<h2>Redis</h2>
<p>Redis is an in-memory data structure store that is used in this game to store the user's progress and game state. 
It is lightweight and fast, making it an ideal choice for real-time applications like our Text Adventure Game. </p>

<h2>Conclusion</h2>

<p>This project is a simple text-based adventure game that demonstrates how to use Redis as a database to store user data. 
It is a fun and interactive way to learn how to use Redis in a real-world application. 
If you have any questions or feedback, please feel free to contact me at <b>nguyenkduywork@gmail.com</b>. 
Thank you for playing the game!</p>