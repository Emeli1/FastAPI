from typing import Optional

from fastapi import FastAPI, Query
from fastapi.params import Depends
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession

from lifespan import lifespan
from dependency import SessionDependency, get_session
from schema import (CreateAdvRequest, IdResponse, GetAdvResponse,UpdateAdvRequest)
import crud
from models import Advertisement


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



@app.get("/advertisement/")
async def search_adv(
    session: AsyncSession = Depends(get_session),
    title: Optional[str] = Query(default=None),  # Явное указание default=None
    description: Optional[str] = Query(default=None),
    price: Optional[str] = Query(default=None),
    owner: Optional[str] = Query(default=None)
):
    conditions = []

    if title:
        conditions.append(Advertisement.title == title)
    if description:
        conditions.append(Advertisement.description == description)
    if price:
        conditions.append(Advertisement.price == price)
    if owner:
        conditions.append(Advertisement.owner == owner)

    query = select(Advertisement)
    if conditions:
        query = query.where(or_(*conditions))

    advs = await session.execute(query)
    advs_res = advs.scalars().all()
    return {"results": [adv.dict for adv in advs_res]}


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