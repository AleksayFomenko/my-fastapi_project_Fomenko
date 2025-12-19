from fastapi import FastAPI, HTTPException
from typing import List
from .db import init_db, get_conn
from .models import ItemCreate, ItemUpdate, ItemOut

app = FastAPI(title="TODO-service", version="1.0.0")

@app.on_event("startup")
def startup():
	init_db()

@app.post("/items", response_model = ItemOut, status_code = 201)
def create_item(payload: ItemCreate):
	with get_conn() as conn:
		cur = conn.execute(
			"INSERT INTO items (title, description, completed) VALUES (?, ?, ?)",
			(payload.title, payload.description, 0)
		)
		conn.commit()
		item_id = cur.lastrowid
		row = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
		return _row_to_item(row)
@app.get("/items", response_model = List[ItemOut])

def list_items():
	with get_conn() as conn:
		rows = conn.execute("SELECT * FROM items ORDER BY id DESC").fetchall()
		return [_row_to_item(r) for r in rows]

@app.get("/items/{item_id}", response_model = ItemOut)
def get_item(item_id: int):
	with get_conn() as conn:
		row = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
		if not row:
			raise HTTPException(status_code = 404, detail = "Item not found")
		return _row_to_item(row)

@app.put("/items/{item_id}", )
def update_item(item_id: int, payload: ItemUpdate):
	with get_conn() as conn:
		row = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()

		if not row:
			raise HTTPException(status_code)
		conn.execute(
			"""	
			UPDATE items
			SET
				title = COALESCE(?, title),
				description = COALESCE(?, description),
				completed = COALESCE(?, completed)
				WHERE id = ?
			""",
			(
				payload.title,
				payload.description,
				int(payload.completed) if payload.completed is not None else None,
				item_id
			)
		)
		conn.commit()

		row = conn.execute(
			"SELECT * FROM items WHERE id = ?", (item_id,)
		).fetchone()

		return _row_to_item(row)

@app.delete("/items/{item_id}", status_code = 204)
def delete_item(item_id: int):
	with get_conn() as conn:
		row = conn.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
		if not row:
                        raise HTTPException(status_code = 404, detail = "Item not found")
		conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
		conn.commit()
		return None

def _row_to_item(row) -> ItemOut:
	return ItemOut(
		id = row["id"],
		title = row["title"],
		description = row["description"],
		completed = bool(row["completed"]),
		created_at = row["created_at"]
	)

