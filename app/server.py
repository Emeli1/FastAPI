from fastapi import FastAPI
from lifespan import lifespan
from dependency import SessionDependency
from schema import (CreateAdvRequest, IdResponse, GetAdvResponse,
                    SearchAdvResponse, UpdateAdvRequest)
import crud
from models import Advertisement
from sqlalchemy import select


app = FastAPI(
    title="Advertisements API",
    description="buy and sale",
    lifespan=lifespan
)


@app.post("/advertisement", response_model=IdResponse)
async def create_adv(session: SessionDependency, item: CreateAdvRequest):
    advertisement = Advertisement(
        title = item.title,
        description = item.description,
        price = item.price,
        owner = item.owner
    )
    await crud.add_item(session, advertisement)
    return advertisement.id_dict


@app.get("/advertisement/{advertisement_id}", response_model=GetAdvResponse)
async def get_adv(session: SessionDependency, advertisement_id: int):
    advertisement = await crud.get_item_by_id(session, Advertisement, advertisement_id)
    return advertisement.dict


@app.get("/advertisement/", response_model=SearchAdvResponse)
async def search_adv(session: SessionDependency, title: str, price: int):
    query = select(Advertisement).where(Advertisement.title == title,
                                        Advertisement.price == price).limit(10000)
    advertisements = await session.scalars(query)
    return {"advertisements": [advertisement.id for advertisement in advertisements]}


@app.patch("/advertisement/{advertisement_id}", response_model=IdResponse)
async def update_adv(session: SessionDependency, advertisement_id: int, item: UpdateAdvRequest):
    advertisement = await crud.get_item_by_id(session, Advertisement, advertisement_id)
    if item.title is not None:
        advertisement.title = item.title
    if item.description is not None:
        advertisement.description = item.description
    if item.price is not None:
        advertisement.price = item.price
    if item.owner is not None:
        advertisement.owner = item.owner

    await crud.add_item(session, advertisement)
    return advertisement.id_dict


@app.delete("/advertisement/{advertisement_id}", response_model=IdResponse)
async def delete(session: SessionDependency, advertisement_id: int):
    advertisement = await crud.get_item_by_id(session, Advertisement, advertisement_id)
    await crud.delete_item(session, advertisement)
    return advertisement.id_dict