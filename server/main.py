from typing import Union
from fastapi import FastAPI,Query
import devtoscraper
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/scrape/{search_query}")
async def scrape_data(search_query: str,limit: int = Query(20, description="Number of results to fetch")):
    print(search_query)
    results = await devtoscraper.scrape_dev_to_search_results(search_query)
    return results

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)