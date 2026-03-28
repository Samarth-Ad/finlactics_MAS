from play_ground import getPlayground
from phi.playground.serve import serve_playground_app

app = getPlayground()
if __name__ == "__main__":
    serve_playground_app("main:app",reload=True)

    
