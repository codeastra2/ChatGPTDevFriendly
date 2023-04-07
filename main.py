import openai
import time
from functools import wraps
import requests


def retry(tries=4, delay=3, backoff=2):
    """
    Retries a function or method until it succeeds or the number of retries is exceeded.

    :param tries: the maximum number of times to retry (default 4).
    :param delay: the initial delay between retries in seconds (default 3).
    :param backoff: the backoff multiplier (e.g. value of 2 will double the delay each retry) (default 2).
    """

    def deco_retry(func):
        @wraps(func)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except (
                    openai.error.APIError,
                    requests.exceptions.RequestException,
                ) as e:
                    print(f"Error occurred: {str(e)}")
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)

        return f_retry

    return deco_retry


def dot_product(list1, list2):
    # Check if the lengths of the two lists are equal
    if len(list1) != len(list2):
        raise ValueError("Lists must have same length")

    # Calculate the dot product using a loop
    dot_product = 0
    for i in range(len(list1)):
        dot_product += list1[i] * list2[i]

    return dot_product


class ChatGptSmartClient(object):
    """
    This is a wrapper class for the chatgpt python api,
    it is meant to provide developers a smooth expereince in
    developing chatgpt applications of their own without the need
    for worrying about things like retries, tracking message history
    or storing messages. This runs on top of the Chat APIs provided by OpenAI
    read more on that here: https://platform.openai.com/docs/guides/chat .
    """

    def __init__(self, api_key: str, model: str):
        openai.api_key = api_key

        self.instruction_msgs = {
            "role": "system",
            "content": "You are a  useful assistant",
        }
        self.prev_msgs = [self.instruction_msgs]
        self.model = model

    @retry()
    def query(self, query: str, w_context=True, add_to_context=True):
        # TODO: We coud get the embeddings, cache and further use them to speed up the results.
        # self.get_embeddings(query=query)

        query = {"role": "user", "content": query}

        if w_context:
            msgs = self.prev_msgs[:]
            msgs.append(query)
            response = openai.ChatCompletion.create(model=self.model, messages=msgs)
        else:
            msgs = [self.instruction_msgs, query]
            response = openai.ChatCompletion.create(model=self.model, messages=msgs)

        f_resp = response["choices"][0]["message"]

        if add_to_context:
            self.prev_msgs.append(f_resp)

        return f_resp

    def erase_history(self):
        self.prev_msgs = [self.instruction_msgs]

    # This function is used for getting embeddings and hence maybe
    # used to speedup the system by caching.
    def get_embeddings(self, query: str):
        response = openai.Embedding.create(input=query, model="text-embedding-ada-002")
        embeddings = response["data"][0]["embedding"]
        print(len(embeddings))

    def rollback_conversation(self):
        pass
