from fastapi import FastAPI, HTTPException
from src.cleeroute.crew import Cleeroute
from src.cleeroute.models import CourseInput

app = FastAPI()

# python -m src.cleeroute.main  // pour lancer le serveur

@app.post("/generate")
def generate_course(request: CourseInput):
    """Génère la structure d'un cours complet"""
    try:
        result = Cleeroute().crew().kickoff(inputs=request.model_dump())
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)