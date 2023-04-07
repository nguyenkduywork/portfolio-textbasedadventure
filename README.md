<h1>Text Adventure Game</h1>

<p>This project is a simple text-based adventure game built with Python and Flask.
The game allows users to navigate through different locations and pick up items as
they progress. The project uses Redis as a database to store the game state and the user's progress.</p>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>

<p>Before you can run the project, you will need to have the following installed on your machine:</p>

<ul><li>Python 3</li><li>Flask</li><li>Redis</li></ul>

<h3>Installation</h3>

<p>To get started, clone the project from GitHub:</p>

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>shell</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-shell"><span class="hljs-meta prompt_">$ </span><span class="bash">git <span class="hljs-built_in">clone</span> https://github.com/&lt;your-username&gt;/text-adventure-game.git</span>
<span class="hljs-meta prompt_">$ </span><span class="bash"><span class="hljs-built_in">cd</span> text-adventure-game</span>
</code></div></div></pre>

<p>Next, install the required dependencies:</p>

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>ruby</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-ruby"><span class="hljs-variable">$ </span>pip install -r requirements.txt
</code></div></div></pre>

<h3>Running the Project</h3>

<p>To run the project, you will need to start the Redis server first. Open a new terminal window and run the following command:</p>

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>ruby</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-ruby"><span class="hljs-variable">$ </span>redis-server
</code></div></div></pre>

<p>This will start the Redis server on the default port (6379).</p>

<p>Next, open another terminal window and navigate to the project directory. Run the following command to start the Flask server:</p>

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>ruby</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-ruby"><span class="hljs-variable">$ </span>python app.py
</code></div></div></pre>

<p>This will start the Flask server on <code>http://localhost:5000/</code>. Open your web browser and navigate to this URL to play the game.</p>

<h3>How to Play</h3>

<p>The game is a simple text-based adventure where you can navigate through different locations and pick up items as you progress. To play the game, enter a command into the input field and click "Submit". The available commands are:</p>

<ul><li><code>move north</code></li><li><code>move south</code></li><li><code>move east</code></li><li><code>move west</code></li><li><code>pickup item</code></li></ul>

<p>As you play the game, your progress will be stored in Redis. This means that you can close the browser window and come back to the game later, and your progress will still be saved.</p>

<h2>Redis</h2>

<p>This project uses Redis as a database to store the game state and the user's progress. Redis is an in-memory data structure store that can be used as a database, cache, and message broker. It is lightweight and fast, making it an ideal choice for real-time applications like this game.</p>

<p>To run the game with Redis, you will need to have Redis installed on your machine. You can download Redis from the <a href="https://redis.io/download" target="_new">official website</a>.</p>

<h2>Conclusion</h2>

<p>This project is a simple text-based adventure game that demonstrates how to use Redis as a database to store user data. It is a fun and interactive way to learn how to use Redis in a real-world application. If you have any questions or feedback, please feel free to contact me at [your-email-address]. Thank you for playing the game!</p>