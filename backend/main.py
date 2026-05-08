from fastapi import FastAPI, UploadFile, File
import librosa
import numpy as np
import io
import shutil
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Audio Analysis API is running"}

@app.post("/analyze")
async def analyze_audio(file: UploadFile = File(...)):
    # Save file temporarily
    temp_filename = f"temp_{file.filename}"
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # Load audio file
        y, sr = librosa.load(temp_filename)
        
        # 1. Detect BPM (Tempo)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        
        # 2. Detect Key
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        key_index = np.argmax(np.mean(chroma, axis=1))
        keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        detected_key = keys[key_index]
        
        # 3. Mock Genre Detection (Real genre detection requires ML models)
        genres = ["Lo-fi", "Hip Hop", "Electronic", "Ambient", "Jazz"]
        detected_genre = np.random.choice(genres)
        
        return {
            "filename": file.filename,
            "bpm": round(float(tempo), 2),
            "key": detected_key,
            "genre": detected_genre,
            "status": "success"
        }
    except Exception as e:
        return {"error": str(e), "status": "failed"}
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
