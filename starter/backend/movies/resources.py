from flask import jsonify
from flask.views import MethodView

# Dummy database with integer IDs matching /movies/<int:movie_id>
movies = {
    1: {"id": 1, "title": "Top Gun: Maverick", "description": "Fighter planes"},
    2: {"id": 2, "title": "Sonic the Hedgehog", "description": "Blue Sega character"},
    3: {"id": 3, "title": "A Quiet Place", "description": "Scary monsters"},
}


class Movies(MethodView):
    def get(self, movie_id):
        if movie_id is None:
            # Return list of all movies formatted with id and title
            return jsonify({
                "movies": [
                    {"id": m_id, "title": m_data["title"], "description": m_data["description"]}
                    for m_id, m_data in movies.items()
                ]
            }), 200
        
        # Single movie lookup
        if movie_id in movies:
            return jsonify({"movie": movies[movie_id]}), 200
            
        return jsonify({"message": "Movie not found"}), 404

    