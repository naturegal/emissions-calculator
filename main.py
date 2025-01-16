from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QueryRequest(BaseModel):
    num_queries: int

class EmissionsResponse(BaseModel):
    total_queries: int
    total_emissions_kg_co2: float

ENERGY_PER_QUERY_KWH = 0.005
EMISSION_FACTOR_KG_CO2_PER_KWH = 0.4

@app.post("/calculate_emissions", response_model=EmissionsResponse)
def calculate_emissions(request: QueryRequest):
    total_emissions = request.num_queries * ENERGY_PER_QUERY_KWH * EMISSION_FACTOR_KG_CO2_PER_KWH
    return EmissionsResponse(
        total_queries=request.num_queries,
        total_emissions_kg_co2=round(total_emissions, 6),
    )
