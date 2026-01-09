from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={'error': str(exc)}
    )


@app.get('/exceptions')
def handle_exceptions():
    return 1 / 0



# Request
#  ↓
# Route matching
#  ↓
# Route function starts
#  ↓
# Exception raised
#  ↓
# FastAPI exception middleware
#  ↓
# Find matching handler
#  ↓
# Call handler
#  ↓
# Return JSONResponse
#  ↓
# Client receives response
