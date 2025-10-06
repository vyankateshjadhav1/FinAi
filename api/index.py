import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

# Import your routers
from agents.ca_agent.router import router as ca_router
from agents.ca_agent.secure_router import secure_router
from agents.ITR_agent.router import router as itr_router
from agents.equity_agent.router import router as equity_router
from agents.assest_agent.router import router as asset_router
from agents.chatbot.router import router as chatbot_router
from agents.pict_route import router as pict_router

# Create FastAPI app
app = FastAPI(title="FinAI API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://*.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ca_router, prefix="/api")
app.include_router(secure_router, prefix="/api")
app.include_router(itr_router, prefix="/api")
app.include_router(equity_router, prefix="/api")
app.include_router(asset_router, prefix="/api/asset", tags=["asset"])
app.include_router(chatbot_router, prefix="/api")
app.include_router(pict_router, prefix="/api", tags=["pictorial"])

@app.get("/api")
async def root():
    return {
        "message": "FinAI API is running!",
        "available_endpoints": {
            "ca_agent": "/api/ca",
            "secure_ca_agent": "/api/secure",
            "itr_agent": "/api/itr",
            "equity_agent": "/api/equity",
            "asset_agent": "/api/asset",
            "chatbot": "/api/chatbot",
            "health": "/api/health"
        }
    }

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "FinAI API"}

# Mangum handler for Vercel
handler = Mangum(app)