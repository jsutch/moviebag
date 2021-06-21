"""
This is removed from app.py to avoid circular dependandies with services
"""
from app import app

# debug
#app.run(port=5000,debug=True)
# prod
app.run(port=5000)
