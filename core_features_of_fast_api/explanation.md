# Core Features of Fast API demo

The first file, `main.py`, contains the definition of the API. There are two methods, a post and a get.

The post takes a JSON object with the format defined by the `pydantic` model `TaggedItem`. In this case, this item is some object with a `name`, one or more `tags` in the form of strings, and an integeter `item_id`.

The get method is used to retrieve `count` instances of `item_id`. This example is just a stub, but one can imagine the post method populating a database with various items and then the get method would be used to retrieve items from the database.

To run this we use the command `uvicorn main:app --reload`. This launches a local server which we use to interact with our API.

In `sample_request.py` we see part of that functionality at work. A post request is made to the local host where our API is running. This post reqest contains a JSON object which is a Hitchhking Kit that has the tags of book and towel, and, surprising to fans of Douglas Adams, it has an `item_id` of 23. To send this post request to our running server use `python sample_request.py` while the server is running.
