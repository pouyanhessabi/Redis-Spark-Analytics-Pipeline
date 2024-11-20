from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

# Connect to Redis
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)


@app.route('/add-city', methods=['POST'])
def add_city():
    # Parse the input JSON
    data = request.json
    country_code = data.get('country_code')
    city = data.get('city')

    if not country_code or not city:
        return jsonify({"error": "The country code and city are required"}), 400

    # Add the city to the set in Redis
    redis_client.sadd(country_code, city)

    return jsonify({"message": f"City '{city}' added to country code '{country_code}'"}), 200


@app.route('/get-cities/<country_code>', methods=['GET'])
def get_cities(country_code):
    # Retrieve the set of cities for the given country code
    cities = redis_client.smembers(country_code)  # Get all members of the set
    if not cities:
        return jsonify({"error": f"No cities found for country code '{country_code}'"}), 404

    return jsonify({"country_code": country_code, "cities": list(cities)}), 200


@app.route('/')
def index():
    return "App is running"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
