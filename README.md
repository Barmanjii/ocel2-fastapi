# ocel2-fastapi

You will need the Poetry for this Project as we are mainiaining all the Requirements via the Poetry

- Please head to this official download page of Poetry and install it.
  `https://python-poetry.org/docs/#installing-manually`

- Head into the project directory and use `poetry shell` then `poetry install --no-cache` to install the dependencies in a virtual env created by the poetry.

- make sure to connect your database instance before running.

  - Can you anything pgadmin or dbeaver
  - Check the `MakeFile` for the port and password for the db.
  - In this we are using the postgre docker image. so you can just run the `Make Commands` like `make prepare' to install the postgres image.
  - After creating the db and succefull connection with db you can run the **ocel2-db-schema**

- Feel free to use the debug mode or the terminal method with `uvicorn`

---

## Thanks for using this.
