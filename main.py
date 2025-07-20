from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import random

app = FastAPI()

# Allow all CORS (for local/frontend use)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crop-specific research institutes
CROP_INSTITUTES = {
    "cotton": "कपाशी संशोधन केंद्र, नागपूर",
    "sugarcane": "वसंतदादा शुगर इन्स्टिट्यूट, पुणे",
    "soybean": "सोयाबीन संशोधन केंद्र, इंदूर",
    "pigeon pea": "ICAR - Indian Institute of Pulses Research, कानपूर",
    "chickpeas": "राष्ट्रीय कडधान्य संशोधन संस्था, कानपूर",
}

@app.get("/")
def read_root():
    return {"message": "AI Crop Doctor API is running!"}

@app.post("/analyze")
def analyze_crop(crop_name: str = Query(..., example="cotton")):
    crop_name = crop_name.lower().strip()
    institute = CROP_INSTITUTES.get(crop_name, "ICAR संस्था")
    damage_percent = random.randint(5, 15)
    yield_gain = random.randint(5000, 7000)

    response = {
        "crop": crop_name,
        "estimated_damage": f"अंदाजित नुकसान: {damage_percent}%",
        "recommendation": "AI Crop Doctor सल्ल्यानुसार तात्काळ उपाययोजना करा.",
        "yield_benefit": f"उपयुक्त उपाय केल्यास ५–१०% उत्पादनवाढीचा फायदा होऊ शकतो (₹{yield_gain} पर्यंत).",
        "reference": f"संदर्भ संस्था: {institute}"
    }

    return JSONResponse(content=response)
