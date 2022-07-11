 Create an API that implements a POST method called `ingest_data` that accepts this body parameter:

```
from pydantic import BaseModel


class Data(BaseModel):
    feature_1: float
	feature_2: str
```

Imagine that this data is going to be used in a machine learning model. We want to make sure that the data is in the ranges we expect so our model doesn't output bogus results. To accomplish this, use `raise` with the `HTTPException` that is included with FastAPI. Your exception should raise an appropriate status code and tell the users what the issue is. For `feature_1` assure that the input is non-negative. For `feature_2` assure that there are 280 characters or less.

Then, use FastAPI's test client to ensure that your API gives the expected status code when it fails.

Lastly, add some metadata to your API including a name, brief description, and a version number.

Hint: FastAPI includes `HTTPException`. 

For more information on FastAPI's error handling see [here](https://fastapi.tiangolo.com/tutorial/handling-errors/) and for metadata see [here](https://fastapi.tiangolo.com/tutorial/metadata/).
