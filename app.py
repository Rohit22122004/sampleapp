from flask import Flask
import time, random, logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    delay = random.uniform(0.1, 1.0)
    time.sleep(delay)
    logging.info(f"Request processed in {delay:.2f}s")
    return f"Response time {delay:.2f}s\n"

app.run(host="0.0.0.0", port=5000)
